# # rows=int(input())
# # columns=int(input())
# # matrix=list()
# #
# # for i in range(0,columns):
# #     a=[]
# #     for j in range(0,rows):
# #         # x=int(input())
# #         a.append(x)
# #     matrix.append(a)
# # print(matrix)
# #
# #
# #
# #
# def matriX(matrix,rows,cols):
#     for i in range(0, col):
#         for j in range(0, rows):
#             if matrix[i][j] == target:
#                 return "Present"
#
#     return "Not Present"
#
# col=int(input("Columns:"))
# rows=int(input("Rows:"))
# target=int(input("Target:"))
# matrix=[]
# for i in range(0,col):
#     a=[]
#     for j in range(0,rows):
#         x=int(input())
#         a.append(x)
#     matrix.append(a)
#
# print(matriX(matrix,rows,col))
#
#
#Print primary and secondary diagonal

#
def PRimarySecondary(matrix,rows,columns):
    primary=[]
    secondary=[]
    for i in range(0,cols):
        for j in range(0,rows):
            if i==j:
                primary.append(matrix[i][j])
            if i+j==cols-1:
                secondary.append(matrix[i][j])
    return primary,secondary


rows=int(input("Rows:"))
cols=int(input("Columns:"))
matrix=[]
for i in range(0,cols):
    arr=[]
    for j in range(0,rows):
        x=int(input())
        arr.append(x)
    matrix.append(arr)
primary,secondary=PRimarySecondary(matrix,rows,cols)
print("Primary diagonal:",primary)
print("Secondary diagonal:",secondary)

