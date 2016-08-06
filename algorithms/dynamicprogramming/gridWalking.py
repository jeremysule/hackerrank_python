
def how_many_ways_in_one_d(x, m_steps, lim_dim, arg_memo):
    if m_steps == 0:
        return 0;
    


def how_many_ways(arg_position, m_steps, arg_dimension, arg_memo):






###Very Slow!!!
def how_many_ways(arg_position, m_steps, arg_dimension, arg_memo):
    # key = (tuple(position), m_steps)
    # if key in arg_memo.keys():
    #     return arg_memo[key]

    if m_steps == 0:
        # arg_memo[key] = 1
        return 1

    res = 0
    for i in range(len(arg_position)):
        coord_at_i = arg_position[i]
        lim_at_i = arg_dimension[i]

        #left
        if 0 < coord_at_i-1 <= lim_at_i:
            new_position = arg_position[:]
            new_position[i] = coord_at_i-1
            res += how_many_ways(new_position, m_steps-1, arg_dimension, arg_memo)

        #right
        if 0 < coord_at_i+1 <= lim_at_i:
            new_position = arg_position[:]
            new_position[i] = coord_at_i+1
            res += how_many_ways(new_position, m_steps-1, arg_dimension, arg_memo)
    # arg_memo[key] = res
    return res






t = int(input())


for test in range(0,t):
    memo = {}
    N, M = map(int, input().split(' '))
    position = list(map(int, input().split(' ')))
    dimension = list(map(int, input().split(' ')))
    print(how_many_ways(position,M,dimension,memo))
