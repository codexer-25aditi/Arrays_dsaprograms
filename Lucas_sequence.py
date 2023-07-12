arr=[]
ins=int(input())
arr.append(0)
arr.append(0)
arr.append(1)

for i in range(3,ins):
    arr.append(arr[i-1]+arr[i-2]+arr[i-3])
print("Lucas sequence:")
print(arr)
