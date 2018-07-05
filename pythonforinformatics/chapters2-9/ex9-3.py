fhand = open('pythonforinformatics/mbox.txt')
days = dict()
for line in fhand:
    buf = line.split()
    if len(buf) is 0:
        continue
    if buf[0] == 'From':
        key = line.split()[1]
        if key not in days:
            days[key] = 1
        else:
            days[key] += 1
print(days)