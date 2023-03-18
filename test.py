num = input()
nums = []
for i in num:
    if i.isnumeric():
        nums.append(i)
    else:
        nums.append(' ')
string = ''.join(nums) 
result = [int(i) for i in string.split()]
print(max(result))
lname = 'Pookantong'