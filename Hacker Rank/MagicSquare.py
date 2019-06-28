def compute_row_sum(arr):
    return sum(arr[0]), sum(arr[1]), sum(arr[2])

def compute_column_sum(arr):
    return sum([row[0] for row in arr]), sum([row[1] for row in arr]), sum([row[2] for row in arr])

def compute_diagonal_sum(arr):
    return arr[0][0] + arr[1][1] + arr[2][2], arr[0][2] + arr[1][1] + arr[2][0]

def compute_matrix(array):
    magic_const = 15  
    for i, row in enumerate(array):
        row1, row2, row3 = compute_row_sum(array)
        main_diag, reverse_diag = compute_diagonal_sum(array)
        
        for j, column in enumerate(row):
            col1, col2, col3 = compute_column_sum(array)
            main_diag, reverse_diag = compute_diagonal_sum(array)

            if row1 != magic_const and (col1 != magic_const or col2 != magic_const or col3 != magic_const):
                if ((main_diag == magic_const and i == 0 and j == 0) 
                or (main_diag == magic_const and i == 1 and j == 1) 
                or (main_diag == magic_const and i == 2 and j == 2) 
                or (reverse_diag == magic_const and i == 0 and j == 2) 
                or (reverse_diag == magic_const and i == 1 and j == 1) 
                or (reverse_diag == magic_const and i == 2 and j == 0)):
                    continue
                else:                    
                    value = row1 if row1 != magic_const else col1
                    print('first if', i, j, value)
                    array[i][j] += (magic_const - value)
                    break
            elif row2 != magic_const and (col1 != magic_const or col2 != magic_const or col3 != magic_const):
                if ((main_diag == magic_const and i == 0 and j == 0) 
                or (main_diag == magic_const and i == 1 and j == 1) 
                or (main_diag == magic_const and i == 2 and j == 2) 
                or (reverse_diag == magic_const and i == 0 and j == 2) 
                or (reverse_diag == magic_const and i == 1 and j == 1) 
                or (reverse_diag == magic_const and i == 2 and j == 0)):
                    continue
                else:
                    value = row2 if row2 != magic_const else col2
                    print('first elif', i, j, row2, col2, main_diag, reverse_diag, value)
                    array[i][j] += (magic_const - value)
                    break
            elif row3 != magic_const and (col1 != magic_const or col2 != magic_const or col3 != magic_const):
                if ((main_diag == magic_const and i == 0 and j == 0) 
                or (main_diag == magic_const and i == 1 and j == 1) 
                or (main_diag == magic_const and i == 2 and j == 2) 
                or (reverse_diag == magic_const and i == 0 and j == 2) 
                or (reverse_diag == magic_const and i == 1 and j == 1) 
                or (reverse_diag == magic_const and i == 2 and j == 0)):
                    continue
                else:
                    value = row3 if row3 != magic_const else col3
                    print('second elif', i, j, value)
                    array[i][j] += (magic_const - value)
                    break
    print(array)

array = [[5,3,4], [1,5,8], [6,4,2]]
compute_matrix(array)
# print(row1, col1)
# print(row2, col2)
# print(row3, col3)
# print(main_diag, reverse_diag)