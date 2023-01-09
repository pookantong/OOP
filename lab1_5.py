lists = []
for x in range(999, 1, -1):
    for y in range(999, 1, -1):
        txt = str(x*y)
        if txt == txt[::-1]:
            lists.append(x*y)
print(max(lists))