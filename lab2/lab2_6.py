def add2list(x,y):
    return [x[i] + y[i] for i in range(len(x))]
print(add2list([int(x) for x in input().split()],[int(x) for x in input().split()]))