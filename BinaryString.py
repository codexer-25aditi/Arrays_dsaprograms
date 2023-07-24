# #The Binary number system only uses two digits, 0 and 1 and number system can be called binary string. You are required to implement the following function:

# int OperationsBinaryString(char* str);

# The function accepts a string str as its argument. The string str consists of binary digits eparated with an alphabet as follows:

# – A denotes AND operation
# – B denotes OR operation
# – C denotes XOR Operation
# You are required to calculate the result of the string str, scanning the string to right taking one opearation at a time, and return the same.

def OperationsBinartString(st):
    sum=st[0]
    for i in range(0,len(st),2):
        if st[i]=='A':
            sum=sum & st[i+1]
        elif st[i]=='B':
            sum=sum | st[i+1]
        elif st[i]=='C':
            sum=sum ^ st[i+1]
    return sum

st=input()
print(OperationsBinartString(st))
    
