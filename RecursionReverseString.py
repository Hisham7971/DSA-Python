def reverse_str(str):
    if (len(str) == 1):
        return str
    else:
        return reverse_str(str[1:])+str[0]
    
str = input("enter a string: ")
result = reverse_str(str)
print(result)