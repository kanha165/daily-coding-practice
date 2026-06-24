# Input: "Python is a powerful programming language"
# Output: programming

s = "Python is a powerful programming language"

words = s.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)