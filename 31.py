#Find Difference Between Max and Min
l=[12,23,45,67,112,44]
min=l[0]
max=l[0]
for i in l:
    if i > max:
        max=i
    if i < min:
        min=i
print(max-min)            