sum = 0
count = 0
while True:
    try:
        dude = input('Enter a number: ')
        sum += int(dude)
        count += 1
    except:
        if dude == 'done':
            break
        print('I have asked for number, or just print done do finish')
try:
    print(sum/count)
except:
    print('No numbers were entered')
