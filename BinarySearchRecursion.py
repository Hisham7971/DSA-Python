def binary_search(l,low,high,mid,s):
    if low<=high:
        mid = (low+high) // 2
        if l[mid] == s:
            print(s, "is found at position", mid+1)
        elif l[mid]>s:
            binary_search(l,low,mid-1,mid,s)
        else:
            binary_search(l,mid+1,high,mid,s)
    else:
        print(s, "is not found")

l = list()
n = int(input("enter number of elements to be inserted:    "))
print("enter ", n, " elements")
for i in range(n):
    l.append(int(input()))
l.sort()
print("After sorting")
print(l)
s = int(input("enter search element:    "))
low=0
high=len(l)-1
mid=(low+high) // 2
binary_search(l,low,high,mid,s)