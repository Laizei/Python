# selenium 8comic 漫畫爬蟲

## 使用套件
![image alt](https://i.imgur.com/TgLmDHk.jpg)

安裝套件指令

> pip install beautifulsoup

[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

> pip install selenium

[selenium 指令 用法](https://pypi.org/project/selenium/)

 

## 爬蟲方式
使用 selenium 瀏覽器，去模仿使用者瀏覽網頁的特性，來爬取要的資料。
8comci網站的漫畫網頁是透過ajax夾帶資訊過來，動態網頁就不能使用 request 來爬取。

分析網頁json檔裡面只有放圖片網址的檔名公式，由這邊可知道檔名是以隨機的公式產生所以，無法準確的抓到所需的圖片檔名參數，才使用 selenium 套件來爬取。

但通常用 selenium 往往都是最逼不得已的情況下使用，因為 selenium 執行速度很慢，對於要大量爬取資料時，都不會是最佳首選。