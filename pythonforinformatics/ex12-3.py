import urllib.request
import re

letters = 0
numbers = 0
count = 0

page = input("Na jaka stronke chcesz?")

fhand = urllib.request.urlopen(page)
for line in fhand:
    if len(line) > 3000:
        print("Line too long > 3000")
        break
    letters += len(re.findall('[A-z]', str(line)))
    numbers += len(re.findall('[0-9]', str(line)))
    count += len(line)
    print(line.decode().strip())
    if count > 3000: break

print("\nliterek jest %d" % letters)
print("cyferek jest %d" % numbers)
print("znakow jest uguem %d" % count)
# Code: http://www.py4e.com/code3/urllib1.py