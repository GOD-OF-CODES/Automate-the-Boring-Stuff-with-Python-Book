def spam(divideby):
    try:
        print(10/divideby)
    except ZeroDivisionError:
        print('Error: invalid arguement')
print(spam(int((input()))))

    
    
    