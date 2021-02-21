import filecmp 
import os

def dirs_same_enough(dir1,dir2,report=False):
    ''' use os.walk and filecmp.cmpfiles to
    determine if two dirs are 'same enough'.

    Args:
        dir1, dir2:  two directory paths
        report:  if True, print the filecmp.dircmp(dir1,dir2).report_full_closure()
                 before returning

    Returns:
        bool

    '''
    # os walk:  root, list(dirs), list(files)
    # those lists won't have consistent ordering,
    # os.walk also has no guaranteed ordering, so have to sort.
    walk1 = sorted(list(os.walk(dir1)))
    walk2 = sorted(list(os.walk(dir2)))

    def report_and_exit(report,bool_):
        if report:
            filecmp.dircmp(dir1,dir2).report_full_closure()
            return bool_
        else:
            return bool_

    if len(walk1) != len(walk2):
        comparison = filecmp.dircmp(dir1, dir2)
        return comparison.report_full_closure()
       #  false_or_report(report)

    for (p1,d1,fl1),(p2,d2,fl2) in zip(walk1,walk2):
        d1,fl1, d2, fl2 = set(d1),set(fl1),set(d2),set(fl2)
        if d1 != d2 or fl1 != fl2:
            return report_and_exit(report,False)
        for f in fl1:
            same,diff,weird = filecmp.cmpfiles(p1,p2,fl1,shallow=False)
            if diff or weird:
                return report_and_exit(report,False)

    return report_and_exit(report,True)


path_git=r'F:\work\svn2git\svn2git\test_data\GIT'
path_svn=r'F:\work\svn2git\svn2git\test_data\SVN'
dirs_same_enough(path_git,path_svn,report=True)