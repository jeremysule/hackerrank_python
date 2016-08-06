import itertools
from collections import defaultdict

#https://www.hackerrank.com/challenges/wet-shark-and-two-subsequences


MOD = 10**9+7

(m, r, s) = map(int, input().split())
myArray = map(int, input().split())
sumForAs = (r+s)//2
sumForBs = (r-s)//2
#inspired from leaderBoards

sumsToLenthsCount = {0: {0:1}} #sum -> length -> count

for x in myArray:
    if x > sumForAs:
        continue
    #extract key values for sum, sort them by decreasing order
    possibleSums = reversed(sorted(sumsToLenthsCount.keys()))
    for currentSum in possibleSums:
        newSum = currentSum + x
        if newSum > sumForAs:
            continue
        currentLengthsToCount = sumsToLenthsCount[currentSum] # key exist
        for currentLength in currentLengthsToCount.keys():
            currentCount = currentLengthsToCount[currentLength] #count without new X, new Length, etc.
            newLengthToCountForSum = sumsToLenthsCount.setdefault(newSum,{})
            newLengthToCountForSum.setdefault(currentLength+1,0) #init if not exist
            newLengthToCountForSum[currentLength+1] += currentCount

res = 0
for l in sumsToLenthsCount.setdefault(sumForAs,{}).keys():
    res += (sumsToLenthsCount[sumForAs][l] * sumsToLenthsCount.setdefault(sumForBs,{}).setdefault(l,0)) %MOD
    res %= MOD
print(0 if sumForAs==0 else res)





#
# sumForAs = (r+s)//2
# sumForBs = (r-s)//2
# (possibleAs, possibleBs) = ({},{});
# totalPossibleComb = 0
# # (possibleAs, possibleBs) = ([],[]);
#
# for n in range(len(myArray)+1):
#     # print(n)
#     possibleAs[n]=0
#     possibleBs[n]=0
#     for subSeq in itertools.combinations(myArray, n):
#         mySum = sum(subSeq)
#         if mySum==sumForAs:
#             possibleAs[n] += 1
#         elif mySum==sumForBs:
#             possibleBs[n] += 1
#     totalPossibleComb += ( possibleAs[n]%MOD * possibleBs[n]%MOD ) %MOD
#     # print("Total possible until {0} is {1}".format(n,totalPossibleComb))
#     # totalPossibleComb = totalPossibleComb % MOD
#
#
# print(totalPossibleComb)
#
# # for i in range(len(myArray)+1):
# #     for j in range(i+1):
# #         subSeq = myArray[j:i]
# #         mySum = sum(subSeq)
# #         if mySum==sumForAs:
# #             possibleAs.append(subSeq)
# #         elif mySum==sumForBs:
# #             possibleBs.append(subSeq)
# #
# # print((len(possibleAs)%MOD * len(possibleBs)%MOD)%MOD)
#
