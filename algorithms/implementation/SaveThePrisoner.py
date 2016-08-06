from itertools import cycle

t = int(input())

for t in range(t):



    N,M,S = map(int,input().split())
    left = M % N
    limit = N - S +1

    if M == 1:
        print(S)
    elif left == 0:
        if S != 1:
            print(S-1)
        else :
            print(N)
    elif 1 <= left <= limit:
        print( S + left -1)
    else:
        print (left - limit)



    # orderedPrisoners =  list(range(S,N+1)) + list(range(1,S))
    #
    # for p in cycle(orderedPrisoners):
    #     if M == 1:
    #         print(p)
    #         break
    #     else:
    #         M -= 1

