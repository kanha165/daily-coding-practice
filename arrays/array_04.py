# Find union of two array whithout set
from array import array
arr=array('i',[1,2,3,4,5,6,7,78,54,92,36,45,67,89,90,12,34,56,78,90])
arr2=array('i',[56,67,3,21,54,56,9])
result=arr+arr2
final=array('i',[])
for i in result:
    if i not in final:
        final.append(i)
print("Union of two arrays:", final)