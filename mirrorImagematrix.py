#mirror image of matrix

def rotateMatrix(matrix):
    transpose=matrix
    for i in range(row):
        for j in range(cols):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for rows in transpose:
        rows.reverse()
    return transpose





row=int(input())
cols=int(input())
matrix=[]
for i in range(cols):
    arr=[]
    for j in range(row):
        a=int(input())
        arr.append(a)
    matrix.append(arr)
print(matrix)
print(rotateMatrix(matrix))

