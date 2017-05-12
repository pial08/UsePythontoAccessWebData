# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

"""import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_195381.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
print len(tags)
for tag in tags:
    # Look at the parts of a tag
    #print 'pial'
    sum += int(tag.contents[0])
    #print 'Contents:',tag.contents[0]
print sum
"""



# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Rai.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
#for tag in tags:
#    print tag.get('href', None)

for i in range(7):
    url = tags[17].get('href', None)
    print url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')



















