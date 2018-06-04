hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
try:
    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        pay = hours * rate
    print('Pay:',pay)
except:
    print('Please enter numbers')