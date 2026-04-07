# Take two list and find the common elements from both list
l1=[12,23,45,67,89]
l2=[23,45,67,89,44]
common=[]
for i in l1:
    if i in l2:
        common.append(i)
print(common)    