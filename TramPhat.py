import string
ten = string.ascii_uppercase
n = int(input("Số trạm: "))
tram = []

for i in range(n):
    matrix = []
    for j in range(n):
        if i == j:
            tam = 0
            matrix.append(tam)
        elif i > j:
            tam = tram[j][i]
            matrix.append(tam)
        else:
            tam = int(input("Khoảng cách từ trạm " + str(ten[i]) + " đến trạm " + str(ten[j]) + ": "))
            matrix.append(tam)
    tram.append(matrix)

print()
for i in range(n):
    print("Khoảng cách trạm", ten[i],":",tram[i])





