# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Monster
# Tanggal: 20 May 2024

import src.Constant as c

# Fungsi menampilkan OWCA DEX yang dimiliki user
def monster() -> None:    
    # Variable Lokal
    index_monster : int # index monster untuk diprint
    list_monster : list[str] # list data monster dan level untuk diprint
    
    print(c.owcadex_header)
    
    print('============ OWCA DEX ============')
    for i in range(len(c.data_monster_inventory)):           
        if (c.data_monster_inventory[i][0] == c.data_login[0]) or i == 0:
            if i == 0:
                index_monster = 0
            else:
                index_monster = int(c.data_monster_inventory[i][1])
                
            list_monster = [c.data_monster[index_monster][0],c.data_monster[index_monster][1],c.data_monster[index_monster][2],c.data_monster[index_monster][3],c.data_monster[index_monster][4],c.data_monster_inventory[i][2]]
            
            if i != 0 and int(list_monster[-1])>1:
                for j in range(2,5):
                    list_monster[j] = str(int(int(list_monster[j])*(int(list_monster[-1])-1)*0.1+int(list_monster[j])))
                
            print(f'{list_monster[0]:<4}|'
                +f'{list_monster[1]:<10}|'
                +f'{list_monster[2]:<10}|'
                +f'{list_monster[3]:<10}|'
                +f'{list_monster[4]:<10}|'
                +f'{list_monster[5]:<5}')

# fungsi membaca level monster untuk user
def read_monster(id : str,monster_id : str) -> str:
    for row in c.data_monster_inventory:
        if row[0] == id and row[1] == monster_id:
            return row[2]
    return '0'

# fungsi update level monster untuk user
def update_monster(id : str,monster_id : str,change_lvl : int) -> None:
    if read_monster(id,monster_id) != '0':
        for i in range(len(c.data_monster_inventory)):
            if c.data_monster_inventory[i][0] == id and c.data_monster_inventory[i][1] == monster_id:
                c.data_monster_inventory[i][2] = str(int(c.data_monster_inventory[i][2])+change_lvl)
                
    else:
        c.data_monster_inventory += [[id,monster_id,str(change_lvl)]]