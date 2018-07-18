fhand = open('mbox-short.txt')
days = dict()
maxvalue = 0
maxkey = ''
for line in fhand:
    buf = line.split()
    if len(buf) is 0:
        continue
    if buf[0] == 'From':
        bufor = buf[5].split(':')
        if bufor[0] not in days:
            days[bufor[0]] = 1
        else:
            days[bufor[0]] += 1
for x in sorted(days.items()):
    print(x)