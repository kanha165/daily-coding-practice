# Question:
# Find the first non-repeating character.
# Input: "aabbcddeff"
# Output: c

s = "aabbcddeff"

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break