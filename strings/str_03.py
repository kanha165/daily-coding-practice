# Question:
# Check whether two strings are anagrams.
# Input: "listen", "silent"
# Output: True


s1="listen"
s2="silent"

dict1={}
for ch in s1:
    if ch in dict1:
        dict1[ch]+=1
    else:
        dict1[ch]=1

dict2={}
for ch in s2:
    if ch in dict2:
        dict2[ch]+=1
    else:
        dict2[ch]=1


if dict1==dict2:
    print("True")
else:
    print("False")                    