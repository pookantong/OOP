list1 = [int(item) for item in input().split()]
list1.sort()
for i in range(len(list1)):
    if list1[0] == 0:
        list1[0], list1[i] = list1[i], list1[0]
print(*list1, sep = "")