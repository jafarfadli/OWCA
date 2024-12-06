# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Load
# Tanggal: 20 May 2024

import src.Utility as u
import src.Constant as c
import argparse
import os

# Prosedur load data yang akan dimainkan
def load() -> bool:
    # Variable Lokal
    exists : bool # True jika folder ada
    folder_name : str # folder untuk diload
    argparser : argparse.ArgumentParser # argumen parser
    args : argparse.Namespace # menampung argumen

    # Membuat Argument Parser 
    argparser = argparse.ArgumentParser()
    argparser.add_argument('nama_folder', help='nama folder tempat data program tersimpan')
    args = argparser.parse_args()
    folder_name = args.nama_folder

    # cek eksistensi folder
    exists = False
    for file in os.listdir('data'):
        if file == folder_name:
            exists = True
    if exists:    
        # mengambil data dari folder
        c.data_user = u.read_csv(f'data/{folder_name}/user.csv')
        c.data_monster = u.read_csv(f'data/{folder_name}/monster.csv')
        c.data_monster_inventory = u.read_csv(f'data/{folder_name}/monster_inventory.csv')
        c.data_item_shop = u.read_csv(f'data/{folder_name}/item_shop.csv')
        c.data_item_inventory = u.read_csv(f'data/{folder_name}/item_inventory.csv')
        c.data_monster_shop = u.read_csv(f'data/{folder_name}/monster_shop.csv')
        c.data_item = [['id','type'],['1','strength'],['2','resilience'],['3','healing'],['4','monster ball']]
        c.data_login = ['','','','','']
        return True
    else:
        print(f'\n\033[31mFolder “{folder_name}” tidak ditemukan.\033[0m\n')
        return False
    