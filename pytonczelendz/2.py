def wytnij():
    fhand = open("mess")
    for line in fhand:
        line.strip()
        for letter in line:
            if ord(letter) > 96 and ord(letter) < 123:
                print(letter)
            else:
                continue

def policz(liczbaznaku):
    count = 0
    fhand = open("mess")
    for line in fhand:
        line.strip()
        for letter in line:
            if ord(letter) == liczbaznaku:
                count += 1
    print(chr(liczbaznaku), " jest ", count, " i to jest znak ", liczbaznaku)

for i in range(97,123):
    policz(i)

wytnij()