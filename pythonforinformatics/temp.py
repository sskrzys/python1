import re
hand = open('mbox.txt')
#for line in hand:
    #print(line)
for line in hand:
    line = line.rstrip()
    #x = re.findall('ˆX\S*: [0-9.]+', line)
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0 :
        print(x)