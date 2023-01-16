def only_english(string1):
    return ''.join(i for i in string1 if i.isalpha())

print(only_english(input()))