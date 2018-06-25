filename = input("Enter filename: ")
try:
    fhand = open(filename)
    count = 0
    for line in fhand:
        count += 1
    print("Lines in file: ", count)
except:
    if filename == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print("File cannot be opened or is not present")
    exit()