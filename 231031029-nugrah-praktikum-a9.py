def judul():
    print("program menghitung luas dan keliling".upper().center(80, "-"))
    print("bangun datar persegi\n".upper().center(80))
def hitung(p,l):
    luas = p * l
    kel = (p+l) * 2
    return luas, kel
def tampil(pesan, nilai):
    print(f'Hasil perhitungan Nilai {pesan}: {nilai}')
def pilihan():
    lanjut = input("lanjut?: ")
    if lanjut == "y":
        a = True
    else:
        print("sampai jumpa")
        a = False
    return a 
a = True
while a:
    judul()
    panjang = float(input("Masukkan Panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas, kel= hitung(panjang, lebar)
    tampil("luas", luas)
    tampil("keliling", kel)
    a = pilihan()