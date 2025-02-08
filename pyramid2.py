height= int(input("enter the height of the triangle"))
height2= height
h=height
h1=height
h2=height
m=2
for i in range(1,height,1):
    for j in range(height,i,-1):
        print(" ", end="")
    height2=height2-1
    for h in range(1,m):
        print("*",end="")
    print()
    m=m+2
m=h2
for i in range(1,h,1):
    for j in range(i,h2):
        print(" ", end="")
    h2=h2-1
    for h in range(m,1,-1):
        print("*",end="")
    print()
    m=m+2
