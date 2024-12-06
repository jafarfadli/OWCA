# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Login
# Tanggal: 20 May 2024

import src.Constant as c

# Prosedur login untuk mengakses akun user
def login() -> None:
    # Variable Lokal
    username : str # username untuk login
    password : str # password
    success : bool # True jika password benar
    exists : bool # True jika username ada
    
    # Memeriksa status login user
    if c.data_login != ['','','','','']:
        print(f'Login gagal!\nAnda telah login dengan username {c.data_login[1]}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.')
    else: # User belum login
        username = input('Username: ')
        password = input('Password: ')
        
        success = True
        exists = False
        
        # Memeriksa kesesuaian username dan password
        for i in range(len(c.data_user)):
            if c.data_user[i][1] == username:
                exists = True
                if c.data_user[i][2] != password:
                    success = False
                index_user = i
                break
        
        if not exists:
            print('\n\033[31mUsername tidak terdaftar!\033[0m')
        elif not success:
            print('\n\033[31mPassword salah\033[0m')
        else: # Username dan password sesuai (valid)
            # Mengubah data ke-2 di file csv menjadi data user yang login
            c.data_login = c.data_user[index_user]
            
            # Output
            print(f'\nSelamat datang, {c.data_login[3]} {username}!\nKetik command "help" untuk menampilkan daftar command yang dapat kamu panggil.')
                
    