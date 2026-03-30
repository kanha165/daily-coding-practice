# 22. Write a Python program to find the second smallest and second largest digits in a given number.

n = int(input("Enter number: "))

# first = 9
# second = 9

# while n > 0:
#     digit = n % 10
    
#     if digit < first:
#         second = first
#         first = digit
#     elif digit < second and digit != first:
#         second = digit
        
#     n = n // 10

# print("Second smallest digit:", second)



first = 0
second = 0

while n > 0:
    digit = n % 10
    
    if digit >  first:
        second = first
        first = digit
    elif digit > second and digit != first:
        second = digit
        
    n = n // 10

print("Second largest digit:", second)



