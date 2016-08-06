def map_occurences(word):
    occurrence_map = {}
    for l in word:
        if l not in occurrence_map:
            occurrence_map[l] = 1
        else:
            occurrence_map[l] += 1
    return occurrence_map

t = int(input())

for t in range(t):
    concat_string = input()

    len_cword = len(concat_string)
    if len_cword %2 == 1: #cannot split in 2
        print(-1)
        continue

    word1 = map_occurences(concat_string[:len_cword//2])
    word2 = map_occurences(concat_string[len_cword//2:])

    resDiff = 0
    for l in word1.keys():
        if l not in word2.keys():
            resDiff += word1[l]
        else:
            resDiff += max(0,(word1[l]-word2[l]))


    print(resDiff)









# t = int(input())
#
# for t in range(t):
#     concat_string = input()
#
#     len_cword = len(concat_string)
#     if len_cword %2 == 1: #cannot split in 2
#         print(-1)
#         continue
#
#     word1 = sorted(concat_string[:len_cword//2])
#     word2 = sorted(concat_string[len_cword//2:])
#
#     resWord1 = 0
#     for l in word1:
#         if l not in word2:
#             resWord1 += 1
#
#     resWord2 = 0
#     for l in word2:
#         if l not in word1:
#             resWord2 += 1
#
#     print(min(resWord1,resWord2))