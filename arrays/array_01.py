# Find missing number (1 to n)
from array import array
a=array('i',[1,4,5,6,7,8,9,10,11,14,15,16,18,19])
for i in range(1,a[-1]+1):
    if i not in a:
        print("Missing number",i)
