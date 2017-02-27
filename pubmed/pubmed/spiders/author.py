#encoding:utf-8
'''Read Time.ini; Assign url; Execute crawl command; Rewrite Time.ini;
   Extract email-add information; Dereplication; Send email
'''
import linecache
import datetime
import os
file = open('Time.ini','r')
#linecount = len(file.readlines())
#print linecount
linecache.clearcache()
year = linecache.getline('Time.ini',1)
month = linecache.getline('Time.ini',2)
day = linecache.getline('Time.ini',3)
file.close()
#È¥µô»»ÐÐ·û
year = year.strip('\n')
month = month.strip('\n')
day = day.strip('\n')
import scrapy
#from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.selector import Selector
import urlparse 
from pubmed.items import AuthorItem
class AuthorSpider(scrapy.Spider):
	name = "author"
        #allowed_domains = ["http://www.ncbi.nlm.nih.gov/"]
	#download_delay = 1
#	def __init__(self, *args, **kwargs): 
#      		super(AuthorSpider, self).__init__(*args, **kwargs) 
#      		self.start_urls = [kwargs.get('start_url')]
	start_urls = [
"http://www.ncbi.nlm.nih.gov/m/pubmed?term=%28%28China[Affiliation]%29%20AND%20%28%22"+year+"%2F"+month+"%2F"+day+"%22[Date%20-%20Publication]%20%3A%20%223000%22[Date%20-%20Publication]%29%20AND%20Cell%20Biology[MeSH%20Terms]%29",
"http://www.ncbi.nlm.nih.gov/m/pubmed?term=%28%28China[Affiliation]%29%20AND%20%28%22"+year+"%2F"+month+"%2F"+day+"%22[Date%20-%20Publication]%20%3A%20%223000%22[Date%20-%20Publication]%29%20AND%20HapMap%20Project[MeSH%20Terms]%29",
"http://www.ncbi.nlm.nih.gov/m/pubmed?term=%28%28China[Affiliation]%29%20AND%20%28%22"+year+"%2F"+month+"%2F"+day+"%22[Date%20-%20Publication]%20%3A%20%223000%22[Date%20-%20Publication]%29%20AND%20Human%20Genome%20Project[MeSH%20Terms]%29",
"http://www.ncbi.nlm.nih.gov/m/pubmed?term=%28%28China[Affiliation]%29%20AND%20%28%22"+year+"%2F"+month+"%2F"+day+"%22[Date%20-%20Publication]%20%3A%20%223000%22[Date%20-%20Publication]%29%20AND%20Cytogenetics[MeSH%20Terms]%29",
"http://www.ncbi.nlm.nih.gov/m/pubmed?term=%28%28China[Affiliation]%29%20AND%20%28%22"+year+"%2F"+month+"%2F"+day+"%22[Date%20-%20Publication]%20%3A%20%223000%22[Date%20-%20Publication]%29%20AND%20Genetics%20Medical[MeSH%20Terms]%29",
"http://www.ncbi.nlm.nih.gov/m/pubmed?term=%28%28China[Affiliation]%29%20AND%20%28%22"+year+"%2F"+month+"%2F"+day+"%22[Date%20-%20Publication]%20%3A%20%223000%22[Date%20-%20Publication]%29%20AND%20Precision%20Medicine[MeSH%20Terms]%29",
"http://www.ncbi.nlm.nih.gov/m/pubmed?term=%28%28China[Affiliation]%29%20AND%20%28%22"+year+"%2F"+month+"%2F"+day+"%22[Date%20-%20Publication]%20%3A%20%223000%22[Date%20-%20Publication]%29%20AND%20DNA%20Fingerprinting[MeSH%20Terms]%29",
"http://www.ncbi.nlm.nih.gov/m/pubmed?term=%28%28China[Affiliation]%29%20AND%20%28%22"+year+"%2F"+month+"%2F"+day+"%22[Date%20-%20Publication]%20%3A%20%223000%22[Date%20-%20Publication]%29%20AND%20Forensic%20Genetics[MeSH%20Terms]%29",
"http://www.ncbi.nlm.nih.gov/m/pubmed?term=%28%28China[Affiliation]%29%20AND%20%28%22"+year+"%2F"+month+"%2F"+day+"%22[Date%20-%20Publication]%20%3A%20%223000%22[Date%20-%20Publication]%29%20AND%20Paternity[MeSH%20Terms]%29",
"http://www.ncbi.nlm.nih.gov/m/pubmed?term=%28%28China[Affiliation]%29%20AND%20%28%22"+year+"%2F"+month+"%2F"+day+"%22[Date%20-%20Publication]%20%3A%20%223000%22[Date%20-%20Publication]%29%20AND%20Medical%20Oncology[MeSH%20Terms]%29",
"http://www.ncbi.nlm.nih.gov/m/pubmed?term=%28%28China[Affiliation]%29%20AND%20%28%22"+year+"%2F"+month+"%2F"+day+"%22[Date%20-%20Publication]%20%3A%20%223000%22[Date%20-%20Publication]%29%20AND%20Pathology[MeSH%20Terms]%29",
"http://www.ncbi.nlm.nih.gov/m/pubmed?term=%28%28China[Affiliation]%29%20AND%20%28%22"+year+"%2F"+month+"%2F"+day+"%22[Date%20-%20Publication]%20%3A%20%223000%22[Date%20-%20Publication]%29%20AND%20Translational%20Medical%20Research[MeSH%20Terms]%29"	
	]
	#rules = [
	#	Rule(SgmlLinkExtractor(allow=('www.ncbi.nlm.nih.gov'+'/pubmed/26984562',)),callback='parse_author_information',follow=True)
	#]
	def parse(self,response):	
		for href in response.xpath('//div[@class="d"]/ul/li/a/@href'):
			url = response.urljoin(href.extract())
			yield scrapy.Request(url,callback=self.parse_author_information)#dont_filter=True)
		next_pages = response.xpath('//div[@class="pag"]/a[@rel="next"]/@href').extract()
		if next_pages:
			next_url =response.urljoin(next_pages[0])
			yield scrapy.Request(next_url,callback=self.parse)#dont_filter=True)

	def parse_author_information(self,response):
		item = AuthorItem()
		item['TitleName'] = response.xpath('//div[@class="a"]/h2/text()').extract()
		item['AuthorsName'] = response.xpath('//div[@class="auths"]/sup/text() | //div[@class="auths"]/a/text()').extract()
		item['AuthorInformation'] = response.xpath('//div[@class="exi"]/ul/li/sup/text() | //div[@class="exi"]/ul/li/text()').extract()
		#item['AuthorsName'] = response.xpath('//div[@class="auths"]/a/text()').extract()
		#item['AuthorInformation'] = response.xpath('//div[@class="exi"]/ul/li/text()').extract()
                #for i in range(len(item['AuthorInformation'])-1):
		        #if i>(len(item['AuthorInformation'])-1):
			#	item['AI'] = { item['AuthorsName'][i]:None}
			#else:
		#	item['AI'] = { item['AuthorsName'][i]:item['AuthorInformation'][i]}
				
		
		item['Citation'] =response.xpath('//div[@id="cit_full"]/p/text()').extract()
		item['Abstract'] = response.xpath('//div[@class="ab"]/p/span/text() | //div[@class="ab"]/p/text()').extract() 
		item['pmid'] = response.xpath('//div[@class="meta"]/div/span/text()').extract()
		item['FullTextLink'] = response.xpath('//div[@class="ids"]/a/@href').extract()
		#tmp1 is item['AuthorInformation'] only authorinformation has no email,request parse_email_information
		#tmp1 = response.xpath('//div[@class="exi"]/ul/li/text()').extract()
		#for i in range(len(tmp1)):
		#	if '@' in tmp1[i]:
		#		continue
		#	else:
		#		nextPage = response.xpath('//div[@class="ids"]/a/@href').extract()
		#		if nextPage:
		#			nextUrl = response.urljoin(nextPage[0])
		#			request = scrapy.Request(nextUrl,callback=self.parse_email_information)
					#request.meta['item'] = item
    		#			yield request
		yield item
	def parse_email_information(self,response):
		#item = AuthorItem()
		#item = response.meta['item']
		item['email']=[]
		#email1 = []
		#email2 = []
		tmp2 = response.xpath('//a/text()').extract()   
		tmp3 = response.xpath('//a/@href').extract()
		for i in range(len(tmp2)):
			if '@' in tmp2[i]:
				if tmp2[i].find('@')>tmp2[i].find('.'):
					tmp2[i]=tmp2[i][::-1]
					#email1.append(tmp2[i])
					item['email'].append(tmp2[i])
					break
				else:
					item['email'].append(tmp2[i])
					break
		#for j in range(len(email1)):
			#item['AuthorInformation'].append(email1[j])
		for i in range(len(tmp3)):
			if '@' in tmp3[i]:
				if tmp3[i].find('@')>tmp3[i].find('.'):
					#tmp3[i]=tmp3[i][::-1]
					email2.append(tmp3[i][7:])
					item['email'].append(tmp3[i][7:])
					break
				else:
					item['email'].append(tmp3[i][7:])
					break
		#for j in range(len(email2)):
			#item['AuthorInformation'].append(email2[j])
		yield item
#i = datetime.datetime.now()
#f = open('Time.ini','rb+')
#f.truncate()
#f.write(str(i.year)+'\n')
#if i.month<10:
#	month = '0' + str(i.month)
#	print month
#else:
#	month = str(i.month)
#f.write(month+'\n')
#if i.day<10:
#	day = '0' + str(i.day)
#else:
#	day = str(i.day)
#f.write(day+'\n')
#f.close()
