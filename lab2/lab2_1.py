list1 = []
list1 = [int(item) for item in input().split()]
for x in range(len(list1)):
    for y in range(len(list1)):
        if list1[x] < list1[y]:
            temp = list1[y]
            list1[y] = list1[x]
            list1[x] = temp
for i in range(len(list1)):
    if list1[0] == 0:
        temp = list1[0]
        list1[0] = list1[i]
        list1[i] = temp
print(*list1, sep = "")