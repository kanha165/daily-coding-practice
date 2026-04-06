# 4. Remove all vowels from string

# 👉 Example: "kanha" → "knh"

string=input("Enter a string :")
result=""
for ch in string:
    if ch not in "AEIOUaeiou":
        result+=ch
print(result)        