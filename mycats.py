import sys
mycats= ['som', 'raj', 'yash', 'aryan']
print('guess my cats name or enter stop to exit')
while True:
    name = input()
    if name in mycats:
        print('you guessed it right')
    elif name=='stop':
        sys.exit()
    else:
        print('incorrect')
        continue