#!python3
#searchpypi.py
import requests , sys , webbrowser, bs4, requests_html

print('searching....')

url= 'https://pypi.org/search/?q=automate'

this_session = requests_html.HTMLSession()
res = this_session.get(url)
res.html.render(sleep=3)

# print(res.html.raw_html)

soup=bs4.BeautifulSoup(res.html.raw_html, "html.parser")
linkelems=soup.select('.package-snippet')
print(len(linkelems))
numopen=min(5,len(linkelems))
for i in range(numopen):
    urltoopen='https://pypi.org'+linkelems[i].get('href')
    print('Opening',urltoopen)
    webbrowser.open(urltoopen)
