def truthTable(n):
    expressions = []
    # if n>=1 and n<= 10**6:
    #     for i in range(1, n+1):
    #         print(2**i)
    
    mid = (2**n+1)//2
    for item in range(1, 2**n+1):
        if item <= mid:
            expressions.append([1])
        else:
            expressions.append([0])
    
    for j in range(n-1):
        mid = mid // 2
        # print(mid)
        expressions = repeat(n, mid, expressions)
        # repeat(n, mid, expressions)
        # print('now..', len(expressions))
    
    print('final', expressions)

def repeat(n, mid, expressions):
    # counter = 1
    # print('repeat', len(expressions))
    for index, item in enumerate(expressions):
        # print(abs((index//mid)%2), item)
        val = abs((index//mid)%2)
        if val == 0:
            item.append(1)
        else:
            item.append(0)
    return expressions

truthTable(3)



# working section
# array = [[1],[1],[1],[1],[1],[1],[1],[1],[0],[0],[0],[0],[0],[0],[0],[0]]
# mid = 4
# for index, item in enumerate(array):
#     print((index//mid)%2, item)

# print('*************************************************')
# mid/=2
# for index, item in enumerate(array):
#     print((index//mid)%2, item)

# print('################################################################')
# mid/=2
# for index, item in enumerate(array):
#     print((index//mid)%2, item)