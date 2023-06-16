#Search element in sorted array
def SearchinSort(matrix,num):
    arr=[]
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            arr.append(matrix[i][j])
    arr=sorted(arr)
    matrixx=[]
    a=0
    for i in range(0,len(matrix)):
        arrr=[]

        for j in range(0,len(matrix[i])):
            arrr.append(arr[a])
            a=a+1
        matrixx.append(arrr)
    for i in range(0,len(matrixx)):
        for j in range(0,len(matrixx[i])):
            if matrixx[i][j]==num:
                return True
    return False



rows=int(input("Rows:"))
cols=int(input("Cols:"))

Mat=[]
for i in range(0,cols):
    arr=list(map(int,input().split()))
    Mat.append(arr)

num=int(input("Target:"))
print(SearchinSort(Mat,num))
