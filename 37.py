#Find all even numbers in the list and their sum
l=[12,23,45,67,89,44]
even=[]
even_sum=0
for i in l:
    if i%2==0:
        even.append(i)
        even_sum+=i
print("total even number",even)        
print("sum of even number",even_sum)        