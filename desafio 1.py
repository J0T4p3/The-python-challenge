alphabet = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = ('g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj')
for x in range(len(text)):
    if text[x] not in alphabet:
        print(text[x],end='')
    else:
        letter = text[x]
        position = alphabet.index(letter) + 2 #por causa do fator de conversão
        if position >= len(alphabet):
            print(alphabet[position - len(alphabet)], end='')
        else:
            print(alphabet[position], end='')
        

