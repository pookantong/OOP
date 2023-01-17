def count_char_in_string(x,s):
    return [i.count(s) for i in x]
print(count_char_in_string(input().split(),input()))