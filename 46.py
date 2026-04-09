# Find Element with Minimum Frquency
a=[1,2,3,4,4,3,2,1,2,3,5,6,8,1,9,8,4,3,7,1,1,4,5,7,9,9]
result={}
for num in a:
    if num in result:
        result[num]+=1
    else:
        result[num]=1
min_f=9       
for i in result.values():
    if i < min_f:
        min_f=i
        
for key,values in result.items():
    if values==min_f:
        print("Element",key,"Value",values)
                    