x = input("Enter integers : ").split()
x.sort()

if (x[0] == '0'):
    n = x[1]
    x[1] = x[0]
    x[0] = n

for i in range(len(x)):
    print(x[i], end='')