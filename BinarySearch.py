l = list()
n = int(input("enter number of elements to be inserted:    "))
print("enter ", n, " elements")
for i in range(n):
    l.append(int(input()))
l.sort()
print("sorted list", l)

s = int(input("enter search element:    "))
low = 0
high=len(l)-1
mid=0
while low<=high:
    mid=(low+high) // 2
    if l[mid] == s:
        print(s, "is found at position ", mid+1)
        break
    elif l[mid]>s:
        high=mid-1
    else:
        low=mid+1
else:
    print(s, "is not found")
