def pattern(num):
    if num == 0:
        return 
    else:
        pattern(num - 1)
        print("* " * num)

num = int(input("enter num: "))
pattern(num)