import random
import string

# Membuat daftar huruf kecil A-Z
lowercase_alphabet = list(string.ascii_lowercase)

# Inisialisasi daftar untuk menyimpan hasil
shuffled_with_domains = []

# Mengulang 10 kali untuk menghasilkan 10 urutan huruf yang diacak
for _ in range(47):
    # Mengacak urutan huruf
    random.shuffle(lowercase_alphabet)
    
    # Mengambil hanya 5 karakter pertama setelah diacak
    shuffled_lower_alphabet = ''.join(lowercase_alphabet[:10])
    
    # Menambahkan "@asu.hanimexco.com.vn" di akhir karakter
    shuffled_with_domain = shuffled_lower_alphabet + "@asu.hanimexco.com.vn"
    
    # Menambahkan hasil ke daftar
    shuffled_with_domains.append(shuffled_with_domain)

# Menyimpan hasil ke dalam file
with open("hasil.txt", "w") as file:
    for email in shuffled_with_domains:
        file.write(email + "\n")
        print(shuffled_with_domain)
