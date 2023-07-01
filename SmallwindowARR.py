

#Find the smallest window to be sorted to get the whole array sorted
def sortWindow(arr):

    level = []
    arr1 = sorted(arr)
    for i in range(len(arr)):
        if arr[i] != arr1[i]:
            level.append(i)
    low = min(level)
    high = max(level)

    return low,high

arr=list(map(int,input().split()))
print(sortWindow(arr))
print("Sorted array:")
print(sorted(arr))

