fhand = open('mbox.txt')
days = dict()
maxvalue = 0
maxkey = ''
for line in fhand:
    buf = line.split()
    if len(buf) is 0:
        continue
    if buf[0] == 'From':
        if buf[1] not in days:
            days[buf[1]] = 1
        else:
            days[buf[1]] += 1
print(max(days.keys()), max(days.values()))