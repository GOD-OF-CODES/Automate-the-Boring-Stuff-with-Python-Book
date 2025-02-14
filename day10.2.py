#fantasy inventory
import sys
inventory={}
while True:
    print("Enter the unique inventory item or type stop to end")
    key=input()
    if(key=='stop'):
        break
    value=int(input("Enter the number of items of this type"))
    inventory[key]=value
print("Inventory: ")
for i,j in inventory.items():
    print(str(i)+" = "+str(j))
        