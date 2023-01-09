n = 10
for row in range(n):
    for col in range(n):
        if row + col < n:
            print(' ',end="")
        else:
            print("#",end='')
    print("#")