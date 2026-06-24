# Question 1:
# Given a string "Python is awesome",
# reverse each word individually without changing the order of words.
# Output: "nohtyP si emosewa"



str=input("Enter a string: ")
reversed_words=""
for word in str.split():
    reversed_words += word[::-1] + " "
print(reversed_words.strip())    