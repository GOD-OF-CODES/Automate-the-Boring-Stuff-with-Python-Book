from selenium import webdriver
browser= webdriver.Firefox()
browser.get('https://login.metafilter.com')
userelem=browser.find_element(by='id', value='user_name')
userelem.send_keys('Raj Vardhan Singh')
passelem=browser.find_element(by='id',value='user_pass')
passelem.send_keys('123456789')
passelem.submit()