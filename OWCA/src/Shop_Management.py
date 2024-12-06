# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Shop Management
# Tanggal: 20 May 2024

import src.Utility as u
import src.Constant as c
import os

# Prosedur shop management
def shop_management() -> None:
    # Variable Lokal
    aksi : str # aksi (lihat/tambah/ubah/hapus/keluar)
    lihat : str # lihat (monster/item)
    tambah : str # tambah (monster/item)
    ubah : str # ubah (monster/item)
    hapus : str # hapus (monster/item)
    id : str # id monster untuk diprint
    exists : bool # True jika ada item/monster untuk ditambah
    monster_id : str # id monster untuk diubah
    item_id : str # id item untuk diubah
    stok_baru : str # stok baru
    harga_baru : str # harga baru
    yakin : str # y jika hapus item/monster
    
    # print header
    print(c.shop_management_header) 
    
    # input aksi user
    while True:
        aksi = input('>>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ')
        
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
                
        # bagian tambah
        elif aksi == 'tambah':
            while True:
                tambah = input('>>> Mau nambah apa? (monster/item/kembali): ')
                if tambah == 'kembali':
                    break
                
                # bagian tambah monster
                elif tambah == 'monster':
                    exists = False
                    for j in range(1,len(c.data_monster)):
                        if c.data_monster_shop[j] == ['','','']:
                            exists = True
                    
                    if exists:
                        for i in range(len(c.data_monster)):
                            if (i > 0 and not c.data_monster[i][0] in c.data_monster_shop[i][0]) or i == 0:
                                print(f'{c.data_monster[int(i)][0]:<4}|'
                                    +f'{c.data_monster[int(i)][1]:<10}|'
                                    +f'{c.data_monster[int(i)][2]:<10}|'
                                    +f'{c.data_monster[int(i)][3]:<10}|'
                                    +f'{c.data_monster[int(i)][4]}')
                            
                        monster_id = input('\n>>> Masukkan id monster: ')
                        
                        if monster_id in [f'{j}' for j in range(1,len(c.data_monster))] and c.data_monster_shop[int(monster_id)] == ['','','']:
                            stok_baru = input('>>> Masukkan stok awal: ')
                            harga_baru = input('>>> Masukkan harga: ')
                            if u.check_int(stok_baru) and u.check_int(harga_baru):
                                c.data_monster_shop[int(monster_id)][0] = monster_id
                                c.data_monster_shop[int(monster_id)][2] = harga_baru
                                c.data_monster_shop[int(monster_id)][1] = stok_baru
                                
                                print(f'\n{c.data_monster[int(monster_id)][1]} telah berhasil ditambahkan ke dalam shop!\n')
                                break  
                            else: 
                                print('\n\033[31mstok dan harga tidak valid\033[0m\n')
                        else:
                            print('\n\033[31mid monster tidak ditemukan\033[0m\n')                                   
                    else:
                        print('\nSemua monster sudah terdapat di shop!\n') 
                
                # bagian tambah item
                elif tambah == 'item':
                    exists = False
                    for j in range(1,len(c.data_item)):
                        if c.data_item_shop[j] == ['','','','']:
                            exists = True    
                            
                    if exists:
                        for i in range(len(c.data_item)):
                            if (i > 0 and not c.data_item[i][0] in c.data_item_shop[i][0]) or i == 0:
                                print(f'{c.data_item[int(i)][0]:<4}|'
                                    +f'{c.data_item[int(i)][1]}')
                            
                        item_id = input('\n>>> Masukkan id item: ')
                        
                        if item_id in [f'{j}' for j in range(1,len(c.data_item))] and c.data_item_shop[int(item_id)] == ['','','','']:
                            stok_baru = input('>>> Masukkan stok awal: ')
                            harga_baru = input('>>> Masukkan harga: ')
                            if u.check_int(stok_baru) and u.check_int(harga_baru):
                                c.data_item_shop[int(item_id)][0] = item_id
                                c.data_item_shop[int(item_id)][2] = harga_baru
                                c.data_item_shop[int(item_id)][1] = stok_baru
                                
                                print(f'\n{c.data_item[int(item_id)][1]} telah berhasil ditambahkan ke dalam shop!\n')
                                break  
                            else: 
                                print('\n\033[31mstok atau harga tidak valid\033[0m\n')
                        else:
                            print('\n\033[31mid item tidak ditemukan\033[0m\n')
                    else:
                        print('\nSemua item sudah terdapat di shop!\n') 
                else:
                    print('\n\033[31minput tidak valid\033[0m\n')  

        # bagian ubah
        elif aksi == 'ubah':
            while True:
                ubah = input('>>> Mau ngubah apa? (monster/item/kembali): ')
                if ubah == 'kembali':
                    break
                
                # bagian ubah monster
                elif ubah == 'monster':
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
                        
                        monster_id = input('\n>>> Masukkan id monster: ')
                        
                        if monster_id in [f'{j}' for j in range(1,len(c.data_monster_shop))] and c.data_monster_shop[int(monster_id)] != ['','','']:
                            stok_baru = input('>>> Masukkan stok baru: ')
                            harga_baru = input('>>> Masukkan harga baru: ')
                            if stok_baru == '' and u.check_int(harga_baru):
                                c.data_monster_shop[int(monster_id)][2] = harga_baru
                                print(f'\n{c.data_monster[int(monster_id)][1]} telah berhasil diubah dengan harga baru {harga_baru}!\n')
                                break
                            elif u.check_int(stok_baru) and harga_baru == '':
                                c.data_monster_shop[int(monster_id)][1] = stok_baru
                                print(f'\n{c.data_monster[int(monster_id)][1]} telah berhasil diubah dengan stok baru sejumlah {stok_baru}') 
                                break
                            elif u.check_int(stok_baru) and u.check_int(harga_baru):
                                c.data_monster_shop[int(monster_id)][2] = harga_baru
                                c.data_monster_shop[int(monster_id)][1] = stok_baru
                                print(f'\n{c.data_monster[int(monster_id)][1]} telah berhasil diubah dengan stok baru sejumlah {stok_baru} dan dengan harga baru {harga_baru}!\n')
                                break 
                            else: 
                                print('\n\033[31mstok dan harga tidak valid\033[0m\n')
                        else:
                            print('\n\033[31mid monster tidak ditemukan\033[0m\n')
                    else:
                        print('\nTidak ada monster di shop!\n')  
                
                # bagian ubah item      
                elif ubah == 'item':
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
                        
                        item_id = input('\n>>> Masukkan id item: ')
                        
                        if item_id in [f'{j}' for j in range(1,len(c.data_item_shop))] and c.data_item_shop[int(item_id)] != ['','','','']:
                            stok_baru = input('>>> Masukkan stok baru: ')
                            harga_baru = input('>>> Masukkan harga baru: ')
                            if stok_baru == '' and u.check_int(harga_baru):
                                c.data_item_shop[int(item_id)][3] = harga_baru
                                print(f'\n{c.data_item_shop[int(item_id)][0]} telah berhasil diubah dengan harga baru {harga_baru}!\n')
                                break
                            elif u.check_int(stok_baru) and harga_baru == '':
                                c.data_item_shop[int(item_id)][2] = stok_baru
                                print(f'\n{c.data_item_shop[int(item_id)][0]} telah berhasil diubah dengan stok baru sejumlah {stok_baru}')
                                break
                            elif u.check_int(stok_baru) and u.check_int(harga_baru):
                                c.data_item_shop[int(item_id)][3] = harga_baru
                                c.data_item_shop[int(item_id)][2] = stok_baru
                                print(f'\n{c.data_item_shop[int(item_id)][0]} telah berhasil diubah dengan stok baru sejumlah {stok_baru} dan dengan harga baru {harga_baru}!\n')
                                break
                            else: 
                                print('\n\033[31mstok dan harga tidak valid\033[0m\n')
                        else:
                            print('\n\033[31mid item tidak ditemukan\033[0m\n')
                    else:
                        print('\nTidak ada item di shop!\n')
                else:
                    print('\n\033[31minput tidak valid\033[0m\n')  
    
        # bagian hapus            
        elif aksi == 'hapus':
            while True:
                hapus = input('>>> Mau hapus apa? (monster/item/kembali): ')
                if hapus == 'kembali':
                    break
                
                # bagian hapus monster
                elif hapus == 'monster':
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
                        
                        monster_id = input('>>> Masukkan id monster: ')
                        if monster_id in [f'{j}' for j in range(1,len(c.data_monster))] and c.data_monster_shop[int(monster_id)] != ['','','']:
                            while True:
                                yakin = input(f'>>> Apakah anda yakin ingin menghapus {c.data_monster[int(monster_id)][1]} dari shop (y/n)? ')
                                if yakin == 'y':
                                    c.data_monster_shop[int(monster_id)]=['','','']
                                    
                                    print(f'{c.data_monster[int(monster_id)][1]} telah berhasil dihapus dari shop')
                                    break
                                elif yakin == 'n':
                                    break
                                else:
                                    print('\n\033[31minput tidak valid\033[0m\n')
                        else:
                            print('\n\033[31mid monster tidak ditemukan\033[0m\n')
                    else:
                        print('\nTidak ada monster di shop!\n')
                
                # bagian hapus item
                elif hapus == 'item':
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
                        
                        item_id = input('>>> Masukkan id item: ')
                        if item_id in [f'{j}' for j in range(1,len(c.data_item))] and c.data_item_shop[int(item_id)] != ['','','','']:
                            while True:
                                yakin = input(f'>>> Apakah anda yakin ingin menghapus {c.data_item[int(item_id)][1]} dari shop (y/n)? ')
                                if yakin == 'y':
                                    c.data_item_shop[int(item_id)]=['','','','']
                                    
                                    print(f'{c.data_item[int(item_id)][1]} telah berhasil dihapus dari shop')
                                    break
                                elif yakin == 'n':
                                    break
                                else:
                                    print('\n\033[31minput tidak valid\033[0m\n')
                        else:
                            print('\n\033[31mid item tidak ditemukan\033[0m\n')
                    else:
                        print('\nTidak ada item di shop!\n')
                else:
                    print('\n\033[31minput tidak valid\033[0m\n')  
        
        # keluar             
        elif aksi == 'keluar':
            os.system('cls')
            
            print('\nDadah Mr. Yanto, sampai jumpa lagi!\n')
            break
