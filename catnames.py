import sys
catnames=[]
while True:
    print('write name of cat '+str(len(catnames)+1)+' or enter stop to finish')
    catname= input()
    if catname=='stop':
        break
    catnames= catnames + [catname]
print('the cat names are')
for x in range(0,len(catnames)):
    print(catnames[x], sep=',' , end=' ')