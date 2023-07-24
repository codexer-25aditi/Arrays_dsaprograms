# def LargeSmallSum(arr)

# The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest  element from the even positions and second smallest from the odd position of given ‘arr’

# Assumption:

# All array elements are unique
# Treat the 0th position as even
# NOTE

# Return 0 if array is empty
# Return 0, if array length is 3 or less than 3
# Example

# Input

# arr:3 2 1 7 5 4

# Output

# 7
def calcsum(arr):
    arr=sorted(arr)
    sums=arr[2]+arr[len(arr)-2]
    return sums
arr=list(map(int,input().split()))

print(calcsum(arr))

