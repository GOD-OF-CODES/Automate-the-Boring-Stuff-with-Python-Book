#using nested dictionaries 
allGuests={'Alice':{'apple':2 , 'pineapples':12},
           'Bob':{'mangoes':5,'apples':3}}
def countt(guest,item):
    total=0
    for k,v in allGuests.items():
        total= total+v.get(item,0)
    return total
print("Apples: "+str(countt(allGuests,'apples')))
print("Pineapples: "+str(countt(allGuests,'pineapples')))
print("mangoes: "+str(countt(allGuests,'mangoes')))
print("cakes: "+str(countt(allGuests,'cakes')))
