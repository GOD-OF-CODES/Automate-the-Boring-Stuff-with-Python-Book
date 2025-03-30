import requests , sys , webbrowser, bs4, requests_html

print('searching....')

url= 'https://www.wikipedia.org/wiki/john'

this_session = requests_html.HTMLSession()
res = this_session.get(url)
res.html.render(sleep=3)


soup=bs4.BeautifulSoup(res.html.raw_html, "html.parser")
linkelems=soup.select('a')
print(len(linkelems))
numopen=min(5,len(linkelems))
for i in range(numopen):
    urltoopen='https://en.wikipedia.org/wiki/'+linkelems[i].get('href')
    print('Opening',urltoopen)
    webbrowser.open(urltoopen)