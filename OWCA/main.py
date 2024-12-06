# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Main
# Tanggal: 20 May 2024

import src.Save as s
import src.Load as ld
import src.Exit as e
import src.Shop_Management as sm
import src.Monster_Management as mm
import src.Laboratory as lb
import src.Shop_Currency as sc
import src.Arena as a
import src.Battle as b
import src.Register as r
import src.Login as ln
import src.Logout as lt
import src.Menu_Help as h
import src.Inventory as inv
import src.Monster as m
import src.Jackpot as jc
import src.Constant as c
import os

# Variable Lokal
saved : bool # True jika sudah melakukan save
command : str # perintah user
danville : list[list[str]] # peta kota danville
run_game : bool # True jika folder load valid

danville = [['*','*','*','*','*','*','*','*','*','*','*','*'],
            ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
            ['*',' ',' ','X',' ','S',' ',' ','X',' ',' ','*'],
            ['*',' ','X','X',' ',' ',' ',' ','X',' ',' ','*'],
            ['*',' ',' ',' ',' ',' ',' ',' ','X',' ',' ','*'],
            ['*',' ',' ',' ',' ','P',' ','X','X',' ',' ','*'],
            ['*',' ','X',' ',' ',' ',' ',' ',' ',' ','L','*'],
            ['*',' ','X',' ',' ',' ',' ',' ',' ',' ',' ','*'],
            ['*',' ','X','X','X',' ',' ','A',' ','X',' ','*'],
            ['*',' ',' ',' ',' ',' ',' ',' ',' ','X',' ','*'],
            ['*',' ',' ','J',' ',' ','X','X','X','X',' ','*'],
            ['*','*','*','*','*','*','*','*','*','*','*','*']]
(x,y) = (5,5)



run_game = ld.load()

if run_game:
    os.system('cls')
    saved = True

    print(c.main_welcome)
    while True:
        # input command user
        command = input('>>> ')
        
        if command == 'help':
            os.system('cls')
            h.help()
        elif command == 'register':
            os.system('cls')
            r.register()
            saved = False
        elif command == 'login':
            os.system('cls')
            ln.login()
        elif command == 'logout':
            os.system('cls')
            lt.logout()
        elif command == 'exit':
            os.system('cls')
            e.exit(saved)
            break
        elif command == 'save':
            os.system('cls')
            s.save()
            saved = True
        else:
            os.system('cls')
            print('\n\033[31mCommand tidak ditemukan!\033[0m\n')
            
        while c.data_login[3] == 'admin':
            command = input('>>> ')
            
            if command == 'shop':
                os.system('cls')
                sm.shop_management()
                saved = False
            elif command == 'monster':
                os.system('cls')
                mm.monster_management()
                saved = False
            elif command == 'help':
                os.system('cls')
                h.help()
            elif command == 'login':
                os.system('cls')
                ln.login()
            elif command == 'logout':
                os.system('cls')
                lt.logout()
                break
            elif command == 'save':
                os.system('cls')
                s.save()
                saved = True
            else:
                os.system('cls')
                print('\n\n\033[31mCommand tidak ditemukan!\n\033[0m\n')
        
        while c.data_login[3] == 'agent':   
            print(f'\nAgent {c.data_login[1]} sedang berada di posisi: ({x-1},{y-1})')
            peta = ''
            for i in range(12):
                peta += '\n'
                for j in range(12):
                    if danville[i][j] == 'X':
                        if (j != 11 and danville[i][j+1] != 'X') or j == 11:
                            peta += f'\033[42mWwW\033[0m'
                        else:
                            peta += f'\033[42mWw\033[0m'
                    elif danville[i][j] == '*':
                        if (j != 11 and danville[i][j+1] != '*') or j == 11:
                            peta += f'\033[41m {danville[i][j]} \033[0m'
                        else:
                            peta += f'\033[41m {danville[i][j]}\033[0m'
                    elif danville[i][j+1] == 'X' or danville[i][j+1] == '*':
                        peta += f'\033[43m{danville[i][j]}\033[0m'
                    else:
                        peta += f'\033[43m{danville[i][j]} \033[0m'
            print(peta + '\n')
            
            command = input('>>> ')
            if command == 'w':
                os.system('cls')
                if danville[x-1][y] == ' ':
                    danville[x][y] = ' '
                    x -= 1

                    danville[x][y] = 'P'
                else:
                    print(f'\nAgent {c.data_login[1]} tidak bisa pindah karena terdapat Obstacle!')
                    if (danville[x-1][y] == 'L'):
                        print('Jika ingin memasuki Laboratory, ketik command "Laboratory"')
                    elif (danville[x-1][y] == 'S'):
                        print('Jika ingin memasuki Shop, ketik command "Shop"')
                    elif(danville[x-1][y] == 'A'):
                        print('Jika ingin memasuki Arena, ketik command "Arena", Good Luck!')
                    elif(danville[x-1][y] == 'J'):
                        print('Jika ingin bermain JackPot, ketik command "Jackpot"')

            elif command == 's':
                os.system('cls')
                if danville[x+1][y] == ' ':
                    danville[x][y] = ' '
                    x += 1

                    danville[x][y] = 'P'
                else:
                    print(f'\nAgent {c.data_login[1]} tidak bisa pindah karena terdapat Obstacle!')
                    if (danville[x+1][y] == 'L'):
                        print('Jika ingin memasuki Laboratory, ketik command "Laboratory"')
                    elif (danville[x+1][y] == 'S'):
                        print('Jika ingin memasuki Shop, ketik command "Shop"')
                    elif(danville[x+1][y] == 'A'):
                        print('Jika ingin memasuki Arena, ketik command "Arena", Good Luck!')
                    elif(danville[x+1][y] == 'J'):
                        print('Jika ingin bermain JackPot, ketik command "Jackpot"')

            elif command == 'd':
                os.system('cls')
                if danville[x][y+1] == ' ':
                    danville[x][y] = ' '
                    y += 1

                    danville[x][y] = 'P'
                else:
                    print(f'\nAgent {c.data_login[1]} tidak bisa pindah karena terdapat Obstacle!')
                    if (danville[x][y+1] == 'L'):
                        print('Jika ingin memasuki Laboratory, ketik command "Laboratory"')
                    elif (danville[x][y+1] == 'S'):
                        print('Jika ingin memasuki Shop, ketik command "Shop"')
                    elif(danville[x][y+1] == 'A'):
                        print('Jika ingin memasuki Arena, ketik command "Arena", Good Luck!')
                    elif(danville[x][y+1] == 'J'):
                        print('Jika ingin bermain JackPot, ketik command "Jackpot"')

            elif command == 'a':
                os.system('cls')
                if danville[x][y-1] == ' ':
                    danville[x][y] = ' '
                    y -= 1

                    danville[x][y] = 'P'
                else:
                    print(f'\nAgent {c.data_login[1]} tidak bisa pindah karena terdapat Obstacle!')
                    if (danville[x][y-1] == 'L'):
                        print('Jika ingin memasuki Laboratory, ketik command "Laboratory"')
                    elif (danville[x][y-1] == 'S'):
                        print('Jika ingin memasuki Shop, ketik command "Shop"')
                    elif(danville[x][y-1] == 'A'):
                        print('Jika ingin memasuki Arena, ketik command "Arena", Good Luck!')
                    elif(danville[x][y-1] == 'J'):
                        print('Jika ingin bermain JackPot, ketik command "Jackpot"')

            
            elif command == 'help':
                os.system('cls')
                h.help()
            elif command == 'login':
                os.system('cls')
                ln.login()
            elif command == 'logout':
                os.system('cls')
                lt.logout()
                break
            elif command == 'save':
                os.system('cls')
                s.save()
                saved = True
            elif command == 'inventory':
                os.system('cls')
                inv.inventory()

            elif command == 'battle':
                os.system('cls')
                if 'X' in [danville[x+1][y],danville[x-1][y],danville[x][y+1],danville[x][y-1]]:
                    b.battle()
        
                    saved = False
                else:
                    print(f'\nAgent {c.data_login[1]} tidak berada di area battle!\n')
            elif command == 'arena':
                os.system('cls')
                if 'A' in [danville[x+1][y],danville[x-1][y],danville[x][y+1],danville[x][y-1]]:
                    a.arena()
        
                    saved = False
                else:
                    print(f'\nAgent {c.data_login[1]} tidak berada di area arena!\n')
            elif command == 'shop':
                os.system('cls')
                if 'S' in [danville[x+1][y],danville[x-1][y],danville[x][y+1],danville[x][y-1]]:
                    sc.shop()
        
                    saved = False
                else:
                    print(f'\nAgent {c.data_login[1]} tidak berada di area shop!\n')
            elif command == 'laboratory':
                os.system('cls')
                if 'L' in [danville[x+1][y],danville[x-1][y],danville[x][y+1],danville[x][y-1]]:
                    lb.laboratory()
        
                    saved = False
                else:
                    print(f'\nAgent {c.data_login[1]} tidak berada di area laboratory!\n')
            elif command == 'jackpot':
                os.system('cls')
                if 'J' in [danville[x+1][y],danville[x-1][y],danville[x][y+1],danville[x][y-1]]:
                    jc.jackpot()
        
                    saved = False
                else:
                    print(f'\nAgent {c.data_login[1]} tidak berada di area jackpot!\n')
            elif command == 'monster':
                os.system('cls')
                m.monster()
            else:
                os.system('cls')
                print('\n\033[31mCommand tidak ditemukan!\033[0m\n')
        
    