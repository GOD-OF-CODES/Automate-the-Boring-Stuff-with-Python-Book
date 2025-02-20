import re
pn= re.compile(r'\d{3}-\d{3}-\d{4}')
mo = pn.findall("my number is 415-213-4545 415-213-4545 415-213-4545")
print(mo)