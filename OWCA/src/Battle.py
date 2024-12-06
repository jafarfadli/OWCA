# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Battle
# Tanggal: 20 May 2024

import src.Utility as u
import src.Random_Number_Generator as rng
import src.Potion as p
import src.Shop_Currency as sc
import src.Constant as c
import os

# Prosedur battle
def battle() -> None:
    # Variable Lokal
    data_monster_agent : list[list[str]] # data monster agent
    data_monster_musuh : list[list[str]] # data monster musuh
    list_monster : list[str] # list monster agent
    id_musuh : int # id monster untuk musuh
    monster_id : int # id monster untuk agent
    stats_musuh : list[str] # stats musuh
    stats_agent : list[str] # stats agent
    lvl_agent : str # level monster agent
    hp_terakhir : str # sisa hp setiap turn
    attack_result : float # attack setiap turn
    strength_potion_usage : bool # True jika sudah menggunakan strength potion
    resilience_potion_usage : bool # True jika sudah menggunakan resilience potion
    healing_potion_usage : bool # True jika sudah menggunakan healing potion
    kabur : bool # True jika kabur dari battle
    dmg_multiplier : int # pengali dmg
    item_exists : bool # True jika monster ball ada
    turn : int # turn setiap stage
    reward : int # hadiah
    
    data_monster_musuh = [[c.data_monster[i][j] for j in range(5)] for i in range(len(c.data_monster))]
    data_monster_agent = [[c.data_monster[i][j] for j in range(5)] for i in range(len(c.data_monster))]
    
    os.system('cls')
    
    # bagian muncul monster musuh
    id_musuh = rng.lcg_x(10)%(len(data_monster_musuh)-1) +1
    lvl_musuh = rng.lcg_x(10)%5 +1
    
    stats_musuh = data_monster_musuh[id_musuh]
        
    if int(lvl_musuh)>1:
        for i in range(2,len(stats_musuh)):
            stats_musuh[i] = str(int(int(stats_musuh[i])*(lvl_musuh-1)*0.1+int(stats_musuh[i])))
    
    if lvl_musuh == 5:
        print(c.monster_level5)
    else:
        print(c.monster)
    
    print(f'''
RAWRRR, monster {stats_musuh[1]} telah muncul

Name      : {stats_musuh[1]}
ATK Power : {stats_musuh[2]}
DEF Power : {stats_musuh[3]}
HP        : {stats_musuh[4]}
Level     : {lvl_musuh}
''')
    
    # bagian muncul monster user
    print('\n============ MONSTER LIST ============\n')
    list_monster = []
    
    num = 1
    for i in range(len(c.data_monster_inventory)):
        if c.data_monster_inventory[i][0] == c.data_login[0]:
            monster_id = int(c.data_monster_inventory[i][1])
            
            print(f'{num}. {data_monster_agent[monster_id][1]}')
            list_monster += [[c.data_monster_inventory[i][2],data_monster_agent[monster_id][1],data_monster_agent[monster_id][2],data_monster_agent[monster_id][3],data_monster_agent[monster_id][4]]]
            
            num += 1
        
    while True:
        id_agent = input('\nPilih monster untuk bertarung: ')
        if not u.check_int(id_agent) or not int(id_agent) in range(1,num):
            print('\n\033[31mPilihan nomor tidak tersedia!\033[0m\n')
        else:
            break
    
    lvl_agent = list_monster[int(id_agent)-1][0]    
    stats_agent = list_monster[int(id_agent)-1]
    max_hp = stats_agent[4]
    
    if int(lvl_agent)>1:
        for i in range(2,len(stats_agent)):
            stats_agent[i] = str(int(int(stats_agent[i])*(int(lvl_agent)-1)*0.1+int(stats_agent[i])))
            
    if int(lvl_agent) == 5:
        print(c.monster_level5)
    else:
        print(c.monster)
    
    print(f'''
RAWRRR, Agent {c.data_login[1]} mengeluarkan monster {stats_agent[1]} !!!

Name      : {stats_agent[1]}
ATK Power : {stats_agent[2]}
DEF Power : {stats_agent[3]}
HP        : {stats_agent[4]}
Level     : {lvl_agent}
''')
    
    strength_potion_usage = False
    resilience_potion_usage = False
    healing_potion_usage = False
    kabur = False
    dapat_monster = False
    
    turn = 1
    # bagian setiap turn
    while int(stats_agent[4])>0 and int(stats_musuh[4])>0:
        kabur = False
        dapat_monster = False
        endturn = False
        
        while not endturn:
            print(f'''
============ TURN {turn} ({stats_agent[1]}) ============
1. Attack
2. Use Potion
3. Use Monster Ball
4. Quit
''')
            
            perintah = input('Pilih perintah: ')
            if not perintah in ['1','2','3','4']:
                print('\n\033[31mPilihan nomor tidak tersedia!\033[0m\n')
            
            # bagian kabur dari battle
            elif perintah == '4':
                endturn = True
                kabur = True
                
            # bagian monster ball
            elif perintah == '3':
                item_exists = False
                monster_exists = False
                
                for j in range(len(c.data_monster_inventory)):
                    if c.data_monster_inventory[j][0] == c.data_login[0] and c.data_monster_inventory[j][1] == data_monster_musuh[id_musuh][0]:
                        monster_exists = True
                
                for j in range(len(c.data_item_inventory)):
                    if c.data_item_inventory[j][0] == c.data_login[0] and c.data_item_inventory[j][1] == 'monster ball':
                        jumlah_item = int(c.data_item_inventory[j][2])
                        item_exists = True
                
                if monster_exists:
                    print(f'\nAnda sudah memiliki monster {stats_musuh[1]} dalam inventory!\n')
                elif not item_exists:
                    print('\nAnda tidak memiliki Monster Ball dalam inventory!\n')
                else:
                    os.system('cls')
                    p.update_potion(c.data_login[0],'monster ball',-1)
                    
                    print('\nSwoosshhhhh, Anda mengeluarkan Monster Ball !!!') 
                    number = rng.lcg_x(10)%100
                    if (lvl_musuh == 1 and number < 75) or (lvl_musuh == 2 and number < 50) or (lvl_musuh == 3 and number < 25) or (lvl_musuh == 4 and number < 10) or (lvl_musuh == 5 and number < 5):
                        os.system('cls')
                        
                        c.data_monster_inventory += [[c.data_login[0],str(id_musuh),str(lvl_musuh)]]
                        
                        print(f'Selamat, Anda berhasil mendapatkan monster {stats_musuh[1]} !!!')
                        endturn = True
                        dapat_monster = True
                    else:
                        print(f'Yahhh, Anda belum berhasil mendapatkan monster {stats_musuh[1]} !!!')
                        
                        print(f'\nSisa Monster Ball Anda: {jumlah_item-1}\n')
            
            # bagian potion
            elif perintah == '2':
                exists = False
                
                for j in range(len(c.data_item_inventory)):
                    if c.data_item_inventory[j][0] == c.data_login[0] and c.data_item_inventory[j][1] != 'monster ball':
                        exists = True
                        
                if not exists:
                    print('\nAnda tidak memiliki Potion dalam inventory!\n')
                else:
                    while True:
                        print(f'''
============ POTION LIST ============
1. Strength Potion (Qty: {p.read_potion(c.data_login[0],'strength')}) - Increases ATK Power
2. Resilience Potion (Qty: {p.read_potion(c.data_login[0],'resilience')}) - Increases DEF Power
3. Healing Potion (Qty: {p.read_potion(c.data_login[0],'healing')}) - Restores Health
4. Cancel
''')
                        potion = input('Pilih perintah: ')
                        if not potion in ['1','2','3','4']:
                            print('\n\033[31mPilihan nomor tidak tersedia!\033[0m\n')
                        elif potion == '1':
                            
                            if p.read_potion(c.data_login[0],'strength') == '0':
                                print('\nAnda tidak memiliki Potion dalam inventory!\n')
                            elif strength_potion_usage == True:
                                print(f'\nKamu mencoba memberikan ramuan ini kepada {stats_agent[1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n')
                            else:
                                os.system('cls')
                                print(f'\nSetelah meminum ramuan ini, aura kekuatan terlihat mengelilingi {stats_agent[1]} dan gerakannya menjadi lebih cepat dan mematikan.\n')
                                stats_agent[2] = str(int(int(stats_agent[2])*1.05))
                                
                                p.update_potion(c.data_login[0],'strength',-1)
                                strength_potion_usage = True
                                endturn = True
                                break
                        elif potion == '2':
                            
                            if p.read_potion(c.data_login[0],'resilience') == '0':
                                print('\nAnda tidak memiliki Potion dalam inventory!\n')
                            elif resilience_potion_usage == True:
                                print(f'\nKamu mencoba memberikan ramuan ini kepada {stats_agent[1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n')
                            else:
                                os.system('cls')
                                print(f'\nSetelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar {stats_agent[1]} yang membuatnya terlihat semakin tangguh dan sulit dilukai.\n')
                                stats_agent[3] = str(int(int(stats_agent[3])*1.05))
                                
                                p.update_potion(c.data_login[0],'resilience',-1)
                                resilience_potion_usage = True
                                endturn = True
                                break
                        elif potion == '3':
                            
                            if p.read_potion(c.data_login[0],'healing') == '0':
                                print('\nAnda tidak memiliki Potion dalam inventory!\n')
                            elif healing_potion_usage == True:
                                print(f'\nKamu mencoba memberikan ramuan ini kepada {stats_agent[1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n')
                            else:
                                os.system('cls')
                                print(f'\nSetelah meminum ramuan ini, luka-luka yang ada di dalam tubuh {stats_agent[1]} sembuh dengan cepat. Dalam sekejap, Pikachow terlihat kembali prima dan siap melanjutkan pertempuran.\n')
                                stats_agent[4] = str(int(int(stats_agent[4])+int(max_hp)*0.25))
                                if int(stats_agent[4]) > int(max_hp):
                                    stats_agent[4] = max_hp
                                
                                p.update_potion(c.data_login[0],'healing',-1)
                                healing_potion_usage = True
                                endturn = True
                                break
                        elif potion == '4':
                            break
                        
            # bagian attack user
            elif perintah == '1':
                os.system('cls')
                
                dmg_multiplier = rng.lcg_x(20)%61+70
                
                hp_terakhir = stats_musuh[4]
                attack_result = int(stats_agent[2])*((dmg_multiplier)/100)*((100-int(stats_musuh[3]))/100)
      
                stats_musuh[4] = str(int(int(stats_musuh[4])-attack_result))
                if int(stats_musuh[4])<0:
                    stats_musuh[4] = '0'
                
                print(f'''
SCHWINKKK, {stats_agent[1]} menyerang {stats_musuh[1]} !!!

Name      : {stats_musuh[1]}
ATK Power : {stats_musuh[2]}
DEF Power : {stats_musuh[3]}
HP        : {stats_musuh[4]}
Level     : {lvl_musuh}

Penjelasan:  ATT results: {attack_result}, HP terakhir = {hp_terakhir}, hasil HP = {stats_musuh[4]}
''')
                endturn = True
        
        if kabur or dapat_monster or stats_musuh[4] == '0':
            break 
        
        # bagian attack musuh   
        else:    
            dmg_multiplier = rng.lcg_x(15)%61+70
            
            hp_terakhir = stats_agent[4]
            attack_result = int(stats_musuh[2])*((dmg_multiplier)/100)*((100-int(stats_agent[3]))/100)
            
      
            stats_agent[4] = str(int(int(stats_agent[4])-attack_result))
            if int(stats_agent[4])<0:
                stats_agent[4] = '0'
            
            print(f'''
============ TURN {turn} ({stats_musuh[1]}) ============

SCHWINKKK, {stats_musuh[1]} menyerang {stats_agent[1]} !!!

Name      : {stats_agent[1]}
ATK Power : {stats_agent[2]}
DEF Power : {stats_agent[3]}
HP        : {stats_agent[4]}
Level     : {lvl_agent}

Penjelasan:  ATT results: {attack_result}, HP terakhir = {hp_terakhir}, hasil HP = {stats_agent[4]}
''')
        
            
        turn += 1
    
    # jika kabur dari battle
    if kabur:
        os.system('cls')
        print('\nAnda berhasil kabur dari BATTLE!\n')
        
    # jika kalah
    elif stats_agent[4] == '0':
        os.system('cls')
        print(f'\nYahhh, Anda dikalahkan monster {stats_musuh[1]}. Jangan menyerah, coba lagi !!!\n')
        
    # jika menang
    elif stats_musuh[4] == '0':
        os.system('cls')
        print(f'\nSelamat, Anda berhasil mengalahkan monster {stats_musuh[1]} !!!')
        
        reward = rng.lcg_x(10)%26 + 5
        print(f'Total OC yang Anda peroleh adalah {reward} OC.\n') 
        print(f'Good luck on your next journey, Agent {c.data_login[1]}!\n')
        
        sc.update_oc(reward)