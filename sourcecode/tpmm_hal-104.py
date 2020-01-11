print('welcome admin')
print('buat nomor baru: ')

# mendapatkaan nilai baru
new_number = input()
print('buat password baru: ')
new_password = input()
print('terimakasih, akun telah terbuat.\n\n nomor\t\t: {}\n password\t: {},\n\n'.format(
    new_number, new_password))

# program untuk validasi nilai
# mendapatkan validasi nilai
print('masukan password: ')
password = input()

# mendiskusikan rentang nilai
# dengan nested ifelse
if password == new_password:
    print('masukan nomor admin: ')
    number = input()
    if number == new_number:
        print('selamat datang admin', number)
    else:
        print('masukan dengan benar!')



