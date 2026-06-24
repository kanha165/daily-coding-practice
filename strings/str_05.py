# Question:
# Count the number of vowels.
# Input: "programming"
# Output: 3

str="programming"
vowels="aeiouAEIOU"
count=0
for ch in str:
    if ch in vowels:
        count+=1
print("Number of vowels:",count)        