#Take an array size and print the odd sum ,even sum of the array

def calculate(arr):
    sumo=0
    sume=0
    for i in range(len(arr)):
        if arr[i]%2==0:
            sume=sume+arr[i]
        else:
            sumo=sumo+arr[i]
    print("sum of odd",sumo)
    print("sum of eve",sume)




n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
calculate(arr)
