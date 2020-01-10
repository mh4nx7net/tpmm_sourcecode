print('masukan opsi: ')
print('[persegi|lingkaran]')
# mendapatkan nilai
opsi = input()

# fungsi pengolahan nilai
def olah_persegi():
    print('masukan panjang sisi:')
    sisi = int(input())
    luas = sisi * sisi
    print('hasilnya : ', luas)

def olah_lingkaran():
    print('masukan jari-jari:')
    jari = int(input())
    luas = 3.14 * (jari**2)
    print('hasilnya : ', luas)

# mendiskusikan rentang nilai
if opsi == 'persegi':
    # pengolahan dengan pemanggilan fungsi
    olah_persegi()
elif opsi == 'lingkaran':
    # pengolahan dengan pemanggilan fungsi
    olah_lingkaran()
else:
    print('masukaan opsi dengan benar')
