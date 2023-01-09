small = 0
big = 0
strings = input()
for x in range(len(strings)):
    if strings[x].isupper() == True:
        big = big + 1
    if strings[x].islower() == True:
        small = small + 1 
print("Lower" ,small)
print("Upper" ,big)