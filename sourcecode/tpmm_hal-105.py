# python tidak memiliki switch case
# seperti kebanyakan bahasa pemrograman lainnya?
# simak https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
# atau https://duckduckgo.com/?q=switch+case+in+python&t=canonical&atb=v202-5__&ia=web

switch = {
    'case1': 'coba_hasil 1',
    'case2': 'coba_hasil 2'
}
print('masukan parameter [case1|case2]\n')
# dengan nilai kunci / keys
print('hasil :', switch.get(input(), 'no keys available'))
# atau sebagai berikut
print('hasil :', switch[input()])

# benar, maka dalam penerapan
# dapat menggunakan dictionary
# ataupun if else seperti biasa



