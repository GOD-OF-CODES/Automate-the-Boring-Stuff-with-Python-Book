import random
num= random.randint(1,20)
count=0

print('guess the number i am thinking')
while True:
    num1=input()
    if int(num1)==num :
        count=int(count)+1
        print('the guess was correct congrats. total guesses were '+str(count))
        break
    elif int(num1)<num:
        count=count+1
        print('the guess is too low')  
        continue  
    elif int(num1)>num:
        count=int(count)+1
        print('the guess is too high')    
        continue
