# find second largest
list=[23,45,12,990,85,67,98,45,991,24]

first=second=0
for num in list:
    if num>first:
        second=first
        first=num
    elif num > second and num != first:
        second=num
        
print(second)   
print(first)   


list=[43,86,34,9,4,34,29,79,45,67,89,90,23,45,67,89,90]
first=second=third=0
for num in list:
    if num>first:
        third=second
        second=first
        first=num
    elif num >second and num!=first:
        third=second
        second=num    
    elif num>third and num != second and num !=first:
        third>num
print("First:", first)
print("Second:", second)
print("Third:", third)        
            