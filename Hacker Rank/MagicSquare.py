def compute_row_sum(arr):
    return sum(arr[0]), sum(arr[1]), sum(arr[2])

def compute_column_sum(arr):
    return sum([row[0] for row in arr]), sum([row[1] for row in arr]), sum([row[2] for row in arr])

def compute_diagonal_sum(arr):
    return arr[0][0] + arr[1][1] + arr[2][2], arr[0][2] + arr[1][1] + arr[2][0]

def compute_matrix(array):
    magic_const = 15
    cost = 0
    prev_value = 0
    for i, row in enumerate(array):
        for j, column in enumerate(row):
            row1, row2, row3 = compute_row_sum(array)
            main_diag, reverse_diag = compute_diagonal_sum(array)

            col1, col2, col3 = compute_column_sum(array)
            main_diag, reverse_diag = compute_diagonal_sum(array)

            print('here', i,j)
            # print(main_diag == magic_const and i == 0 and j == 0) 
            # print(main_diag == magic_const and i == 1 and j == 1) 
            # print(main_diag == magic_const and i == 2 and j == 2) 
            # print(reverse_diag == magic_const and i == 0 and j == 2) 
            # print(reverse_diag == magic_const and i == 1 and j == 1) 
            # print(reverse_diag == magic_const and i == 2 and j == 0)
            print((i == 0 or j == 0) and (row1 == magic_const or col1 == magic_const), row1, col1) 
            print((i == 1 or j == 1) and (row2 == magic_const or col2 == magic_const), row2, col2) 
            print((i == 2 or j == 2) and (row3 == magic_const or col3 == magic_const), row3, col3)

            if row1 != magic_const and (col1 != magic_const or col2 != magic_const or col3 != magic_const):
                if ((main_diag == magic_const and i == 0 and j == 0) 
                or (main_diag == magic_const and i == 1 and j == 1) 
                or (main_diag == magic_const and i == 2 and j == 2) 
                or (reverse_diag == magic_const and i == 0 and j == 2) 
                or (reverse_diag == magic_const and i == 1 and j == 1) 
                or (reverse_diag == magic_const and i == 2 and j == 0)) or (((i == 0 or j == 0) and (row1 == magic_const and col1 == magic_const)) 
                or ((i == 1 or j == 1) and (row2 == magic_const and col2 == magic_const)) 
                or ((i == 2 or j == 2) and (row3 == magic_const and col3 == magic_const))):
                    continue
                else:                    
                    value = row1 if row1 != magic_const else col1
                    # print('first if', i, j, row1, col1, main_diag, reverse_diag, value)
                    prev_value = array[i][j]
                    array[i][j] += (magic_const - value)
                    cost += abs(array[i][j] - prev_value)
                    # print(array)
                    break
            elif row2 != magic_const and (col1 != magic_const or col2 != magic_const or col3 != magic_const):
                if ((main_diag == magic_const and i == 0 and j == 0) 
                or (main_diag == magic_const and i == 1 and j == 1) 
                or (main_diag == magic_const and i == 2 and j == 2) 
                or (reverse_diag == magic_const and i == 0 and j == 2) 
                or (reverse_diag == magic_const and i == 1 and j == 1) 
                or (reverse_diag == magic_const and i == 2 and j == 0)) or (((i == 0 or j == 0) and (row1 == magic_const and col1 == magic_const)) 
                or ((i == 1 or j == 1) and (row2 == magic_const and col2 == magic_const)) 
                or ((i == 2 or j == 2) and (row3 == magic_const and col3 == magic_const))):
                    continue
                else:
                    value = row2 if row2 != magic_const else col2
                    # print('first elif', i, j, row2, col2, main_diag, reverse_diag, value)
                    prev_value = array[i][j]
                    array[i][j] += (magic_const - value)
                    cost += abs(array[i][j] - prev_value)
                    # print(array)
                    break
            elif row3 != magic_const and (col1 != magic_const or col2 != magic_const or col3 != magic_const):
                if ((main_diag == magic_const and i == 0 and j == 0) 
                or (main_diag == magic_const and i == 1 and j == 1) 
                or (main_diag == magic_const and i == 2 and j == 2) 
                or (reverse_diag == magic_const and i == 0 and j == 2) 
                or (reverse_diag == magic_const and i == 1 and j == 1) 
                or (reverse_diag == magic_const and i == 2 and j == 0)) or (((i == 0 or j == 0) and (row1 == magic_const and col1 == magic_const)) 
                or ((i == 1 or j == 1) and (row2 == magic_const and col2 == magic_const)) 
                or ((i == 2 or j == 2) and (row3 == magic_const and col3 == magic_const))):
                    continue
                else:
                    value = row3 if row3 != magic_const else col3
                    # print('first if', i, j, row3, col3, main_diag, reverse_diag, value)                    
                    prev_value = array[i][j]
                    array[i][j] += (magic_const - value)
                    cost += abs(array[i][j] - prev_value)
                    # print(array)
                    break
            else:
                print('whats wrong',row1, row2, row3, col1, col2, col3, main_diag, reverse_diag)
                cost = 0
    print('final', array, 'cost', cost)
    return cost

def compute_matrix2(s):
    n = [s[i][j] for i in range(3) for j in range(3)]
    all_n = [
            [8, 1, 6, 3, 5, 7, 4, 9, 2],
            [6, 1, 8, 7, 5, 3, 2, 9, 4],
            [4, 9, 2, 3, 5, 7, 8, 1, 6],
            [2, 9, 4, 7, 5, 3, 6, 1, 8],
            [8, 3, 4, 1, 5, 9, 6, 7, 2],
            [4, 3, 8, 9, 5, 1, 2, 7, 6],
            [6, 7, 2, 1, 5, 9, 8, 3, 4],
            [2, 7, 6, 9, 5, 1, 4, 3, 8]
        ]
 
    allsum = []
    for l in all_n:
        allsum.append(sum([abs(n[i]-l[i]) for i in range(9)]))
    
    print(min(allsum))

# array = [[5,3,4], [1,5,8], [6,4,2]]
# array = [[4,9,2],[3,5,7],[8,1,5]]
# array = [[4,8,2],[4,5,7],[6,1,6]]
array = [[4,5,8],[2,4,1],[1,9,7]]
# compute_matrix(array)
compute_matrix2(array)
# print(row1, col1)
# print(row2, col2)
# print(row3, col3)
# print(main_diag, reverse_diag)

# a = 1
# b = 1
# c= 1
# if (a, b, c) != (1, 1, 1):
#     print('worked')
# else:
#     print('something')