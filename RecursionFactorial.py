def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)

n = int(input("enter a number: "))

result = factorial(n)

print(result)


# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
# print(fact)