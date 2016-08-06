# https://www.hackerrank.com/challenges/fibonacci-modified

prev2, prev1, n = map(int, input().split())
res = 0

for i in range(3,n+1):
    res = prev1 * prev1 + prev2
    prev2 = prev1
    prev1 = res

print(res)

#recursive, slow:
#
# def mfib(n):
#     if n==1:
#         return prev2
#     elif n==2:
#         return prev1
#     else:
#         partialRes = mfib(n-1)
#         return partialRes * partialRes +mfib(n-2)
#
# mfib(n)

