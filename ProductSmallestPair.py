# def ProductSmallestPair(sum, arr)

# The function accepts an integers sum and an integer array arr of size n. Implement the function to find the pair, (arr[j], arr[k]) where j!=k, Such that arr[j] and arr[k] are the least two elements of array (arr[j] + arr[k] <= sum) and return the product of element of this pair

# NOTE

# Return -1 if array is empty or if n<2
# Return 0, if no such pairs found
# All computed values lie within integer range
# Example
# #
# Input

# sum:9

# size of Arr = 7

# Arr:5 2 4 3 9 7 1

# Output

#  2

def ProductSmallestPair(sums,arr):
    mini=arr[0]
    minj=arr[0]
    S=mini+minj
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                continue
            else:
                if arr[i]+arr[j]<S and arr[i]+arr[j]<=sums:
                    mini=arr[i]
                    minj=arr[j]
                    S=arr[i]+arr[j]
    return mini*minj
                    
                
                    
arr=list(map(int,input().split()))
sums=int(input())
print(ProductSmallestPair(sums,arr))

