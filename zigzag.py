import time , sys
indent =0
indentincrease = True

try:
    while True:
        print(' '*indent, end='')
        print('****')
        time.sleep(0.1)

        if indentincrease==True:
            indent=indent+1
            if indent==10:
                indentincrease=False
        else:
            indent=indent-1
            if indent==0:
                indentincrease=True
except KeyboardInterrupt:
    sys.exit()