# a = True

# while a:
#     jawab = input('Apakah kamu mau jadi pacarku? (iya/tidak)')
#     if jawab =='iya':
#         print('kita pacaran!')
#         a = False
#     elif jawab =='tidak':
#          print('Kita cuman teman:D')
#          a = False
#     else:
#         print('Maaf gak kenal:.)')
#         a = True

a = True  # Menginisialisasi variabel a sebagai True untuk mengawali perulangan

while a:  # Memulai loop while yang akan berjalan selama variabel a bernilai True
    jawab = input('Apakah kamu mau jadi pacarku? (iya/tidak)')  # Meminta input dari pengguna
    
    if jawab == 'iya':  # Memeriksa jika jawaban yang dimasukkan adalah 'iya'
        print('kita pacaran!')  # Cetak pesan bahwa mereka akan pacaran
        a = False  # Ubah nilai a menjadi False untuk menghentikan loop
    
    elif jawab == 'tidak':  # Memeriksa jika jawaban yang dimasukkan adalah 'tidak'
        print('Kita cuman teman:D')  # Cetak pesan bahwa mereka hanya akan menjadi teman
        a = False  # Ubah nilai a menjadi False untuk menghentikan loop
    
    else:  # Blok ini dijalankan jika jawaban tidak cocok dengan 'iya' atau 'tidak'
        print('Maaf gak kenal:.)')  # Cetak pesan bahwa jawaban tidak dikenali
        # Jangan ubah nilai 'a' agar program tetap berjalan jika jawaban tidak sesuai 'iya' atau 'tidak'