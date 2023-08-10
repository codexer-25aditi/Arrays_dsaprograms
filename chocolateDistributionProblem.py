

#Chocolate distribution problem

def solve(arr,n):
    arr.sort()
    min=arr[len(arr)-1]
    for i in range(len(arr)-n+1):
        if arr[i+n-1]-arr[i]<min:
            min=arr[i+n-1]-arr[i]
    return min



arr=list(map(int,input().split()))
n=int(input())
print(solve(arr,n))
