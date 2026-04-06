# Count Elements Equal to Average
l=[1,2,3,4,5,6,7,8,9]
total=0
for i in l:
    total+=i 
avg=total//len(l)    
for i in l:
    if avg==i:
        print(i,"yes")
    else:
        print(i,"no")    
