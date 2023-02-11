# Process
# First convert the matrix to row echelon form and then mutilply the diagonal elements
def inputMatrix():
    rows = int(input("Enter number of rows of matrix:"))
    cols = int(input("Enter number of columns of matrix:"))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            number = float(input(f"Enter the number for row {i+1} and column {j+1}:"))
            row.append(number)
        matrix.append(row)
    return matrix

def findDeterminant():
    matrix = inputMatrix()
    ans = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == col:
                pe = matrix[row][col]
                ans.append(pe)  # Stores the diagonal elements
                if pe != 0:
                    for r in range(len(matrix[0])):
                        matrix[row][r] = round(matrix[row][r] / pe, 3)
                    for j in range(len(matrix)):
                        if j > row:
                            makeZero = matrix[j][col]
                            for k in range(len(matrix[0])):
                                matrix[j][k] = round(matrix[j][k] - matrix[row][k] * makeZero, 3)
    result = 1
    for r in range(len(ans)):
        result *= ans[r]
    return round(result)
print(findDeterminant())
