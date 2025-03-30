from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
linkelem= browser.find_element(by='link text',value="Read Online for Free")
linkelem.click()