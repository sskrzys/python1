sum = 0
count = 0
max = 0
min = 0
while True:
    try:
        dude = input('Enter a number: ')
        bufer = int(dude)
        if bufer > max:
            max = bufer
        if bufer < min or count == 0:
            min = bufer
        count += 1
    except:
        if dude == 'done':
            break
        print('I have asked for number, or just print done do finish')
try:
    print("Max is", max)
    print("Min is", min)
except:
    print('No numbers were entered')
