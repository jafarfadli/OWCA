# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Shop dan Currency
# Tanggal: 20 May 2024

import src.Utility as u
import src.Monster as m
import src.Potion as p
import src.Constant as c
import os

# Fungsi update OC untuk user
def update_oc(oc : int) -> None:
    for i in range(len(c.data_user)):
        if c.data_user[i][0] == c.data_login[0]:
            c.data_user[i][4] = str(int(c.data_user[i][4])+oc)
            break

# Prosedur shop
def shop() -> None:    
    # Variable Lokal
    aksi : str # aksi (lihat/beli/keluar)
    lihat : str # lihat (monster/item)
    beli : str # beli (monster/item)
    id : str # id monster untuk diprint
    item_id : str # id item untuk dibeli
    monster_id : str # id monster untuk dibeli
    jumlah : str # jumlah item untuk dibeli
    
    # print header
    print(c.shop_header) 
    
    # input aksi user
    while True:
        aksi = input('>>> Pilih aksi (lihat/beli/keluar): ')
        
        # bagian lihat
        if aksi == 'lihat':
            lihat = input('>>> Mau lihat apa? (monster/item): ')
            
            # bagian lihat monster
            if lihat == 'monster':
                exists = False
                for j in range(1,len(c.data_monster)):
                    if c.data_monster_shop[j] != ['','','']:
                        exists = True
                
                if exists:            
                    for i in range(len(c.data_monster_shop)):
                        if i > 0:
                            id = c.data_monster_shop[i][0]
                        else:
                            id = 0
                            
                        if id != '':
                            print(f'{c.data_monster[int(id)][0]:<4}|'
                                +f'{c.data_monster[int(id)][1]:<10}|'
                                +f'{c.data_monster[int(id)][2]:<10}|'
                                +f'{c.data_monster[int(id)][3]:<10}|'
                                +f'{c.data_monster[int(id)][4]:<10}|'
                                +f'{c.data_monster_shop[i][1]:<5}|'
                                +f'{c.data_monster_shop[i][2]}')
                else:
                    print('\nTidak ada monster di shop!\n')
            
            # bagian lihat item
            elif lihat == 'item':
                exists = False
                for j in range(1,len(c.data_item)):
                    if c.data_item_shop[j] != ['','','','']:
                        exists = True
                
                if exists:
                    for i in range(len(c.data_item_shop)):
                        if c.data_item_shop[i] != ['','','','']:
                            print(f'{c.data_item_shop[i][0]:<5}|'
                                +f'{c.data_item_shop[i][1]:<15}|'
                                +f'{c.data_item_shop[i][2]:<5}|'
                                +f'{c.data_item_shop[i][3]}')
                else:
                    print('\nTidak ada item di shop!\n')           
            else:
                print('\n\033[31minput tidak valid\033[0m\n')
                
        # bagian beli
        elif aksi == 'beli':
            print(f'Jumlah O.W.C.A. Coin-mu sekarang {c.data_login[4]}.\n')
            while True:
                beli = input('>>> Mau beli apa? (monster/item/kembali): ')
                if beli == 'kembali':
                    break
                
                # bagian beli monster
                elif beli == 'monster':
                    exists = False
                    for j in range(1,len(c.data_monster)):
                        if c.data_monster_shop[j] != ['','','']:
                            exists = True
                    
                    if exists: 
                        monster_id = input('Masukkan id monster: ')
                        if monster_id in [f'{j}' for j in range(1,len(c.data_monster))] and c.data_monster_shop[int(monster_id)] != ['','','']:
                            if c.data_monster_shop[int(monster_id)][1] == '0':
                                print(f'\nStok monster {c.data_monster[int(monster_id)][1]} habis! Pembelian dibatalkan.\n')
                            elif m.read_monster(c.data_login[0],monster_id) != '0':
                                print(f'\nMonster {c.data_monster[int(monster_id)][1]} sudah ada dalam inventory-mu! Pembelian dibatalkan.\n')   
                            elif int(c.data_login[4]) < int(c.data_monster_shop[int(monster_id)][2]):
                                print(f'\nOC-mu tidak cukup.\n')                 
                            else:
                                print(f'Berhasil membeli item: {c.data_monster[int(monster_id)][1]}. Item sudah masuk ke inventory-mu!')
                                
                                update_oc(-int(c.data_monster_shop[int(monster_id)][2]))
                                
                                c.data_monster_shop[int(monster_id)][1] = str(int(c.data_monster_shop[int(monster_id)][1])-1)
                                c.data_monster_inventory += [[c.data_login[0],monster_id,'1']]
                                break
                        else:
                            print('\n\033[31mid monster tidak ditemukan\033[0m\n')
                    else:
                        print('\nTidak ada monster di shop!\n') 
                        
                # bagian beli item        
                elif beli == 'item':
                    exists = False
                    for j in range(1,len(c.data_item)):
                        if c.data_item_shop[j] != ['','','','']:
                            exists = True
                            
                    if exists:
                        item_id = input('>>> Masukkan id item: ')
                        jumlah = input('>>> Masukkan jumlah: ')
                        if item_id in [f'{j}' for j in range(1,len(c.data_item_shop))] and c.data_item_shop[int(item_id)] != ['','','',''] and u.check_int(jumlah):
                            if int(c.data_item_shop[int(item_id)][2]) < int(jumlah) or c.data_item_shop[int(item_id)][2] == '0':
                                print(f'\nStok potion {c.data_item_shop[int(item_id)][0]} tidak cukup! Pembelian dibatalkan.\n')  
                            elif int(c.data_login[4]) < int(jumlah)*int(c.data_item_shop[int(item_id)][3]):
                                print(f'\nOC-mu tidak cukup.\n')                 
                            else:
                                print(f'Berhasil membeli item: {jumlah} {c.data_item_shop[int(item_id)][1]}. Item sudah masuk ke inventory-mu!')
                                
                                update_oc(-int(jumlah)*int(c.data_item_shop[int(item_id)][3]))
                                
                                c.data_item_shop[int(item_id)][2] = str(int(c.data_item_shop[int(item_id)][2])-int(jumlah))
                                p.update_potion(c.data_login[0],c.data_item_shop[int(item_id)][1],int(jumlah))
                        else:
                            print('\n\033[31mid item tidak ditemukan\033[0m\n')
                    else:
                        print('\nTidak ada item di shop!\n')
                else:
                    print('\n\033[31minput tidak valid\033[0m\n')  
                            
        # keluar
        elif aksi == 'keluar':
            os.system('cls')
            
            print('\nMr. Yanto bilang makasih, belanja lagi ya nanti :)\n')
            break         