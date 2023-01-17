def count_minus(num):
    return len([i for i in num if i < 0])
print(count_minus([int(i) for i in input().split()]))