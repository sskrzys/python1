fhand = open('romeo.txt')
liston = []
for line in fhand:
    buf = line.split()
    for word in buf:
        if word not in liston:
            liston.append(word)
liston.sort()
print(liston)