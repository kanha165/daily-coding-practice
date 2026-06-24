# Question:
# Check whether a string is palindrome.
# Input: "madam"
# Output: True

str=input("Enter a string: ")
rev=""
for i in range(len(str)-1,-1,-1):
    rev+=str[i]
if str==rev:
    print("True")
else:
    print("False")

print("Reversed string is:",rev)    

