import camelot

# read pdf      
tables = camelot.read_pdf('C://jupyter notebook//17taitung.pdf', pages = '1', flavor = 'stream')

# 表格
print(tables) # list n=1
print(tables[0]) # 抓取表格(行，列)
#print(tables[0].data)
#print(tables[0].df)
tables[0].to_csv('test.csv') # 轉成 csv檔