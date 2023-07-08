#equillibrium point in array
#left hand side of element is equal to that right hand side

def Equillibrium(arr):
    for i in range(1,len(arr)):
        suml=0
        sumr=0
        for j in range(0,i):
            suml=suml+arr[j]
        for k in range(i+1,len(arr)):
            sumr=sumr+arr[k]

        if suml==sumr:
            return i

arr=list(map(int,input().split()))

print(Equillibrium(arr))
