

#Find if there is a pair with a given sum in the rotated sorted Array

def solve(arr,n):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==n:
                return True
    return False



arr=list(map(int,input().split()))
n=int(input())
print(solve(arr,n))
