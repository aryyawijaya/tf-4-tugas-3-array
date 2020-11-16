klubA = input('Klub A : ')
klubB = input('Klub B : ')

i = 1
hasil = []
kondisi = False
while (not kondisi):
    a = list(map(int,input(f'Pertandingan {i} : ').split()))
    if (a[0]>=0) and (a[1]>=0):
        i += 1
        if (a[0]>a[1]):
            hasil.append(klubA)
        elif (a[0]<a[1]):
            hasil.append(klubB)
        else:
            hasil.append('Draw')
    else:
        kondisi = True
for i in range(len(hasil)):
    print(f'Hasil {i+1} : {hasil[i]}')
print('Pertandingan selesai')