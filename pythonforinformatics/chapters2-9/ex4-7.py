def computegrade(score):
    try:
        score = float(score)
        if score > 1:
            print('Enter number from between 0 and 1')
        elif score > 0.9:
            print('A')
        elif score > 0.8:
            print('B')
        elif score > 0.7:
            print('C')
        elif score > 0.6:
            print('D')
        else:
            print('F')
    except:
        print('Bad score')

score = input('Enter score: ')
computegrade(score)