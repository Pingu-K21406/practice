from tkinter import *
stt=1
diem, mon, tc = [], [], []
window = Tk()
window.title("Score tracking")
window.geometry('400x500')

#Tạo khung
frame0 = Frame(window)
frame0.pack()

frame1 = Frame(window)
frame1.pack()

frame2 = Frame(window)
frame2.pack(pady=10)

frame3 = Frame(window)
frame3.pack()

frame4 = Frame(window)
frame4.pack(pady=10)

#Tạo nhãn
Stt = Label(frame0, text="STT")
Stt.pack(padx=4, side=LEFT)

Stc = Label(frame0, text="STC")
Stc.pack(padx=4, side=LEFT)

Nhan_mon = Label(frame0, text="Tên môn")
Nhan_mon.pack(padx=75, side=LEFT)

Nhan_diem = Label(frame0, text="Điểm")
Nhan_diem.pack(padx=25,side=LEFT)

#Tạo con lăn
scrollball = Scrollbar(frame1)
scrollball.pack(side=RIGHT, fill=Y)

#Tạo khung hiển thị
STT = Listbox(frame1, width=3, height=5, font=('Arial',10), justify="center", bd=1, fg="#000000", highlightthickness=0,
              selectbackground="#9529cf", activestyle="none", exportselection=0, yscrollcommand=scrollball.set)
STT.pack(side=LEFT)

listtc = Listbox(frame1, width=4, height=5, font=('Arial',10), justify="center", bd=1, fg="#000000", highlightthickness=0,
                 selectbackground="#9529cf", activestyle="none", exportselection=0, yscrollcommand=scrollball.set)
listtc.pack(side=LEFT)

listmon = Listbox(frame1, width=33, height=5, font=('Arial',10), bd=1, fg="#000000", highlightthickness=0,
                  selectbackground="#9529cf", activestyle="none", exportselection=0, yscrollcommand=scrollball.set)
listmon.pack(side=LEFT)

listdiem = Listbox(frame1, width=5, height=5, font=('Arial',10), justify="center", bd=1, fg="#000000", highlightthickness=0,
                  selectbackground="#9529cf", activestyle="none", exportselection=0, yscrollcommand=scrollball.set)
listdiem.pack(side=LEFT)

#Khung kết quả

KQ1 = Label(frame4, text="", justify=LEFT)
KQ1.pack()

KQ2 = Label(frame4, text="", justify=LEFT)
KQ2.pack()

KQ3 = Label(frame4, text="", justify=LEFT)
KQ3.pack()

KQ4 = Label(frame4, text="", justify=LEFT)
KQ4.pack()

#Cấu hình thanh lăn
def multiview(*args):
    listmon.yview(*args)
    listdiem.yview(*args)
    listtc.yview(*args)
    STT.yview(*args)
scrollball.config(command=multiview)

#Đầu vào dữ liệu
inp_tc = IntVar()
inp_tc.set(3)
inp_tcmenu = OptionMenu(frame2, inp_tc, 2, 3)
inp_tcmenu.grid(row=0, column=0)

inp_mon = Entry(frame2, width=30)
inp_mon.grid(row=0, column=1)

inp_diem = Entry(frame2, width=10)
inp_diem.grid(row=0, column=2)

#Tạo nút
def them():
    global stt
    STT.insert(END, stt)
    stt += 1

    listmon.insert(END, inp_mon.get())
    mon.append(inp_mon.get())
    inp_mon.delete(0, END)

    listdiem.insert(END, inp_diem.getdouble(inp_diem.get()))
    diem.append(float(inp_diem.get()))
    inp_diem.delete(0, END)

    listtc.insert(END, inp_tc.get())
    tc.append(inp_tc.get())

    nut_xoa['state'] = ACTIVE
    nut_capnhat['state'] = ACTIVE

def xoa():
    global stt
    STT.delete(END)
    stt -= 1

    x = listmon.curselection()[0]
    mon.pop(x)
    diem.pop(x)
    tc.pop(x)

    listmon.delete(ANCHOR)
    listdiem.delete(x)
    listtc.delete(x)

    if len(mon) == 0:
        nut_xoa['state'] = DISABLED
        nut_capnhat['state'] = DISABLED

def capnhat():
    # Hàm tính điểm trung bình
    def tongdiem(a, b):
        c = 0
        for l in range(len(diem)):
            c = c + a[l]*tc[l]
        c = (c / sum(b))
        return c

    # Hàm xếp loại
    def xeploai(z):
        if (z >= 9) and (z <= 10):
            return("Xếp loại: Xuất sắc")
        elif (z >= 8):
            return("Xếp loại: Giỏi")
        elif (z >= 7):
            return("Xếp loại: Khá")
        elif (z >= 6):
            return("Xếp loại: Trung bình khá")
        elif (z >= 5):
            return ("Xếp loại: Trung bình")
        elif (z >= 4):
            return("Xếp loại: Yếu")
        elif (z < 4) and (z >= 0):
            return("Xếp loại: Kém")

    # Phần tính điểm và xếp loại
    trungbinh= round(tongdiem(diem, tc), 2)

    KQ1.config(text="Điểm trung bình: "+str(trungbinh))
    KQ2.config(text=xeploai(trungbinh))
    KQ3.config(text="Môn có thành tích tốt nhất: " + str(mon[diem.index(max(diem))]))
    KQ4.config(text="Môn cần cải thiện nhiều nhất: " + str(mon[diem.index(min(diem))]))

nut_xoa = Button(frame3, text="Xóa", command=xoa, state=DISABLED)
nut_them = Button(frame3, text="Thêm", command=them)
nut_capnhat = Button(frame3, text="Kết quả", command=capnhat, state=DISABLED)

nut_xoa.grid(row=0, column=0, padx=20)
nut_them.grid(row=0, column=1, padx=20)
nut_capnhat.grid(row=0, column=2, padx=20)

window.mainloop()


