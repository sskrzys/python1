import re
count = 0
sum = 0
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0 :
        sum += int(x[0])
        count += 1
print(sum/count)