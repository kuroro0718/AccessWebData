import urllib
import re
from bs4 import BeautifulSoup

# This assignment use urllib and BeautifulSoup to find a specific 
# link and retrieve name by using regular expression.

url = 'http://python-data.dr-chuck.net/known_by_Peirce.html'
count = 7
position = 18

while count > 0:
  html = urllib.urlopen(url).read()
  soup = BeautifulSoup(html, "html.parser")

  tags = soup.findAll('a')
  next_link = re.findall('http:.+html', str(tags[position-1]))
  url = str(next_link[0])
  print url

  name = re.findall('_by_([A-Za-z]+)', url)
  count -= 1
  
print str(name[0])  