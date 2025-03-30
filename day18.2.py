import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.raise_for_status())
playfile=open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(100000):
    playfile.write(chunk)
playfile.close()