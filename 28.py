# 7. Find longest word in string

# 👉 Example: "I love programming" → "programming"

string="I love  python programming "
length=0
longest_str=""    
for word in string.split():
    if len(word)>length:
        length=len(word)
        longest_str=word
print(longest_str)        


