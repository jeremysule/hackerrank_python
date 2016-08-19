m,r,s=map(int,input().split())
inputArray=map(int, input().split())
sums={0:{0:1}} #sum->items->numbers  ##possibleSums -> length -> count?
sumA = (r + s) // 2
sumB = (r - s) // 2
for x in inputArray:
    for sum in reversed(sorted(sums.keys())):
        if x+sum> sumA: #new Sum, useless to check if above what we need
            continue
        lengthsForSum=sums[sum] #items->numbers ## lengthForSum -> count
        for lengthForSum in lengthsForSum:
            count=lengthsForSum[lengthForSum]
            newSumAndLengths=sums.setdefault(x + sum, {})
            newSumAndLengths.setdefault(lengthForSum + 1, 0)
            newSumAndLengths[lengthForSum + 1]+=count

res=0
lengthsForSum=sums.setdefault(sumA, {})
for length in lengthsForSum: #iterate over all length for which there is a sum of sumA
    res+= lengthsForSum[length] * sums.setdefault(sumB, {}).setdefault(length, 0)
print(0 if r+s==0 else res%(10**9+7))
