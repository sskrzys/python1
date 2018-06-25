filename = input("Enter filename: ")
fhand = open(filename)
spamcount = 0
sum = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        findpos1 = line.find(':')
        flot = float(line[findpos1 + 1:])
        sum += flot
        spamcount += 1
avg = sum / spamcount
print('Average spam confidence: ', avg)
