# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Register
# Tanggal: 20 May 2024

import src.Constant as c
import os

# Prosedur untuk mendaftar akun baru pada game
def register() -> None:
    # Variable Lokal
    user_id : str # id user baru
    username : str # username baru
    password : str # password
    success : bool # True jika username valid
    list_monster : list[str] # list monster yang bisa menjadi monster awal
    monster_id : str # id monster awal 
    
    # Memeriksa status login user
    if c.data_login != ['','','','','']:
        print(f'Register gagal!\nAnda telah login dengan username {c.data_login[1]}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.')
    else: # User belum login, memasukkan data user baru
        user_id = str(int(c.data_user[-1][0])+1)
        
        username = input('Masukan username: ')
        while username == '' or username == " ":
            print("Username tidak boleh kosong!")
            username = input('Masukan username: ')

        password = input('Masukan password: ')
        while password == '' or password == " ":
            print("Password tidak boleh kosong!")
            password = input('Masukan username: ')
        
        success = True
        
        # Memeriksa kesesuaian karakter dalam username
        for char in username:
            if not char in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_-':
                print('\n\033[31mUsername hanya boleh berisi alfabet, angka, underscore, dan strip!\033[0m')
                success = False
                break

        # Memeriksa ketersediaan username
        if success:
            for row in c.data_user:
                if row[1] == username:
                    print(f'\n\033[31mUsername {username} sudah terpakai, silahkan gunakan username lain!\033[0m')
                    success = False
                    break
        
        # Menambahkan data user ke dalam file csv, user login
        if success:
            c.data_user += [[user_id,username,password,'agent',0]]
            c.data_login = c.data_user[-1]
            
            # User memilih monster
            print('''
Silahkan pilih salah satu monster sebagai monster awalmu.

1. Pikachow
2. Bulbu
3. Zeze
4. Zuko
5. Chacha
''')
            
            list_monster = ['Pikachow','Bulbu','Zeze','Zuko','Chacha']
            while True:
                monster_id = input('Monster pilihanmu: ')
                if not monster_id in ['1','2','3','4','5']:
                    print('\n\033[31mPilihan nomor tidak tersedia!\033[0m\n')
                else: # Menambahkan data monster user
                    os.system('cls')
                    
                    c.data_monster_inventory += [[user_id,monster_id,'1']]
                    
                    # User berhasil mendaftar
                    print(f'''
Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {list_monster[int(monster_id)-1]}!
Ketik "help" untuk melihat daftar command yang dapat dilakukan.
''')
                    break
        

