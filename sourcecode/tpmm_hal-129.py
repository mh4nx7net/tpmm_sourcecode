a = 1
# jika a < 100 -> jalankan
# ## tiap lembar(a) seharga (a kelipatan 80)
# ## dapat dituliskan harga=a*80
while a <= 100:
    b = a*80
    print('{} Lembar -> Rp.{}'.format(a, b))
    a += 1
# else: a=100 -> end
