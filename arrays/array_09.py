# Find majority element (> n/2 times)
from array import array
arr=array('i',[1,2,3,2,2,5,2,4,2])
count={}    
for num in arr:
    if num in count:
        count[num]+=1
    else:
        count[num]=1
        
for num, freq in count.items():
    if freq > len(arr) // 2:
        print("Majority element:", num)
        break
else:
     print("No majority element found")
    