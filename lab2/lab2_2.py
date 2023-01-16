def count_char_in_string(x,c):
    count = []
    for i in range(len(x)):
        temp = x[i].count(c)
        count.append(temp)
    return count
print(count_char_in_string(input().split(),input()))