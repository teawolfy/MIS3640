str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
newStr = ""

for letter in str:
    if (ord(letter) in range(65,91) or ord(letter) in range(97,121)):
        letter = chr(ord(letter) + 2)
    elif(letter == 'y' or letter == 'z'):
        letter = chr(ord(letter) -  24)
    newStr += letter

print(newStr)
