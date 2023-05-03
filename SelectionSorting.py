list1 = [56,3,2,78,6,0]
print("original", list1)

for i in range(len(list1)):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val)
    temp = list1[i]
    list1[i] = list1[min_ind]
    list1[min_ind]= temp

print("min", list1)

for i in range(len(list1)):
    max_val = max(list1[i:])
    max_ind = list1.index(max_val)
    temp = list1[i]
    list1[i] = list1[max_ind]
    list1[max_ind]= temp

print("max", list1)