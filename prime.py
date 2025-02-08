def prime(a):
    count=0
    for i in range(1,a):
        if(a%i==0):
            count=count+1
        else:
            continue
    return count
b=int(input())
c=prime(b)
if c==1:
    print("Number is prime")
else:
    print('number is not prime')