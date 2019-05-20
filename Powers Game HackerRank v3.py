def powersGame(n):
    for _ in range(n): # int(input())
        return 'First' if n%8 else 'Second' # int(input())
        # print('First' if n%8 else 'Second') # int(input())

# print(powersGame(16))

print(-2**1 % 17)
print(2**1 % 17)

# if __name__ == '__main__':
#     fptr = open('./otheroutput.txt', 'w')

#     t =  3 # int(input())
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