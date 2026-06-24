# Leaders in an array (elements greater than right side)
from array import array
arr=array('i',[16,17,4,3,7,5,2])
for i in range(len(arr)):
    leader=True
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            leader=False
    if leader:
        print("Leader in array",arr[i])
            
            