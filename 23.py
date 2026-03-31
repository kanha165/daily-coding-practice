# sum of square of the digits
n=int(input("enter the number"))
sum=0
while n>0:
    digit=n%10
    sum+=(digit*digit)
    n=n//10
print(sum)    
    
    
    