
#check array having only even or only odd or mixed elements
arr=list(map(int,input().split()))

counte=0
counto=0

for i in range(len(arr)):
    if arr[i]%2==0:
        counte=counte+1 
    else:
        counto=counto+1 

if counte==len(arr):
    print("1")
elif counto==len(arr):
    print("0")
else:
    print("Array with mixed elements")
