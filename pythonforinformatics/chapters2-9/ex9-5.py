fhand = open('pythonforinformatics/mbox.txt')
days = dict()
for line in fhand:
    buf = line.split()
    if len(buf) is 0:
        continue
    if buf[0] == 'From':
        searchfordomain = str(buf).split('@')
        key = searchfordomain[1].split(' ')[0]
        if key not in days:
            days[key] = 1
        else:
            days[key] += 1
print(days)