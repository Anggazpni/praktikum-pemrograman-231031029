nama   = 'nugrah surya pratama'
nim    = '231031029'
meet   = 'praktikum 3'
prodi  = 'sistem informasi A'
email  = 'nugrahpratama111@gmail.com'
TTL    = 'parepare, 01 november 2005'
Alamat = 'jalan andi mappangara'
asal   = 'parepare'
hobi   = 'badminton'
tinggi = '170 cm'

sp = 40
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.capitalize().rjust(sp))
print(prodi.title().rjust(sp))
print(email.rjust(sp))
print('-'*sp)

print(f'''Halo, nama saya {nama.title()} dengan nim {nim.title()} dari prodi {prodi.title()}, ini adalah file {meet.title()}. Terima kasih.
      ''')

print(f'''Biodata saya
Nama  \t: {nama.title()}
Nim   \t: {nim}
prodi \t: {prodi.title()}
TTL   \t: {TTL.title()}
Alamat\t: {Alamat.title()}
Asal  \t: {asal.capitalize()}
hobi  \t: {hobi.title()}
tinggi\t: {tinggi}
      ''')

stat = 'sir issac newton frankel'
up   = stat.upper()
print(up)
up = up.split() 
print(up)
print(up[-1][0],' '.join(up[0:-1]))
print('F SIR ISSAC NEWTON')

print(up[-1],up[0][0],up[1][0])
print('NEWTON S I')

print()

stat2 = '&sir$ @issac# *newton.'
up2   = stat2.upper()
print(up2)
up2   = up2.split()
print(up2)
print(up2[0][1:-1],up2[1][1:-1],up2[2][1:-1])
print(up2[0].strip('&$'),up2[1].strip('@#'),up2[2].strip('*.'))
print('SIR ISSAC NEWTON')  




