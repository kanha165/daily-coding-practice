# Shift all 0 of the list to the end
list=[1,2,0,3,4,0,4,0,4,5,0,0,9,0,9,0,7,6,5,4,9,0]
new=[]
for i in range(len(list)):
    if list[i]!=0:
        new.append(list[i])
for i in range(len(list)-len(new)):
    new.append(0)   
print(new)        