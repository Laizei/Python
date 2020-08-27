from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
# selenium

url = 'https://comicbus.live/online/a-13530.html?ch=1'

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
#print('https:' + soup.select_one('#TheImg').get('src'))

pagenum = int(soup.select_one('#pagenum').text.split('/')[1].strip('頁'))
pageurl = 'https://comicbus.live/online/a-13530.html?ch=1-{}'

for i in range(pagenum):
    print(pageurl.format(i+1))
    driver.get(pageurl.format(i+1))
    soup = BeautifulSoup(driver.page_source, 'lxml')
    imgurl = ('https:' + soup.select_one('#TheImg').get('src'))
    urllib.request.urlretrieve(imgurl, '{}.jpg'.format(i+1))

driver.close()