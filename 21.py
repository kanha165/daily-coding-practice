# find smallest even number
list=[12,34,56,76,34,36,85,35,74]
min_even=list[0]
for i in list:
    if i%2==0:
        if i < min_even:
            min_even=i
print(min_even)            
        