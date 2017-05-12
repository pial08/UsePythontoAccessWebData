import re



with open('text.txt', 'r') as myfile:
    data=myfile.read()

#print data

y = re.findall('\d+', data)
print y

sum = 0
for num in y:
    sum = sum + int(num)
print sum
print len(y)