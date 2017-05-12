import urllib
import xml.etree.ElementTree as ET





url = 'http://python-data.dr-chuck.net/comments_195378.xml '
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
#print len(lst)
#lst[0].find('count').text
#print lst[1].find('count').text

sum = 0
for elements in lst:
    sum += int(elements.find('count').text)
print sum
