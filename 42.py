# Find Element of maximum frequency
a=[1,2,3,4,4,3,2,1,2,3,5,6,8,1,9,8,4,3,7,1,1,4,5,7,9,9]
result={}
for num in a:
    if num in result:
        result[num]+=1
    else:
        result[num]=1
largest_f=0        
for i in result.values():
    if i >largest_f:
        largest_f=i
        
for key,values in result.items():
    if values==largest_f:
        print("Element",key,"Value",values)



           
   
    
      
        
        
           