import bs4
soup=bs4.BeautifulSoup(open('example.html'),'html.parser')
spanelem=soup.select('span')[0]
print(len(spanelem))
print(str(spanelem))
print(spanelem.get('id'))
