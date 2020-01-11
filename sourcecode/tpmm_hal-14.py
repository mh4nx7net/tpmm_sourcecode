import random

class nilaiSiswa:
    # fungsi init untuk class nilaiSiswa
    def __init__(self, jumlah_siswa):
        self.daftar_nilai = list()
        # membuat daftar nilai untuk masing2 siswa
        while len(self.daftar_nilai) <= jumlah_siswa:
            # menambahkan nilai acak dengan kisaran 50 hingga 100
            self.daftar_nilai.append(random.randrange(50, 100))

    # generate output kedalam list
    # iterable output.
    def __iter__(self):
        return list(iter(self.daftar_nilai))

    # representasi output untuk --> callable kelas nilaiSiswa
    def __repr__(self):
        return str(list(self.daftar_nilai))

# generate nilai pada tiap kelas
kelasA = nilaiSiswa(5).__iter__()
kelasB = nilaiSiswa(5).__iter__()

def menentukan_kelulusan(nama_kelas):
    # fungsi utama untuk menentukan kelulusan
    for nilai in nama_kelas:
        if nilai >= 65:
            print(nilai, '==> lulus')
        else:
            print(nilai, '==> tidak lulus')

# penentuan nilai tiap kelas
print('daftar nilai KelasA: ')
menentukan_kelulusan(kelasA)

