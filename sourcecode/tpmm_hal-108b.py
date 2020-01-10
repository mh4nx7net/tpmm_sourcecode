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

    # fungsi untuk tiap tiap operator
    # fungsi akan dijalankan sesuai opsi yang digunakan
    def tambah():
        hasil = int(nilai1) + int(nilai2)
        return hasil

    def kurang():
        hasil = int(nilai1) - int(nilai2)
        return hasil

    def kali():
        hasil = int(nilai1) * int(nilai2)
        return hasil

    def bagi():
        hasil = int(nilai1) / int(nilai2)
        return hasil

    # alternative switch-case pada python
    # dengan menggunakan dict
    switcher = {'a': tambah(),
                'b': kurang(),
                'c': kali(),
                'd': bagi(),
                'tambah': tambah(),
                'kurang': kurang(),
                'kali': kali(),
                'bagi': bagi()
                }
    print('hasilnya: ', switcher.get(opsi, 'tidak ditemukan'))
    # FYI!. struktur dict berupa dict_n = {ini_keys: ini_val}
    # maka pada dasarnya untuk pemanggilan value
    # cukup menuliskan kunci/keys
    # Ex: dict_n[ini_keys] atau dict_n.get(ini_kunci,'pesan jika tidak ditemukan')


olah(input().split(' '))
# menjalankan fungsi olah **utama dari keseluruhan program
# dengan mengubah input kedalam list (array)
# kemudian akan di iterasi kedalam tiap variable. cek atas!

# PERDALAM! penggunaan dict lebih lanjut,lakukan uji laborat!
# buatlah dua variable dengan nilai yang sama.
# lakukan cek id(nama variable) maka tertampil id yang sama
# seperti itulah dictionary pada python bekerja, simpulkan!
