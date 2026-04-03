# Find Sum of Odd Numbers in List
l=[12,23,45,67,89,44]
total=0
for i in l:
    if i%2!=0:
        total+=i
print(total)