
def printLeaders(arr, size):
    for i in range(0, size):
        for j in range(i + 1, size):
            if arr[i] <= arr[j]:
                break
        if j == size - 1:
            print(arr[i], end=' ')


arr =list(map(int,input().split()))
printLeaders(arr, len(arr))

