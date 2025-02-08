m=2
for i in range(0,6):
    
    for j in range(5,i,-1):
        print("", end=" ")
    
    for h in range(1,m):
        print('*', end="")
    print()
    m=m+2