import re
pn= re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = pn.search("my number is 415-213-4545")
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
