# camelot pdf

安裝方式，使用方法都在
[camelot 官方網站](https://pypi.org/project/camelot-py/)

---
其實這種類似的套件有:
* [pdfplumber](https://github.com/jsvine/pdfplumber)
* [tabula-py](https://pypi.org/project/tabula-py/)
* [pdfminer](https://pypi.org/project/pdfminer/)

---

可能很多人都會認為這個套件用的機會很少。但那大概是因為您的工作碰觸不到需要大量處理公家機關的公文。像是法拍屋房屋公文或是法院判決書這類的正試公文，都會有許多表格，這時就會使用這種套件來幫助自己，做資料整理的時候更加便利。

---


## 使用方法
> 如果要抓取PDF檔裡面的表格資料，如下圖。

![](https://i.imgur.com/bfJyO1z.png)

 
* 首先先 讀取 PDF ， camelot.read_pdf ( 檔案位置,  頁數,  表格解析方式)
* 檔案位置: 絕對位置 or 網路上的檔案位置
* 頁數: 讀取 PDF 第X頁 ( 讀取要的表格在X頁 )
* 解析方式: lattice  or  stream ( 這邊使用 stream ， 把整頁當成表格來解析 )


> 印出解析的結果

![](https://i.imgur.com/VD2ijMW.png)

> 再來就能夠把 抓取的內容印出來 如下圖

![](https://i.imgur.com/0U8LmJa.png)

> 這時就能把 tables[0].df 轉成其他格式檔案 ( html , csv , excel , json 等等)
這邊我就轉成 csv

![](https://i.imgur.com/uRXitFP.png)

> 轉好之後 我們就能夠打開csv檔，這時會遇到一個問題 中文字的部分出現亂碼

![](https://i.imgur.com/Pym6XQw.png)

> excel 預設為 ANSI，可是檔案裡面的中文是以 BIG5，所以格式不符就會出現亂碼
這邊很簡單把CSV檔用記事本開啟，編碼存成  具有BOM的UTF-8

![](https://i.imgur.com/7VNqXE4.png)

> 這樣就成解決檔案出現亂碼的問題，而且開始弄資料處理的部分了。

![](https://i.imgur.com/Xr5Dtaj.png)

---
如果今天有一堆 PDF 檔表格又亂又雜。需要的資料、數據又都在表格裡時，就很需要這種套件來方便我們使用，也能大大縮短整理資料的時間。

這是很簡單的範例，如果有一堆相同的PDF檔，就能夠寫一個自動化腳本，讓 python 去幫我們做事，在把那些資料轉成需要的檔案。