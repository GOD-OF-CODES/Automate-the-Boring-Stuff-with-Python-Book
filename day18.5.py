import bs4
examplefile= open('example.html')
examplesource=bs4.BeautifulSoup(examplefile.read(),'html.parser')
elems=examplesource.select('p')
print(len(elems))
print(str(elems[0]))