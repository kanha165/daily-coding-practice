# Replace all even digits with 0

# 👉 Example: 1234 → 1030
num = int(input("Enter the number: "))
result=0
place=1
while num > 0:
    digit=num%10
    if digit%2==0:
        digit=0
    result=result+digit*place
    place*=10
    num=num//10
print(result)        
              