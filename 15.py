# count positive and negative
n=[10,28,-1,972,-73,74]
negative_count=0
positive_count=0
for i in n:
    if i>=0:
        positive_count+=1
    else:
        negative_count+=1
        
print("positive number in a list is :",positive_count)            
print("negative number in a list is :",negative_count)            
        
    