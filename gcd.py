def divisor(s,r):
    c=0
    for i in range(1,s+1):
        if s%i==0 and r%i==0:
            c=i
    return c
num=int(input())
num2=int(input())
print("greatest divisor= ",divisor(num,num2))
