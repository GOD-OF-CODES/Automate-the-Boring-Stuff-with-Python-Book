import bs4 , requests
res=requests.get('https://nostarch.com')
res.raise_for_status()
nostarchsoup= bs4.BeautifulSoup(res.text,'html.parser')
type(nostarchsoup)