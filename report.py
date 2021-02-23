
with open('output.log','rt') as f:
    #lookahead(f)
    for i,line in enumerate(f):
        if line.startswith('Differing') or line.startswith('Only'):
            print('line:('+str(i-1)+') :'+last,end='')
            print('-'*20)
            print('difference: '+line,end='')
            print('-'*20)
            print('-'*20)
        last=line