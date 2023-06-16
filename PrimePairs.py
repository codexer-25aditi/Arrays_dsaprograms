#Print the pairs of prime numbers having difference of 6 between a given range

def calcPrimepairs(u,l):
    arr=[]
    for i in range(u,l+1):
        counter=0
        for j in range(1,i+1):
            if i%j==0:
                counter=counter+1
        if counter==2:
            arr.append(i)

    for i in range (0,len(arr)):
        num=arr[i]+6
        if num in arr:
            print(f"({arr[i]},{num})",end=" ")




lower=int(input())
upper=int(input())
print(f"The prime pairs between {lower} and {upper} are:\n")
calcPrimepairs(lower,upper)