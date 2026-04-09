#Find Frequency of each elements: [1,1,2,3,3,2,3]
l=[1,2,3,4,5,6,7,9,6,4,2,2,1,4,5,7,8,9,8,6,5,5,6,4,3,4,3,3,56,4,3]
result={}
for num in l:
    if num in result:
        result[num]+=1
    else:
        result[num]=1
print(result)            

