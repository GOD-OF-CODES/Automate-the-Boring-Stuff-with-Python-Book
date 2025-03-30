#!python3
#searchpypi.py
import requests , sys , webbrowser, bs4 
print('searching....')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

res= requests.get('https://google.co.in/search?q='+' '.join(sys.argv[1:]), headers=headers, allow_redirects=True)
res.raise_for_status()
print(res.text)
soup=bs4.BeautifulSoup(res.text,'html.parser')
linkelems=soup.select('.package-snippet')
print(len(linkelems))
numopen=min(5,len(linkelems))
for i in range(numopen):
    urltoopen=''+linkelems[i].get('href')
    print('Opening',urltoopen)
    webbrowser.open(urltoopen)