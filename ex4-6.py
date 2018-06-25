def computepay(hours,rate):
    try:
        hours = float(hours)
        rate = float(rate)
        if hours > 40:
            pay = (40 * rate) + ((hours - 40) * rate * 1.5)
        else:
            pay = hours * rate
        print('Pay:',pay)
    except:
        print('Please enter numbers')


hours = input('Enter hours: ')
rate = input('Enter rate: ')

computepay(hours,rate)