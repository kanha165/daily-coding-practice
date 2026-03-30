#replace negative value with 0
list=[12,34,56,76,-1,8934,-38,-674]
for i in range(len(list)):
    if list[i] < 0:
        list[i]=0
print(list)          