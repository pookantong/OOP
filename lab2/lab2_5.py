def only_english(string1):
    return ''.join(i for i in string1 if i.isalpha() and i.isascii())
print(only_english(input()))