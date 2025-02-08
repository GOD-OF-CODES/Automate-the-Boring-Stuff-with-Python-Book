import random

def getanswer(num):
    if(num==1):
        return 'good'
    elif(num==2):
        return 'bad'

r = random.randint(1,2)
fortune= getanswer(r)
print(fortune)
    