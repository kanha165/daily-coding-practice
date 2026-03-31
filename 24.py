# find first digit of a number
n=int(input("Enter a number :"))
first=0
while n>0:
    digit=n%10
    first=digit
    n=n//10
print(first)    