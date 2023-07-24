
#The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i
def Calculate(arr,r,unit):
    sum=0
    total=r*unit
    
    for i in range(0,len(arr)):
        sum=sum+arr[i]
        if sum>total:
            return i+1
    
        


r=int(input())
units=int(input())
arr=list(map(int,input().split()))
print(Calculate(arr,r,units))
