# separate even odd in list
list=[23,45,33,45,46,88,92,43,15,76,4,678,97]
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)    
        
print("even",even)
print("odd",odd)        