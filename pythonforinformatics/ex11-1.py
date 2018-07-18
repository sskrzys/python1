import re
given = input('Enter a regular expression: ')
count = 0
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall(given, line)
    if len(x) > 0 : count += 1
print('File had %d lines that matched %s'%(count,given))