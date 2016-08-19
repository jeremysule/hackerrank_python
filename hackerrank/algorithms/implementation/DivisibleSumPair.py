from itertools import combinations

n, k = map(int, input().split())
my_array = list(map(int, input().split()))


# print(len(list(filter( lambda ab: ab[0] + ab[1] % k == 0, combinations(my_array,2)))))



count = 0
for (a,b) in combinations(my_array,2):
    if (a + b) % k == 0:
        count += 1

print(count)

# import sys
#
#
# n,k = input().strip().split(' ')
# n,k = [int(n),int(k)]
# a = [int(a_temp) for a_temp in input().strip().split(' ')]