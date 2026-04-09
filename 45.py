# Check if Two Lists Are Rotations of Each Other

a = [1,2,3,4,5]
b = [3,4,5,1,2]

if len(a) != len(b):
    print("Not rotation")
else:
    temp = a + a
    
    found = False
    for i in range(len(a)):
        if temp[i:i+len(b)] == b:
            found = True
            break

    print("Rotation" if found else "Not rotation")
       