import re
frink= """abcdef hij abc abc
84162tgfi ug1qiowf
f9h23r9f91hrewee
974y1f08goq hcdoiqhwdi
fg81eibfwqbfwqoh34082
raj vardhan singh is a good boy
&^%!#(* ^)&!)@(* &^@!())"""
pattern = re.compile(r'raj vardhan singh')
mo= pattern.finditer(frink)
for mos in mo:
    print(mos)