# count vowels and consonants    
str=input("enter a string")
vowels_count=0
conso_count=0
for ch in str:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels_count+=1
        else:
            conso_count+=1
print(vowels_count)
print(conso_count) 