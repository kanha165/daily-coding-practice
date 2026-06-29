#pelindrom  number

n=int(input("Enter a number"))
orignal=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
  
if orignal==rev:
    print(orignal," is a pelindrom ")    
else:
    print(orignal,  " is not pelindrom")    