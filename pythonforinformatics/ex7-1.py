filename = 'mbox-short.txt'
fhand = open(filename)
for line in fhand:
    print(line.upper().strip())