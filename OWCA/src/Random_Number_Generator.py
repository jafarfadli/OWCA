# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Random Number Generator
# Tanggal: 20 May 2024

import time

# Fungsi untuk menentukan bilangan acak dengan diberikan masukan
def lcg_x(n : int) -> int:
    # Variable Lokal
    a : int # pengganda
    c : int # peningkatan
    m : int # modulus
    
    a = 1664525
    c = 1013904223
    m = 2**(32)

    # Fungsi lcg
    def x(n : int) -> int:
        if n == 0: return int(time.time()*1000)
        else: return (a*x(n-1) +c)%m
        
    return x(n)
