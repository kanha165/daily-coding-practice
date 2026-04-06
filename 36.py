# Check if List is Sorted, Ascending Descending both
l=[12,23,45,67,89]
asc=True
desc=True
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        asc=False
    if l[i]<l[i+1]:
        desc=False
if asc:
    print("list are arranged in ascending order")  
elif desc:              
    print("list are arranged in descending order")
else:
    print("list are  not sorted")                