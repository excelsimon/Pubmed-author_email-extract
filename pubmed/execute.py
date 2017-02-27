import datetime
import os
os.system(r"e: & cd E:\crawl project\extract email\pubmed & scrapy crawl author -o author.json ")
os.system(r"e: & cd E:\crawl project\extract email\pubmed & scrapy crawl authorPair -o authorPair.json")
i = datetime.datetime.now()
f = open('Time.ini','rb+')
f.truncate()
f.write(str(i.year)+'\n')
if i.month<10:
	month = '0' + str(i.month)
	print month
else:
	month = str(i.month)
f.write(month+'\n')
if i.day<10:
	day = '0' + str(i.day)
else:
	day = str(i.day)
f.write(day+'\n')
f.close()

os.system(r"e: & cd E:\crawl project\extract email\pubmed & python extractEmail.py")

