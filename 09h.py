# input aabbcccccdeeeee
# putput=a2b2c5d1e5
string=input("enter a string")
result=""
count=1
for i in range(1,len(string)):
    if string[i]==string[i-1]:
        count+=1
    else:
        result+=string[i-1]+str(count)
        count=1
        
print(result+string[-1]+str(count))        
        
        
        
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

