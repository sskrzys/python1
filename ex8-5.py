fhand = open('mbox-short.txt')
counter = 0
for line in fhand:
    buf = line.split()
    if len(buf) is 0:
        continue
    if buf[0] == 'From':
        print(buf[1])
        counter += 1
print('There are -- %d %s %s -- froms' % (counter, counter, counter))