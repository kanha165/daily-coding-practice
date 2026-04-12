# Find intersection of two arrays
from array import array
arr=array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
arr2=array('i',[1,4,5,6,7,8,9])
for i in arr:
    if i in arr2:
        print("Common element",i)