small = 0
big = 0
strings = input()
for x in range(len(strings)):
    if strings[x].isupper():
        big = big + 1
    if strings[x].islower():
        small = small + 1 
print(small)
print(big)