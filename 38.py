# Count the numbers in the list which are ending with 5
list=[12,34,56,78,90,15,34,95]
count=0
for num in list:
    digit=num%10
    if digit==5:
        count+=1
print(count)        