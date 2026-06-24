# Find duplicate element
from array import array
arr=array('i',[1,2,3,1,4,5,9,6,7,5,8,9,10,11,12,3,13,14,1,5,16,17,18,19])
result={}
for num in arr:
    if num in result:
        result[num]+=1
    else:
        result[num]=1
for key,values in result.items():
    if values > 1:
        print("Element",key,"Value",values)            