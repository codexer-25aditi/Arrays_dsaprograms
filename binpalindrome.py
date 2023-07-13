#check the given binary is palindrome or not
def checkPalindrome(a):
    if a==a[::-1]:
        return True
    else:
        return False
    
a=input()
sum=0


an=int(a)
decimal, i = 0, 0
while(an!= 0):
        dec = an % 10
        decimal = decimal + dec * pow(2, i)
        an = an//10
        i += 1

if checkPalindrome(a)==True:
    print(f"{decimal} is palindrome")
else:
    print(f"{decimal} is not palindrome")
