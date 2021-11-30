diem = []
mon = ["Toán", "Lí", "Hóa", "Sinh", "Sử", "Địa", "Văn", "Anh"]

for i in range(len(mon)):
        tam = float(input(mon[i] + ": "))
        diem.append(tam)

def khoiA(x):
        return x[0] + x[1] + x[2]

def khoiB(x):
        return x[1] + x[2] +x[3]

def khoiC(x):
        return x[4] + x[5] + x[6]

def khoiD(x):
        return x[0] + x[7] + x[6]

j = max(khoiA(diem), khoiB(diem), khoiC(diem), khoiD(diem))

if j == khoiA(diem):
        print("Khối có kết quả tốt nhất: A" + "(" + str(khoiA(diem)) + ")", sep="")
elif j == khoiB(diem):
        print("Khối có kết quả tốt nhất: B" + "(" + str(khoiB(diem)) + ")", sep="")
elif j == khoiC(diem):
        print("Khối có kết quả tốt nhất: C" + "(" + str(khoiC(diem)) + ")", sep="")
elif j == khoiD(diem):
        print("Khối có kết quả tốt nhất: D" + "(" + str(khoiD(diem)) + ")", sep="")


