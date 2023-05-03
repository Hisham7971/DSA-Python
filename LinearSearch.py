ls = list()
n = int(input("enter number of elements: "))
for i in range(n):
    ls.append(int(input()))
s = int(input("enter element to search "))

if s in ls:
    print(s, "found at", ls.index(s+1))
else:
    print(s, "is not found")
