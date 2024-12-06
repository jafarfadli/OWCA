# Penulis Modul: Muhammad Jafar Fadli 16523137, Jessica Allen 19623227
# Judul Modul: Utility
# Tanggal: 20 May 2024

# Fungsi split string
def split_str(string : str,delimiter : str) -> list[str]:
    # Variable Lokal
    array : list[str] # hasil split
    limit : int # membatasi string untuk ditambah ke array
    
    array = []
    limit = 0
    for i in range(len(string)):
        if string[i] == delimiter:
            array += [string[limit:i]]
            limit = i+1
    array += [string[limit:]]
    return array            

# Fungsi membaca file csv sebagai matriks
def read_csv(file_name : str) -> list[list[str]]:
    # Variable Lokal
    data : list[list[str]] # hasil read
    row : list[str] # baris pada data
    
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            row = split_str(line[:-1],';')
            data += [row]
    return data

# Fungsi menulis ulang csv
def write_csv(file_name : str, data : list[list[str]]) -> None:
    with open(file_name, 'w', newline='') as file:
        for row in data:
            file.write(';'.join(map(str, row)) + '\n')

# Fungsi cek string sebagai int non-negatif
def check_int(string : str) -> bool:
    if len(string) == 0:
        return False
    elif string[0] not in '123456789' and len(string)>1:
        return False
    for char in string:
        if char not in '1234567890':
            return False
    return True

