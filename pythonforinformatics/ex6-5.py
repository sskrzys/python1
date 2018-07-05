str = 'X-DSPAM-Confidence: 0.8475'
findpos1 = str.find(':')
flot = float(str[findpos1+1:])
print(flot)