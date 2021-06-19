from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import html5lib
import time
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# browser = webdriver.Chrome(chrome_options=options)
src = (['Жилая'])
browser = webdriver.Chrome()
browser.get('https://my.cian.ru/leads/')
elem = browser.find_element_by_class_name('b7635b5199--input--2vxTR')
elem.send_keys('info@anberloga.ru')
elem.send_keys(Keys.ENTER)
time.sleep(1)
try:
    elem = browser.find_element_by_name('password')
    elem.send_keys('Titova19')
    elem.send_keys(Keys.ENTER)
except:
    elem = browser.find_element_by_name('password')
    # elem = browser.find_element_by_class_name('b7635b5199--input-group--lxTKJ')
    elem.send_keys('Titova19')
    elem.send_keys(Keys.ENTER)
time.sleep(2)
requiredHtml = browser.page_source
soup = BeautifulSoup(requiredHtml, 'html.parser')
# button_elem = browser.find_element_by_name('OpenLead')
# button_elem.click()
with open('test.txt', 'w', encoding='UTF-8') as f:
    f.write(soup.prettify())
