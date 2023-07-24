# You are given a function.
# int CheckPassword(char str[], int n);
# The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
# str is a valid password if it satisfies the below conditions.

# – At least 4 characters
# – At least one numeric digit
# – At Least one Capital Letter
# – Must not have space or slash (/)
# – Starting character must not be a number

def CheckPassword(st,n):
    if n<4:
        return 0
    countCap=0
    countDigit=0
    if  st[0].isdigit()==False and st.isspace()==False:
        for i in range(len(st)):
            if st[i].isupper()==True:
                countCap+=1
            elif st[i]=='/':
                return 0
            elif st[i].isdigit()==True:
                countDigit+=1
                
            
    
    if countCap==0 or countDigit==0:
       return 0
    return 1
   

s=input()
print(CheckPassword(s,len(s)))




