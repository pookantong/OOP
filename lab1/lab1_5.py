lists = []
for x in range(100, 1000):
    for y in range(100, 1000):
        txt = str(x*y)
        if txt == txt[::-1]:
            print(x,y,txt)
            lists.append(x*y)
print(max(lists))