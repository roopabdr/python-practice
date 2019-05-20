from itertools import product

def powersGame(n):
    exponents = []
    total = 0

    if n>=1 and n<= 10**6:
        for i in range(1, n+1):
            exponents.append(2**i)

    inputs = product(['+', '-'], repeat=n)

    for items in inputs:
        for item, exponent in zip(list(items), exponents):
            if item == '+':
                total += exponent
            else:
                total -= exponent
        if (total%17 != 0):
            total = 0
            return 'First'
        else:
            total = 0
            return 'Second'

print(powersGame(8))

# if __name__ == '__main__':
#     fptr = open('./otheroutput.txt', 'w')

#     t =  22 # int(input())
#     file_data = []
#     with open('./otherinput.txt') as f:
#         for line in f:
#             file_data.append(line.strip())
    
#     # print(file_data)

#     for t_itr in range(t):
#         n = int(input())

#         result = powersGame(n)

#         fptr.write(result + '\n')

#     fptr.close()
#     print('Done')