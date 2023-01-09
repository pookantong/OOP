h1, m1, h2, m2 = [int(x) for x in input().split()]
if m2-m1 < 0:
    m1 += 60
    h1 -= 1
dh = h2-h1
dm = m2-m1
time = (h2*60+m2)-(h1*60-m1)
if time < 15:
    print(0, "Baht")
    exit()
if dm > 0:
    dh+=1
if dh <= 3:
    price = dh * 10
elif dh <= 6:
    price = 30 + ((dh-3)*20)
elif dh > 6:
    price = 200
print(price, "Baht")