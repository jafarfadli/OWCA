# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Monster Management
# Tanggal: 20 May 2024

import src.Utility as u
import src.Constant as c
import os

# Prosedur monster management
def monster_management() -> None:
    # Vriable Lokal
    aksi : str # aksi (1/2/3)
    success : bool # True jika nama monster baru valid
    nama : str # nama monster baru
    attack : str # attack monster baru
    defense : str # defense monster baru
    hp : str # hp monster baru
    tambahkan : str # y jika tambah monster
    
    # print header
    print(c.monster_header)
    
    # input aksi user
    while True:
        aksi = input('Pilih aksi: ')
        
        if aksi not in ['1','2','3']:
            print('\n\033[31mPilihan nomor tidak tersedia!\033[0m\n')
        
        # bagian tampilkan monster
        elif aksi == '1':
            for i in range(len(c.data_monster)):
                print(f'{c.data_monster[i][0]}' + (5-len(c.data_monster[i][0]))*' '+'|'
                    +f'{c.data_monster[i][1]}' + (20-len(c.data_monster[i][1]))*' '+'|'
                    +f'{c.data_monster[i][2]}' + (15-len(c.data_monster[i][2]))*' '+'|'
                    +f'{c.data_monster[i][3]}' + (15-len(c.data_monster[i][3]))*' '+'|'
                    +f'{c.data_monster[i][4]}')
        
        # bagian tambah monster
        elif aksi == '2':
            print('\nMemulai pembuatan monster baru\n')
            
            while True:
                success = True
                nama = input('Masukkan Type/Nama : ')
                for row in c.data_monster:
                    if row[1] == nama:
                        print('\033[31mNama sudah terdaftar, coba lagi!\033[0m')
                        success = False
                if success:
                    break
                
            while True:
                attack = input('Masukkan ATK Power : ')
                if u.check_int(attack):
                    break
                else:
                    print('\033[31mMasukkan input bertipe Integer, coba lagi!\033[0m')
                    
            while True:
                defense = input('Masukkan DEF Power (0-50) : ')
                if u.check_int(defense) and 0<=int(defense)<=50:
                    break
                else:
                    print('\033[31mDEF Power harus bernilai 0-50, coba lagi!\033[0m')
                    
            while True:
                hp = input('Masukkan HP : ')
                if u.check_int(hp):
                    break
                else:
                    print('\033[31mMasukkan input bertipe Integer, coba lagi!\033[0m')
                    
            print(f'''
Monster baru berhasil dibuat!
Type : {nama}
ATK Power : {attack}
DEF Power : {defense}
HP : {hp}
''')
            while True:
                tambahkan = input('Tambahkan Monster ke database (y/n) : ')
                if tambahkan == 'y':
                    id = str(len(c.data_monster))
                    
                    c.data_monster += [[id,nama,attack,defense,hp]]
                    c.data_monster_shop += [['','','']]
                    
                    print('\nMonster baru telah ditambahkan!\n')
                    break
                elif tambahkan == 'n':
                    break
                else:
                    print('\n\033[31minput tidak valid\033[0m\n')  
            
        # keluar
        elif aksi == '3':
            os.system('cls')
            break            