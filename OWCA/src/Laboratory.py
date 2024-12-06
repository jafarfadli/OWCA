# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Laboratory
# Tanggal: 20 May 2024

import src.Utility as u
import src.Monster as m
import src.Shop_Currency as sc
import src.Constant as c
import os

# Prosedur laboratory
def laboratory() -> None:
    # Variable Lokal
    list_harga : list[int] # list harga upgrade
    list_monster : list[str] # list data monster dan level
    id : str # id monster untuk diupgrade
    lanjutkan : str # y jika melanjutkan upgrade
    
    list_harga = [300,500,800,1000]
    
    # print header
    print(c.lab_header)
    
    # print monster yang dimiliki user
    while True:
        print('============> INVENTORY LIST <============')
        
        list_monster = []
        
        num = 1
        for i in range(len(c.data_monster_inventory)):
            if c.data_monster_inventory[i][0] == c.data_login[0]:
                index_monster = int(c.data_monster_inventory[i][1])
                
                print(f'{num}. {c.data_monster[index_monster][1]} (Lvl: {c.data_monster_inventory[i][2]})')
                list_monster += [[c.data_monster_inventory[i][2],c.data_monster[index_monster][1],c.data_monster[index_monster][2],c.data_monster[index_monster][3],c.data_monster[index_monster][4]]]
                
                num += 1
        print(f'''
============>>> UPGRADE PRICE <<<============
              
Jumlah O.W.C.A. Coin-mu sekarang adalah {c.data_login[4]}
1. Level 1 -> Level 2: 300 OC
2. Level 2 -> Level 3: 500 OC
3. Level 3 -> Level 4: 800 OC
4. Level 4 -> Level 5: 1000 OC''')

        # input id monster untuk diupgrade
        id = input(''' 
Pilih ID monster yang ingin diupgrade! 
Jika ingin keluar dari Lab Dokter Asep, ketik command "exit"

>>> ''')
        if id == 'exit':
            os.system('cls')
            break
        
        # jika pilihan nomor ID tidak tersedia
        elif not u.check_int(id) or not int(id) in range(1,num):
            os.system('cls')
            print('\n\033[31mPilihan ID tidak tersedia!\033[0m\n')
            
        # jika level monster sudah maksimum
        elif list_monster[int(id)-1][0] == '5':
            os.system('cls')
            print('\n\033[31mMaaf, monster yang Anda pilih sudah memiliki level maksimum!\033[0m\n')
        else:
            os.system('cls')
            print(f'''
{list_monster[int(id)-1][1]} akan di-upgrade ke level {int(list_monster[int(id)-1][0])+1}.
Harga untuk melakukan upgrade {list_monster[int(id)-1][1]} adalah {list_harga[int(list_monster[int(id)-1][0])-1]} OC.
''')
            lanjutkan = input(f'Lanjutkan upgrade (OC: {c.data_login[4]}) (y/n): ')
            while True:
                if lanjutkan == 'y':
                    if int(c.data_login[4]) < list_harga[int(list_monster[int(id)-1][0])-1]:
                        print(f'\nMohon maaf, OC-mu tidak cukup.\n')
                        break
                    else:
                        for i in range(len(c.data_monster)):
                            if c.data_monster[i][1] == list_monster[int(id)-1][1]:
                                monster_id = c.data_monster[i][0]
                        
                        m.update_monster(c.data_login[0],monster_id,1)
                        sc.update_oc(-list_harga[int(list_monster[int(id)-1][0])-1])
                        
                        print(f'\nSelamat, {list_monster[int(id)-1][1]} berhasil di-upgrade ke level {int(list_monster[int(id)-1][0])+1} !\n')
                        break
                elif lanjutkan == 'n':
                    os.system('cls')
                    
                    break
                else:
                    print('\n\033[31minput tidak valid\033[0m\n')  
            