print('Masukan nilai maka saya akan mengujinya\n 60 <= E, 70 <= D, 80 <= C, 90 <= B, 100 <= A')
nilai = int(input())
grade = str()
if nilai <= 60:
    grade = 'E'
elif nilai <= 70:
    grade = 'D'
elif nilai <= 80:
    grade = 'C'
elif nilai <= 90:
    grade = 'B'
elif nilai <= 100:
    grade = 'A'
else:
    grade = 'Masukan data dengan benar!'
print('Grade dan Nilai anda adalah {}-> {}'.format(grade, nilai))
# FYI! perdalam dengan membaca dokumentasi
# jalankan 'pydoc -p 9999'
# kunjungi 'http://localhost:9999/topic?key=EXPRESSIONS'



