diem, ct, xx = [], [], []
j, n = 3, 0
mon1 = ["Toán", "Văn", "Anh", "Lí", "Hóa", "Sinh", "Sử", "Địa", "GDCD", "GDQP"]
mon = mon1.copy()

print("Những môn bạn không cần tính điểm, hãy nhập số 0.")
print("Không được bỏ qua môn Toán, Văn, Anh!!!")

while n <= 2:
        tam = float(input(mon1[n] + ": "))
        if (tam == 0) or (tam < 0) or (tam > 10):
            print("Điểm nhập không hợp lệ!!! Hãy nhập lại.")
        else:
            diem.append(tam)
            n += 1

while j <= 9:
        tam = float(input(mon1[j] + ": "))
        if tam < 0 or tam > 10:
            print("Điểm nhập không hợp lệ!!! Hãy nhập lại.")
        elif tam == 0:
            mon.pop(n)
            j += 1
        else:
            diem.append(tam)
            j += 1
            n += 1

midi, madi = min(diem), max(diem)
DTB = round(sum(diem) / n, 2)
print()
print("Điểm trung bình các môn:", DTB)

def tc(x):
    if x >= 6.5: return "G"
    elif x >= 5: return "K"
    elif x >= 3.5: return "TB"
    elif x >= 2: return "Y"
    else: return "F"

print("Xếp loại học lực:", end=" ")
match DTB:
    case DTB if DTB >= 8:
        if (diem[0] >= 8) or (diem[1] >= 8) or (diem[2] >= 8):
            match(tc(midi)):
                case "G": print("Giỏi")
                case "K": print("Khá")
                case "TB": print("Trung bình")
                case "Y": print("Yếu")
                case "F": print("Kém")
        else:
            match (tc(midi)):
                case "G": print("Khá")
                case "K": print("Khá")
                case "TB": print("Trung bình")
                case "Y": print("Yếu")
                case "F": print("Kém")
    case DTB if DTB >= 6.5:
        if (diem[0] >= 6.5) or (diem[1] >= 6.5) or (diem[2] >= 6.5):
            match(tc(midi)):
                case "G": print("Khá")
                case "K": print("Khá")
                case "TB": print("Trung bình")
                case "Y": print("Yếu")
                case "F": print("Kém")
        else:
            match (tc(midi)):
                case "G": print("Trung Bình")
                case "K": print("Trung Bình")
                case "TB": print("Trung Bình")
                case "Y": print("Yếu")
                case "F": print("Kém")
    case DTB if DTB >= 5:
        if (diem[0] >= 5) or (diem[1] >= 5) or (diem[2] >= 5):
            if midi >= 3.5: print("Trung bình")
            elif midi >= 2: print("Yếu")
        else: print("Kém")
    case DTB if DTB >= 3.5:
        if midi >= 2: print("Yếu")
        else: print("Kém")
    case _: print("Kém")


print("Môn có thành tích tốt nhất:", end=" ")
for i in range(n):
    if diem[i] == madi:
        xx.append(i)
if len(xx) == n:
    print("không có", end=" ")
else:
    for i in range(len(xx)):
        print(mon[xx[i]], end=" ")
print()
print("Môn cần cải thiện:", end=" ")
if DTB >= 8:
    for i in range(n):
            if diem[i] <= 6.5: ct.append(i)
else:
    for i in range(n):
            if diem[i] <= 5: ct.append(i)
if len(ct) == 0:
    print("không có")
elif len(ct) == n:
    print("tất cả các môn")
else:
    for i in range(len(ct)):
        print(mon[ct[i]], end=" ")
print("Học hành như cái nịt thế này thì về quê chăn bò")