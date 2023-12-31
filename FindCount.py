# int findCount(int arr[], int length, int num, int diff);

# The function accepts an integer array ‘arr’, its length and two integer variables ‘num’ and ‘diff’. Implement this function to find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.
# Note: In case there is no element in ‘arr’ whose absolute difference with ‘num’ is less than or equal to ‘diff’, return -1.

# Example:
# Input:

# arr: 12 3 14 56 77 13
# num: 13
# diff: 2
# Output:
# 3

def findCount(arr,n,num,diff):
    count=0
    for i in range(n):
        if arr[i]-num<=diff:
            count+=1
    if count==0:
        return -1
    else:
        return count-1
    
arr=list(map(int,input().split()))
num=int(input())
diff=int(input())
print(findCount(arr,len(arr),num,diff))
