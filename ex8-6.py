zbieracz = []
while True:
    try:
        dude = input('Enter a number: ')
        zbieracz.append(int(dude))
    except:
        if dude == 'done':
            break
        print('I have asked for number, or just print done do finish')
try:
    print("Max is", max(zbieracz))
    print("Min is", min(zbieracz))
except:
    print('No numbers were entered')