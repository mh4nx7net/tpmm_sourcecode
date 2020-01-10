nilai = list()

# mendapatkan nilai hingga 5kali
print('dapatkan data hingga 5kali')
for i in range(5):
    nilai.append(input())

# menampilkan nilai hingga list habis
print('tampilkan data sesuai urut nilai')
for i, x in enumerate(nilai):
    print('num{} -> nilai{}'.format(i, x))

# menampilkan seluruh data
print('seluruh data: ', nilai)
