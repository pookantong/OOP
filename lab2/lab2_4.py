def count_minus(num):
    return sum([i.count('-') for i in num])
print(count_minus(input().split()))