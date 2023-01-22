def char_count(str):
    return {[x for x in str][i] : str.count([x for x in str][i]) for i in range(len(str))}
print(char_count('language'))