# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Menu dan Help
# Tanggal: 20 May 2024

import src.Constant as c

# Prosedur menampilkan command yang valid untuk user
def help() -> None: 
    # jika user belum login
    if c.data_login == ['','','','','']:
        print(c.help_header)
        print('''
Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.

1. login: Masuk ke dalam akun yang sudah terdaftar
2. register: Membuat akun baru
3. exit: Keluar

Footnote: 
Untuk melanjutkan game, silahkan ketik command yang terdaftar.
Jangan lupa untuk memasukkan input yang valid!
''')
        
    # jika user login sebagai agent
    elif c.data_login[3] == 'agent':
        print(c.help_header)
        print(f'''
Halo Agent {c.data_login[1]}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:

1. w            : Bergerak ke atas
2. s            : Bergerak ke bawah
3. d            : Bergerak ke kanan
4. a            : Bergerak ke kiri
5. logout       : Keluar dari akun yang sedang digunakan
6. monster      : Melihat owca-dex
7. inventory    : Melihat inventory
8. battle       : Melawan monster secara random
9. arena        : Melawan lima monster dengan level 1-5
10. shop        : Melihat dan membeli item/monster
11. laboratory  : Menaikkan level monster
12. jackpot     : Main slot

Footnote: 
Untuk melanjutkan game, silahkan ketik command yang terdaftar.
Jangan lupa untuk memasukkan input yang valid!
''')
        
    # jika user login sebagai admin
    elif c.data_login[3] == 'admin':
        print(c.help_header)
        print('''
Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:

1. logout   : Keluar dari akun yang sedang digunakan
2. shop     : Melakukan manajemen pada shop
3. monster  : Melakukan manajemen pada database monster

Footnote: 
Untuk melanjutkan game, silahkan ketik command yang terdaftar.
Jangan lupa untuk memasukkan input yang valid!
''')
        
        
    
