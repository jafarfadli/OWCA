# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Inventory
# Tanggal: 20 May 2024

import src.Utility as u
import src.Constant as c
import os

# Prosedur melihat inventory untuk user
def inventory() -> None:
    # Variable Lokal
    list_inventory : list[list[str]] # list item dan monster di inventory
    monster_id : int # id monster di inventory
    num : int # id item/monster di inventory
    id : str # id yang ingin ditampilkan secara detail
    
    # print header
    print(c.inventory_header)
    
    # print monster dan item list
    while True:
        print(f'''
============ User ID: {c.data_login[0]} ============
Jumlah O.W.C.A. Coin-mu sekarang adalah {c.data_login[4]} OC''')
        
        list_inventory = []
        
        num = 1
        for i in range(len(c.data_monster_inventory)):
            if c.data_monster_inventory[i][0] == c.data_login[0]:
                monster_id = int(c.data_monster_inventory[i][1])
                list_inventory += [['monster',c.data_monster[monster_id][1],c.data_monster[monster_id][2],c.data_monster[monster_id][3],c.data_monster[monster_id][4],c.data_monster_inventory[i][2]]]
                
                if int(list_inventory[-1][5])>1:
                    for j in range(2,5):
                        list_inventory[-1][j] = str(int(int(list_inventory[-1][j])*(int(list_inventory[-1][5])-1)*0.1+int(list_inventory[-1][j])))
                        
                print(f'{num}. Monster      (Name: {list_inventory[-1][1]}, Lvl: {list_inventory[-1][5]}, HP: {list_inventory[-1][4]})')
                
                num += 1
                
        for j in range(len(c.data_item_inventory)):
            if c.data_item_inventory[j][0] == c.data_login[0]:
                if c.data_item_inventory[j][1] != 'monster ball':
                    print(f'{num}. Potion       (Type: {c.data_item_inventory[j][1]}, Qty: {c.data_item_inventory[j][2]})')
                    list_inventory += [['potion',c.data_item_inventory[j][1],c.data_item_inventory[j][2]]]
                else:
                    print(f'{num}. Monster Ball (Qty: {c.data_item_inventory[j][2]})')
                    list_inventory += [['monster ball',c.data_item_inventory[j][2]]]
                num += 1
            

    # bagian menampilkan detail item atau monster
        id = input('''
Ketikkan nomor ID untuk menampilkan detail item
Jika ingin keluar dari Inventory, ketik command "exit". 

>>> ''')
        if id == 'exit':
            os.system('cls')
            
            break
        elif not u.check_int(id) or not int(id) in range(1,num):
            os.system('cls')
            print('\n\033[31mPilihan nomor tidak tersedia!\033[0m\n')

        else:
            if list_inventory[int(id)-1][0] == 'monster':
                os.system('cls')
                print(f'''
Monster
Name      : {list_inventory[int(id)-1][1]}
ATK Power : {list_inventory[int(id)-1][2]}
DEF Power : {list_inventory[int(id)-1][3]}
HP        : {list_inventory[int(id)-1][4]}
Level     : {list_inventory[int(id)-1][5]}
''')

            elif list_inventory[int(id)-1][0] == 'potion':
                os.system('cls')
                print(f'''
Potion
Type      : {list_inventory[int(id)-1][1]}
Quantity  : {list_inventory[int(id)-1][2]}
''')

            elif list_inventory[int(id)-1][0] == 'monster ball':
                os.system('cls')
                print(f'''
Monster Ball
Quantity  : {list_inventory[int(id)-1][2]}
''')


     
        
