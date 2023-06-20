#Compare two arrays of equal size
# size1=size2=5
#arr1=[1,2,3,4,5]
#arr2=[5,4,3,2,1] arr1=arr2

def ComparArr(arr1,arr2):
    sum1=0
    sum2=0
    for i in range(len(arr1)):
        sum1=sum1+arr1[i]
        sum2=sum2+arr2[i]
    if sum1==sum2:
        print("Equal")
    else:
        print("Not equal")




size=int(input())
arr1=size*[None]
arr2=size*[None]

print("arr1:")
for i in range(size):
    a=int(input())
    arr1[i]=a
print("arr2:")
for j in range(size):
    x=int(input())
    arr2[j]=x
ComparArr(arr1,arr2)
