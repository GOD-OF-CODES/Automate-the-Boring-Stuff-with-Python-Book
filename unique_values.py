num= []
while True:
    number=input()
    if(number=='q'):
        break
    else:
        num.append(int(number))
print("the unique numbers are")
for x in range(len(num)):
    check=True
    for y in range(len(num)):
        if(num[x]==num[y] and x!=y):
            check=False
            break
    if(check==True):
        print(num[x])
