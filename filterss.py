numbers= [1,2,3,4,5,6,7,8,9,10]

def even(n):
    if n%2==0:
        return True
    
even_numbers= filter(even,numbers)
print(even_numbers)
even_numbers_list= list(even_numbers)
print(even_numbers_list)