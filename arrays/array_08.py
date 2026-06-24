# Rearrange array (positive & negative alternate)
from array import array
arr=array('i',[1,2,3,-4,-1,4])
positive=array('i',[])
negative=array('i',[])
for i in arr:
    if i>=0:
        positive.append(i)
    else:
        negative.append(i)
print("Positive array",positive)
print("Negative array",negative)        