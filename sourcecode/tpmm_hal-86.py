# mendapatkan nilai
nama_X = input()
tahun_lahir = int(input())
tahun_ini = int(input())
tinggi_badan = int(input())
berat_badan = int(input())
# mengolah nilai
umur = tahun_ini - tahun_lahir
bmi = berat_badan / tinggi_badan
# menampilkan nilai
print('nama : {}\numur : {}\n bmi : {}'.format(nama_X, umur, bmi))
