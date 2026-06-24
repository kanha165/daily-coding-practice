# Input: "ABCD", "CDAB"
# Output: True

s1 = "ABCD"
s2 = "CDAB"

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("True")
else:
    print("False")