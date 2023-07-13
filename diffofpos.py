#difference between odd pos and even positons
a=(input())

sumo=0
sume=0
for i in range(len(str(a))):
    if i%2==0:
        sume=sume+int(a[i])
    else:
        sumo=sumo+int(a[i])

print(sumo-sume)
