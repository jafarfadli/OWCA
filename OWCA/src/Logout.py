# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227, Nawaf Amjad Rizqi A. I. 19623217
# Judul Modul: Logout
# Tanggal: 20 May 2024

import src.Constant as c

# Prosedur logout dari akun user
def logout() -> None:
    # jika user belum login
    if c.data_login == ['','','','','']:
        print('Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum logout')
    
    # jika user sudah login
    else:
        c.data_login = ['','','','','']
        print("Anda telah logout, ketik 'help' untuk melihat daftar command yang dapat dipanggil." )