income= int(input())
per= int(input())
if income<200000:
    if per>60:
        print('eligible')
    else:
        print('percentage should be more than 60')
else:
    print('family income should be less than 2 lakh')