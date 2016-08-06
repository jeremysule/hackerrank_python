prev2 = 0
prev1 = 1
n = int(input())
res = 0

if n == 0:
    res = 0
elif n == 1:
    res = 1
else:
    for i in range(2,n+1):
        res = prev1 + prev2
        prev2 = prev1
        prev1 = res

print(res)