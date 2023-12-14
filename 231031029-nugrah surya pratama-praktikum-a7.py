pw_benar = 'anggaz'
percobaan = 3
a = True 
while a:
    masukan = input('masukkan password: ')
    if masukan == pw_benar:
        print('selamat anda login!')
        a = False
    else:
        if percobaan == 0:
            print('password yang anda masukkan salah! akun anda di banned')
            a = False
        else:
            print('password anda salah! silahkan coba lagi dengan sisa percobaan: ', percobaan)
            percobaan -= 1