import sys

# sys.setrecursionlimit(2500)

def nikita(arg_array):
    len_array = len(arg_array)
    if len_array == 0 or len_array == 1:
        return 0
    sum_array = sum(arg_array)
    if sum_array%2 == 1:
        return 0
    if sum_array == 0:
        return len_array-1
    acc = 0
    for i in range(len_array):
        acc += arg_array[i]
        if acc == sum_array//2:
            return 1 + max(nikita(arg_array[:i + 1]), nikita(arg_array[i + 1:]))
    return 0

t = int(input())
for test in range(0,t):
    arraySize = int(input())
    array = list(map(int, input().split()))
    print(nikita(array))

