


# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated according to the following rules:



Board =     [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

def valid(a):
    row_value = [set() for _ in range(9)]
    col_value = [set() for _ in range(9)]
    box_value = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            value = a[r][c]

            if value == ".":
                continue

            if value in row_value[r]:
                return False
            row_value[r].add(value)
        #  for Collums now

            if value in col_value[c]:
                return False
            col_value[c].add(value)
            
            box_index = (r // 3) * 3 + (c // 3)
            if value in box_value[box_index]:
                return False
            box_value[box_index].add(value)
    return True
print(valid(Board))