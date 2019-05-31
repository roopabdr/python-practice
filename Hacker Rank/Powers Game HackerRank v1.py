def powersGame(n):
    expressions = []
    exponents = []
    if n>=1 and n<= 10**6:
        for i in range(1, n+1):
            exponents.append(2**i)
    
    mid = (2**n+1)//2
    for item in range(1, 2**n+1):
        if item <= mid:
            expressions.append([1])
        else:
            expressions.append([0])
    
    for j in range(n-1):
        mid = mid // 2
        expressions = repeat(n, mid, expressions)

    total = 0
    for items in expressions:
        for item, exponent in zip(items, exponents):
            if item == 1:
                total += exponent
            else:
                total -= exponent
        if (total%17 != 0):
            total = 0
            return 'First'
        else:
            total = 0
            return 'Second'

def repeat(n, mid, expressions):
    for index, item in enumerate(expressions):
        val = abs((index//mid)%2)
        if val == 0:
            item.append(1)
        else:
            item.append(0)
    return expressions

# powersGame(17)

if __name__ == '__main__':
    fptr = open('./otheroutput.txt', 'w')

    t =  22 # int(input())
    file_data = []
    with open('./otherinput.txt') as f:
        for line in f:
            file_data.append(line.strip())
    
    # print(file_data)

    for t_itr in range(t):
        n = int(input())

        result = powersGame(n)

        fptr.write(result + '\n')

    fptr.close()
    print('Done')


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