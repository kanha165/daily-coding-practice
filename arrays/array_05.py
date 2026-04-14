# Find all pairs with given sum
from array import array
arr =array("i",[1, 5, 7, -1, 5])
target = 6

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print("Pair with given sum",arr[i],arr[j],"is",target)