def solve(s):
    sum=int(s[0])
    
    for i in range(0,len(s),2):
        if s[i]=='A':
            sum&=int(s[i+1])
        elif s[i]=='B':
            sum|=int(s[i+1])
        elif s[i]=='C':
            sum^=int(s[i+1])

    return sum
            
            

s=input()
print(solve(s))
