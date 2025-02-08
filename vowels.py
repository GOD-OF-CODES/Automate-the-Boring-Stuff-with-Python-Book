def count_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count= count+1
    return count
m= input()
print(count_vowels(m))