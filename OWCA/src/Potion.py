# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Potion
# Tanggal: 20 May 2024   

import src.Constant as c

# Fungsi membaca kuantitas potion/item untuk user
def read_potion(id : str,type_potion : str) -> str:
    for row in c.data_item_inventory:
        if row[0] == id and row[1] == type_potion:
            return row[2]
    return '0'

# Fungsi update kuantitas potion/item untuk user
def update_potion(id : str,type_potion : str,change_qty : int) -> None:
    if read_potion(id,type_potion) != '0':
        for i in range(len(c.data_item_inventory)):
            if c.data_item_inventory[i][0] == id and c.data_item_inventory[i][1] == type_potion:
                c.data_item_inventory[i][2] = str(int(c.data_item_inventory[i][2])+change_qty)
                if read_potion(id,type_potion) == '0':
                    c.data_item_inventory.pop(i)
         
    else:
        c.data_item_inventory += [[id,type_potion,str(change_qty)]]
