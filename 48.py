# Convert lowercase to uppercase (without built-in functions)
string=input("Enter a string  :")
upper_str=""
for ch in string:
    asccii_value=ord(ch)
    if 97<=asccii_value<=122:
        upper_str+=chr(asccii_value-32)
    else:
        upper_str+=ch
print(upper_str)        
    
    