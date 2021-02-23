import os
import argparse
import logging
import logging.config




if __name__ == '__main__':
    #initiating parser
    myparser = argparse.ArgumentParser(description="To Compare 2 Dirtory recursively")

    #adding argumnets
    myparser.add_argument('-DIR1' , metavar='DIR1',type=str,help=' path of first Directory')
    myparser.add_argument('-DIR2' , metavar='DIR2',type=str,help=' path of second Directory')
    myparser.add_argument('-OUT' , metavar='OUT',type=str,help=' path of Output file')

    arg=myparser.parse_args()

    if not arg.DIR1 or not arg.DIR2 or not arg.OUT:
        myparser.error('Incorrect usage of argument, please check usage.')

    dir1=arg.DIR1
    dir2=arg.DIR2
    out_file=arg.OUT

    logger=logging.getLogger(__name__)
    logging.getLogger().setLevel(logging.DEBUG)

    c_handler=logging.StreamHandler()
    c_handler.setLevel(logging.DEBUG)

    c_format=logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)

    logger.addHandler(c_handler)
    
    logger.info(arg)

    cmd='python compare_v2.py > '+out_file
    os.system(cmd)

    with open(out_file,'rt') as f:
        nf=''
        #lookahead(f)
        for i,line in enumerate(f):
            if line.startswith('Differing') or line.startswith('Only'):
                nf+='line:('+str(i-1)+') :'+last+'\n'
                nf+='-'*20+'\n'
                nf+='difference: '+line+'\n'
                nf+='-'*20+'\n'
                nf+='-'*20+'\n'
            last=line

    with open(out_file,'w') as f:
        f.write(nf)        