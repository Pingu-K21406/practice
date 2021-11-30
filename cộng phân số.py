kq ,ms, ts, tich = [], [], [], 1
n = int(input("số phân số cần tính: "))

for i in range(n):
    tgt = input("Phân số thứ " + str(i+1) + ": ")
    tg = tgt.split("/")
    ts.append(int(tg[0]))
    ms.append(int(tg[1]))

for i in reversed(range(1, min(ms)+1)):
    dem = 0
    for m in ms:
        if m % i == 0:
            dem += 1
    if dem == len(ms):
        ucln = i
        break
    else: ucln = 1

for m in ms:
    tich *= m
bcnn = tich / ucln

for i in range(n):
    tg = ts[i] * (bcnn / ms[i])
    kq.append(tg)

tsc, msc = int(sum(kq)), int(bcnn)

for i in reversed(range(1, min(msc, tsc)+1)):
    if (tsc % i == 0) and (msc % i == 0):
        ucc = i
        break

print("Kết quả: ", int(tsc/ucc), "/" , int(msc/ucc), sep="")
