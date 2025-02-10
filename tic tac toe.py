b= {'1':' ','2':' ','3':' ',
    '4':' ','5':' ','6':' ',
    '7':' ','8':' ','9':' '}
count=0
def printBoard(board):
    print(b['1']+'|'+b['2']+'|'+b['3'])
    print("-+-+-")
    print(b['4']+'|'+b['5']+'|'+b['6'])
    print("-+-+-")
    print(b['7']+'|'+b['8']+'|'+b['9'])
turn='X'
for i in range(9):
    printBoard(b)
    print("Turn for "+turn+" .Move on which space?")
    move=input()
    b[move]=turn
    p=turn
    if((b['1'] == b['2'] == b['3'] == p) or 
        (b['4'] == b['5'] == b['6'] == p) or 
        (b['7'] == b['8'] == b['9'] == p) or
        (b['1'] == b['4'] == b['7'] == p) or 
        (b['2'] == b['5'] == b['8'] == p) or 
        (b['3'] == b['6'] == b['9'] == p) or 
        (b['3'] == b['5'] == b['7'] == p) or 
        (b['1'] == b['5'] == b['9'] == p)):
            count=1
            break
    if turn=='X':
        turn='O'
    else:
        turn='X'
printBoard(b)
if(count==0):
     print("Bad Luck. Nobody won the game")
else:
     print(turn+" won the game")

