#text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text = "map"
sum = ""
for letter in text:
    if letter == ' ':
        sum += letter
    elif letter == 'y':
        sum += 'a'
    elif letter == 'z':
        sum += 'b'
    else:
        sum += (chr(ord(letter)+2))
sum.strip()
print(sum)

