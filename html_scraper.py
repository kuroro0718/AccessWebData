# Scraping Numbers from HTML document
import urllib
import re
from bs4 import BeautifulSoup

url = 'http://python-data.dr-chuck.net/comments_255932.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

total = 0
count = 0
tags = soup('span')
for tag in tags:
  number = re.findall('[0-9]+', str(tag))
  total += int(number[0])
  count += 1

print 'Count:', count  
print 'Sum:', total