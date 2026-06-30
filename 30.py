#. Product of even digits only

# 👉 Example: 1234 → 2×4 = 8
num=int(input("Enter a number :"))
product=1
while num > 0:
    digit=num%10
    if digit % 2==0:
        product*=digit
    num=num//10    
print(product)        
        
    