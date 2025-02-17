import sys
print("Enter the english sentence to covert to pig latin")
sentence=input()
vowels=('a','e','i','o','u')
piglatin=[]
sec=''
for word in sentence.split(' '):
    if(word[0] in vowels):
        print (word+"yay")
    else:
        for i in range(0,len(word)):
            if(word[i] not in vowels):
                sec=sec+word[i]
            else:
                word=word[i:]+sec+'ay'
                break
        print(word)
        sec=''