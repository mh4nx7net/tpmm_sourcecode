print('opsi:\na)tambah\nb)kurang\nc)kali\nd)bagi')
print('contoh: nilai1 (opsi) nilai2\n')

def olah(masukan):
    # masukan = [nilai1, opsi, nilai2]
    # variable masukan berupa list
    # melakukan iterasi dan mengubahnya menjadi masing2 variable
    nilai1, opsi, nilai2 = masukan
    # FYI!. pada umumnya bahasa pemrograman klasik,
    # variable perlu dideklarasikan terlebih dahulu
    # namun tidak pada python ! hal ini bersifat opsional.
    # bahkan lebih baik tidak samasekali. *Cmiww
    hasil = int()

    # alternative switch-case pada python
    # dengan menggunakan conditional ifelse
    if opsi == 'a' or 'tambah':
        hasil = int(nilai1) + int(nilai2)
    elif opsi == 'b' or 'kurang':
        hasil = int(nilai1) - int(nilai2)
    elif opsi == 'c' or 'kali':
        hasil = int(nilai1) * int(nilai2)
    elif opsi == 'd' or 'bagi':
        hasil = int(nilai1) / int(nilai2)
    else:
        print('inputan salah!')
        print('masukan nilai atau opsi dengana benar!')
    print('hasilnya: ', hasil)
olah(input().split(' '))
# menjalankan fungsi olah **utama dari keseluruhan program
# dengan mengubah input kedalam list (array)
# kemudian akan di iterasi kedalam tiap variable. cek atas!

# PERDALAM! mengapa pyhton tidak mendukung switch-case
# Kunjungi!  https://s.id/py-no_switch 


