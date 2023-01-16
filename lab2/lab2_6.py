def add2list(x,y):
    lists = []
    for i in range(len(x)):
        lists.append(x[i] + y[i])
    return lists
print(add2list([int(x) for x in input().split()],[int(x) for x in input().split()]))