def armstrong(num):
    digits= str(num)
    power= len(digits)
    armstrong_sum= sum(int(digit) ** power for digit in digits) 
    return armstrong_sum == num
numb= int(input())
if armstrong(numb):
    print("armstrong")
else:
    print("not armstrong")