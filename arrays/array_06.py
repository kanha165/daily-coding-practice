# Find subarray with given sum
from array import array
arr=array('i',[1,2,3,7,5,12,15,17,19,21,-5,8,9])
target=12
for i in range(len(arr)):
    current_sum=arr[i]
    for j in range(i+1,len(arr)):
        current_sum+=arr[j]
        if current_sum==target:
            print("Subarray with given sum",arr[i:j+1])