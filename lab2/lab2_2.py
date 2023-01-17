def count_char_in_string(x,s):
    count = []
    for i in range(len(x)):
        temp = x[i].count(s)
        count.append(temp)
    return count
print(count_char_in_string(input().split(),input()))