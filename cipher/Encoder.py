clear="This is a text"

def encode(text,a,b,c):
    res = []
    for i in range(len(text)):
        if i%3 == 0:
            res.append(ord(text[i])+a%256)
        elif i%3 == 1:
            res.append(ord(text[i])+b%256)
        elif i%3 == 2:
            res.append(ord(text[i])+c%256)
    return res


cypher = encode(clear,10,11,12)
print(" ".join(str(x) for x in cypher))