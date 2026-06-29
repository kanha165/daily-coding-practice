# input abdlnaabld
# output=a3b2d2l2n1
string=input("enter a string")
result={}
for ch in string:
    if ch in result:
        result[ch]+=1
    else:
        result[ch]=1
        
print(result)        
            
           

