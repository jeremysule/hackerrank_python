cypher_text="75 35 14 111 45 206 35 1 17 113 37 20 100 50 23 111 31 22 108 45 16 118 222 8 114 48 194 118 45 14 121 39 16 106 222 22 107 35 194 74 31 15 101 39 22 35 33 10 100 42 14 104 44 9 104 236 194 83 42 7 100 49 7 35 49 7 113 34 194 124 45 23 117 222 21 114 42 23 119 39 17 113 222 3 113 34 194 70 20 194 119 45 194 108 33 3 113 33 17 103 35 226 106 31 15 101 39 22 117 35 21 104 31 20 102 38 208 102 45 15 35 47 23 114 50 11 113 37 194 117 35 8 104 48 7 113 33 7 61 222 214 105 244 6 100 241 215 101 240 6 49"
# cypher_text="94 115 117 125 43 117 125 43 109 42 127 113 130 127"
cypher=list(map(int,cypher_text.split(' ')))

shiftedByA = cypher[0::3]
shiftedByB = cypher[1::3]
shiftedByC = cypher[2::3]

# for i in range(0,len(cypher)-3):
#     if cypher[i+3] - cypher[i] == 63:
#         print(i)
#         print(cypher[i])

# assert max(shiftedByA) - min(shiftedByA) <= 127 - 32
# assert max(shiftedByB) - min(shiftedByB) <= 127 - 32
# assert max(shiftedByC) - min(shiftedByC) <= 127 - 32

# RangeLimForA = max(abs(max(shiftedByA)-127), abs(min(shiftedByA)-32))
# minA = min(shiftedByA)
# maxA = max(shiftedByA)
# RangeLimForB = max(abs(max(shiftedByB)-127), abs(min(shiftedByB)-32))
# minB = min(shiftedByB)
# maxB = max(shiftedByB)
# RangeLimForC = max(abs(max(shiftedByC)-127), abs(min(shiftedByC)-32))
# minC = min(shiftedByC)
# maxC = max(shiftedByC)
# for d in cypher_list:
#     print(d)
list = [ (a,b,c) for a in range(256) for b in range(256) for c in range(256) ]
for (a, b, c) in list:
    # if not 32 <= (cypher[0]-a%256) < 127:
    #     continue
    # if not 32 <= (cypher[1]-b%256) < 127:
    #     continue
    # if not 32 <= (cypher[2]-c%256) < 127:
    #     continue

    candidateText = ""
    for i in range(len(cypher)):
        if i%3 == 0:
            candidateText += chr( (cypher[i]-a) % 256 )
        elif i%3 == 1:
            candidateText += chr( (cypher[i]-b) % 256 )
        elif i%3 == 2:
            candidateText += chr( (cypher[i]-c) % 256 )
        # print(candidateText)
    if "Hello" in  candidateText:
        print(candidateText)