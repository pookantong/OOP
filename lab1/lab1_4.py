x = input("Input : ")
num = x
sum = 0
for i in range(4):
    sum += int(num)
    num = num + x
print(sum)