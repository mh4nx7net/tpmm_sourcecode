# dalam python tidak benar benar membutuhkan pointers
# untuk melakukan check penempatan memory
# dapat menggunakan builtins module python 'id'
print('masukan nilai angka:')
angka = int(input())
print('tampilkan id angka:', id(angka))
pointer = angka
print(
    'pointer\t:{} -> id:{}\nangka\t:{} -> id:{}'
    .format(pointer, id(pointer), angka, id(angka))
)
# FYI!. Selengkapnya baca 'cPython'



