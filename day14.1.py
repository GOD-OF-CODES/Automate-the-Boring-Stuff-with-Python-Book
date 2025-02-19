table=[['apples','games','names','trains'],
       ['ramesh','suresh','harish','burrissh'],
       'loooong word','short','tt','issabella',
       'one','two','three','four']
count=[0,0,0,0]
maxi=0
for j in range(len(table[0])):
    if(len(table[0][j])>maxi):
        count[0]=len(table[0][j])
maxi=0

for j in range(len(table[1])):
    if(len(table[1][j])>maxi):
        count[1]=len(table[1][j])

maxi=0

for j in range(len(table[2])):
    if(len(table[2][j])>maxi):
        count[2]=len(table[2][j])
maxi=0

for j in range(len(table[3])):
    if(len(table[3][j])>maxi):
        count[3]=len(table[3][j])
maxi=0

for j in range(len(table[0])): 
    for i in range(len(table)): 
        print(table[i][j].rjust(count[j])) 

