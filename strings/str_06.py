# Question 6:
# Remove duplicate characters while preserving order.
# Input: "programming"
# Output: "progamin"

str=input("Enter a string: ")
result=""
for ch in str:
    if ch not in result:
        result+=ch
print("String after removing duplicates:", result)