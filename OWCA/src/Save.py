# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Save
# Tanggal: 20 May 2024

import src.Utility as u
import src.Constant as c
import os

# Prosedur save
def save() -> None:
    # Variable Lokal
    folder_name : str # nama folder untuk save
    folder_baru : bool # True jika membuat folder baru
    
    # input nama folder
    folder_name = input('\nMasukkan nama folder: ')
    
    try:
        # membuat folder baru
        os.makedirs(f'data/{folder_name}')
        folder_baru = True
    except:
        folder_baru = False
    
    # jika membuat folder baru
    if folder_baru:
        print(f'''
              
Saving...

Membuat folder data...
Membuat folder data/{folder_name}...
Berhasil menyimpan data di folder data/{folder_name}!''')
        
    else:
        print(f'''
Saving...

Berhasil menyimpan data di folder data/{folder_name}!''')
    
    # menulis ulang csv
    u.write_csv(f'data/{folder_name}/user.csv',c.data_user)
    u.write_csv(f'data/{folder_name}/monster.csv',c.data_monster)
    u.write_csv(f'data/{folder_name}/monster_inventory.csv',c.data_monster_inventory)
    u.write_csv(f'data/{folder_name}/item_shop.csv',c.data_item_shop)
    u.write_csv(f'data/{folder_name}/item_inventory.csv',c.data_item_inventory)
    u.write_csv(f'data/{folder_name}/monster_shop.csv',c.data_monster_shop)
