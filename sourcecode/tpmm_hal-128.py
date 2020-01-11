# menghitung GLB
print('opsi:\n1)hitung kecepatan\n2)hitung jarak\n3)hitung waktu\n')
print('ex: gunakan nomor opsi atau nama')

# fungsi untuk tiap operasi


def kecepatan(jarak, waktu):
    print(jarak/waktu)


def jarak():
    print(kecepatan*waktu)


def waktu():
    print(jarak/kecepatan)


# kondisional untuk tiap opsi
if input() == '1' or 'kecepatan':
    kecepatan(int(input()), int(input()))
elif input() == '2' or 'jarak':
    jarak(int(input()), int(input()))
elif input() == '3' or 'waktu':
    waktu(int(input()), int(input()))
else:
    print('opsi salah!')



