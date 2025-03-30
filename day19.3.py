from selenium import webdriver 
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
try:
    # Use either 'card-img-top' or 'cover-thumb', not both
    elem = browser.find_element(by="class name", value="ard-img-top")
    print('Found <%s> element with that class name!' % (elem.tag_name))
except Exception as e:  # It's better to catch specific exceptions
    print('Was not able to find the element:', str(e))