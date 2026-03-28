#factorial
n=int(input("Enter a number: "))
fact=1
if n<0:
    print("factorial does not exist for negative numbers")
elif n==0:    
    print("factorial of",n,"is",n)
else:
    for i in range(1,n+1):
        fact=fact*i 
    print("factorial of",n,"is",fact)