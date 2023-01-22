def char_count(str):
    return {str[i] : str.count(str[i]) for i in range(len(str))}
print(char_count('language'))