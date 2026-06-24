# Question 7:
# Find the character that appears the most times.
# Input: "success"
# Output: 's'

str=input("Enter a string: ")
freq={}
for ch in str:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
        
max_char = ""
max_count = 0

for ch in freq:
    if freq[ch] > max_count:
        max_count = freq[ch]
        max_char = ch

print(max_char)