import csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from patent_numbers import patent_nos
import patent_numbers
from parsel import Selector

writer = csv.writer(open(patent_numbers.file_name,'w+'))
writer.writerow(['Title','Abstract','Filing_date','Inventors'])#,'Assignee'])


def validate_field(field):
	if field:
		pass
	else:
		field=''
	return field


driver = webdriver.Chrome("/home/pranjal/Desktop//chromedriver_linux64/chromedriver")
for x in patent_nos:


	driver.get("http://patft.uspto.gov/netahtml/PTO/srchnum.htm")
	search = driver.find_element_by_id('qry')
	search.send_keys(x)
	sleep(1)
	search_res = driver.find_element_by_xpath('//input[@type = "submit"]')
	search_res.click()
	sleep(2)
	
	sel = Selector(text=driver.page_source)
	
	title = driver.find_element_by_xpath('//font[@size = "+1"]').text
	sleep(1)
	abstract = driver.find_element_by_xpath('//p').text
	sleep(1)

	base = sel.xpath('.//table//tr//text()').extract()
	sleep(1)
	index = base.index('Filed:\n       ')
	sleep(1)

	filing_date = base[index+2]
	sleep(1)
	#inventors = driver.find_element_by_xpath('//table[3]//td').text
	inventors = driver.find_element_by_xpath('//table[3]/tbody/tr/td').text

	#x = base.index("Assignee:")                   #Make sure these values exist
	#y = base.index('Family ID:\n       ')          # Run an if-else loop for checking existence of assignee index
	#assignee = base[x:y]
	
	title=validate_field(title)
	abstract=validate_field(abstract)
	filing_date=validate_field(filing_date)
	inventors=validate_field(inventors)
	#assignee=validate_field(assignee)


	# name = sel.xpath('//h1/text()').extract_first()
	# if name:
	# 	name = name.strip()
	# job_title = sel.xpath('//h2/text()').extract_first()
	# if job_title:
	# 	job_title = job_title.strip()
	# location = sel.xpath('//h3/text()').extract_first()
	# if location:
	# 	location = location.strip()
	# school = sel.xpath('//*[starts-with(@class,"pv-top-card-v2-section__entity-name pv-top-card-v2-section__school-name text-align-left ml2 t-14 t-black t-bold lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first()
	# if school:
	# 	school = school.strip()

	# linkedin_url = driver.current_url


	


	# print('\n')
	# print('Name:' + name)
	# print('Job Title:' + job_title)
	# print('Location:'+location)
	# print('School:'+school)
	# print('URL:'+linkedin_url)
	# print('\n')

	writer.writerow([title,
						abstract,
						filing_date,
						inventors])
						#assignee])












