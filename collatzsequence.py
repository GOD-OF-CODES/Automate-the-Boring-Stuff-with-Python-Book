import sys 
num= int(input())
while True:
    if num%2==0:
        num=int(num/2)
        print(num)
    else:
        num= 3*num+1
        print(num)
    if num==1:
        sys.exit()

