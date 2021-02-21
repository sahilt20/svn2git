import os
import filecmp

# force content compare instead of os.stat attributes only comparison
filecmp.cmpfiles.__defaults__ = (False,)

def _is_same_helper(dircmp):
    assert not dircmp.funny_files
    if dircmp.left_only or dircmp.right_only or dircmp.diff_files or dircmp.funny_files:
        return False
    for sub_dircmp in dircmp.subdirs.values():
       if not _is_same_helper(sub_dircmp):
           return False
    return True

def is_same(dir1, dir2):
    """
    Recursively compare two directories
    :param dir1: path to first directory 
    :param dir2: path to second directory
    :return: True in case directories are the same, False otherwise
    """
    if not os.path.isdir(dir1) or not os.path.isdir(dir2):
        return False
    dircmp = filecmp.dircmp(dir1, dir2)
    return _is_same_helper(dircmp)


path_git=r'F:\work\svn2git\svn2git\test_data\GIT'
path_svn=r'F:\work\svn2git\svn2git\test_data\SVN'


print(is_same(path_git,path_svn))