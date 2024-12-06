# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Exit
# Tanggal: 20 May 2024

import src.Save as Save

# Prosedur exit
def exit(saved : bool) -> None:
    # Variable Lokal
    simpan : str # y jika melakukan save
    
    # jika belum disave
    if not saved:
        while True:
            simpan = input('\nApakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')
            if simpan == 'y': 
                Save.save()           
                break
            elif simpan == 'n':
                break
            else:
                print('\n\033[31minput tidak valid\033[0m\n')  
