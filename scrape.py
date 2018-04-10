#import libraries
import urllib.request
from bs4 import BeautifulSoup

import csv 
from datetime import datetime

#specify the url
quote_page='http://www.bloomberg.com/quote/SPX:IND'

#query the website and return the html to the variable 'page'
page=urllib.request.urlopen(quote_page)

#parse the page into beautiful soup and store it in variable soup
soup=BeautifulSoup(page,'html.parser')

#code to extract data

#Take the div of name and get its value
name_box = soup.find('h1',attrs={'class':'name'})
name = name_box.text.strip() #strip() is used to remove the starting and trailing print name

#get index price
price_box=soup.find('div',attrs={'class':'price'})
price=price_box.text
print (price)

#open a csv file with append, so old data will not be erased
with open('index.csv','a')as csv_file:
 writer=csv.writer(csv_file)
 writer.writerow([name,price,datetime.now()])

