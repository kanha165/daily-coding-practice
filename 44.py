#Rotate List by position like [1,2,3,4,5,6] R=2 then [5,6,1,2,3,4]
list=[1,2,3,4,5,6]
r=8
# r=r%len(list)
result = list[-r:] + list[:-r]
print(result)



