import string
fhand = open('mbox-short.txt')
days = dict()
maxvalue = 0
maxkey = ''
for line in fhand:
    if len(line) > 1:
        for x in line:
            if str(x) is string.punctuation or x is string.punctuation:
                continue
            else:
                if x.lower() not in days:
                    days[x.lower()] = 1
                else:
                    days[x.lower()] += 1
print(days)