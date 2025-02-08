age=int(input())
cit= input()
if age>=18:
    if cit=="indian":
        print('you are eligible to vote')
    else:
        print('you must be a citizen of india')
else:
    print('you are not eligible to vote')