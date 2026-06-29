# remove duplicate from a list 

list=[2,3,2,4,5,6,7,78,45,32,45,32,5,78]
result=[]
for i in list:
    if i not in result:
        result.append(i)
    
print(result)        
        