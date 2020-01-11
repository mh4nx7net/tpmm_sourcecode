# contoh penerapan array dalam pyton
arr0 = [[00+x for x in range(3)], [10 + x for x in range(3)],
        [20+x for x in range(3)]]
arr1 = [[100+x for x in range(3)], [110 + x for x in range(3)],
        [120+x for x in range(3)]]
arr2 = [[200+x for x in range(3)], [210 + x for x in range(3)],
        [220 + x for x in range(3)]]
array = [arr0, arr1, arr2]

for x in range(3):
    for y in range(3):
        for z in range(3):
            print(array[x][y][z])
    print('\n')
# FYI! perdalam dengan membaca dokumentasi
# jalankan 'pydoc -p 9999'
# kunjungi http://localhost:9999/get?key=array


