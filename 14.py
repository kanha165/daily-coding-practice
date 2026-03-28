# count even odd in a list
list=[23,13,6,2,4,98,4,78,1,3,5,7,9]
even=0
odd=0
for i in list:
    if i%2==0:
        even+=1
    else:
        odd+=1
        
print("even count is ",even)            
print("odd count is ",odd)            