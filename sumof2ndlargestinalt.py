#find the sum of second largest element from both even and odd placed elements in given array.
arr=list(map(int,input().split()))
sumo=[]

sume=[]
for i in range(len(arr)):
    if i%2==0:
        sumo.append(arr[i])
    else:
        sume.append(arr[i])

sumo=sorted(sumo)
sume=sorted(sume)

print(sumo[1]+sume[1])
