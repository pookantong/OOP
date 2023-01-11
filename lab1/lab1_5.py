lists = []
for x in range(1, 1000):
    for y in range(1, 1000):
        txt = str(x*y)
        if txt == txt[::-1]:
            lists.append(x*y)
print(max(lists))