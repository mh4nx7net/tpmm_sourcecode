import random

# list nama mahasiswa
nama_mahasiswa = ['jeriko', 'sandiko', 'azis', 'mario', 'fajar']
# generate nilai_mahasiswa
nilai_mahasiswa = [random.randrange(50, 100) for x in range(5)]
# zip nama dan nilai
kelas_IT = dict(zip(nama_mahasiswa, nilai_mahasiswa))


def menentukan_kelulusan(nama_kelas):
    # fungsi untuk menentukan kelulusan
    for i, nilai in enumerate(nama_kelas.values()):
        if nilai >= 70:
            print('{}\t{}\t{}'.format(
                list(nama_kelas.keys())[i], nilai, 'lulus'))
        else:
            print('{}\t{}\t{}'.format(
                list(nama_kelas.keys())[i], nilai, 'tidak lulus'))


print('daftar absen dan nilai: \n\n', kelas_IT)
print('\nnama\tnilai\tketerangan')
# menjalankan fungsi menentukan_kelas
menentukan_kelulusan(kelas_IT)


