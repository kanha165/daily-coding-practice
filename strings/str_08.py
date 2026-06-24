# Input: "banana"
# Output: {'b':1, 'a':3, 'n':2}

s = "banana"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)