def count_minus(str):
    count = 0
    for i in range(len(str)):
        count += str[i].count('-') 
    return count
print(count_minus(input().split()))