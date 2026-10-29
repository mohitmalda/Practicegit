str=input("Enter the string")
n=len(str)
i=0
j=n-1
isPallindrome=True
while(i<j):
    if(str[i]!=str[j]):
        isPallindrome=False
        break
if(isPallindrome):
    print("The String is Pallindrome")
else:
    print("The String is not Pallindrome hi")