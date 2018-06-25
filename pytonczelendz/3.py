but = "I"
print(but.isupper())

def wypiszanko():
    fhand = open("mess3").readlines()
    count = 0
    sec_count = 0
    smallo = 0
    buforliter = ""
    result = ""
    longstring = ""
    for line in fhand:
        line.strip()
        print(repr(line.strip()))
        longstring += line.strip()
    for line in longstring:
        line.strip()
        for letter in line:
            try:
                if letter.isupper() and smallo == 0:
                    count += 1
                    if count == 3:
                        smallo = 1
                elif letter.islower() and smallo == 1:
                    buforliter = letter
                    smallo += 1
                elif letter.isupper() and smallo == 2:
                    sec_count += 1
                    if sec_count == 3:
                        smallo += 1
                elif letter.islower() and smallo == 3:
                    result += buforliter
                    count = 0
                    smallo = 0
                    sec_count = 0
                else:
                    count = 0
                    smallo = 0
                    sec_count = 0
            except:
                raise hell
    print(result)

wypiszanko()