# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Jackpot
# Tanggal: 20 May 2024

import src.Shop_Currency as sc
import src.Random_Number_Generator as rng
import src.Constant as c
import os

# Prosedur bermain jackpot
def jackpot() -> None:
    # Variable Lokal
    list_item : list[str] # list item
    list_value : list[int] # list nilai item
    list_monster : list[int] # list monster milik agent
    item1 : int # item 1
    item2 : int # item 2
    item3 : int # item 3
    reward : int # hadiah
    
    list_item = ['Topi','Pedang','Koin','Potion','Monster']
    list_value = [50,100,150,200,250]
    
    # print header
    print(c.jackpot_header)
    
    # mulai bermain
    while True:
        mulai = input('\n>> Mulai bermain (y/n): ')
        if mulai == 'n':
            os.system('cls')
            break
        elif mulai == 'y':
            
            # jika OC tidak cukup
            if int(c.data_login[4]) < 400:
                print('\nMaaf, anda tidak memiliki cukup OC untuk bermain JACKPOT.')
            else:
                os.system('cls')
                
                sc.update_oc(-400)

                item1 = rng.lcg_x(10)%5
                item2 = rng.lcg_x(15)%5
                item3 = rng.lcg_x(20)%5
                
                print(f'''\nAnda Mendapatkan: \n
\033[33m
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$    \033[32m{list_item[item1]:<7}\033[33m|\033[32m{list_item[item2]:<7}\033[33m|\033[32m{list_item[item3]:<7}\033[33m    $$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\033[0m
''')
                
                # bagian mendapat jackpot
                if item1 == item2 == item3:
                    list_monster = []
                    for j in range(len(c.data_monster_inventory)):
                        if c.data_monster_inventory[j][0] == c.data_login[0]:
                            list_monster += [int(c.data_monster_inventory[j][1])]
                    
                    if len(list_monster) == len(c.data_monster)-1:
                        print('\nJACKPOT!!! Selamat, Anda mendapatkan 5000 OC\n')
                        
                        sc.update_oc(5000)
                    else:
                        while True:
                            monster_id = rng.lcg_x(10)%(len(c.data_monster)-1) +1
                            if not monster_id in list_monster:
                                c.data_monster_inventory += [[c.data_login[0],str(monster_id),'1']]
                                
                                print(f'\nJACKPOT!!! Selamat, Anda mendapatkan monster {c.data_monster[monster_id][1]}.\n')
                                break
                
                # bagian tidak mendapat jackpot
                else:
                    reward = list_value[item1]+list_value[item2]+list_value[item3]
                    sc.update_oc(reward)
                    
                    print(f'\nO.W.C.A. Coin sebanyak {reward} OC telah ditambahkan ke akun Anda!\n')
        else:
            print('\n\033[31minput tidak valid\033[0m\n')                