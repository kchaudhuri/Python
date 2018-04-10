enc = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
new = []
for c in enc:
    if(c.isalpha()):
        if(c == 'y'):
            new.append('a')
        else:
            new.append(("{}".format(chr(ord(c)+2))))
    else:
        new.append(c)

##print(new)
    
for c in new:
    print(c),
