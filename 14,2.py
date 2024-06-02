# import random, string dan re
import re
import random
import string

# Mengambil semua karakter dan angka
all_characters = string.ascii_letters + string.digits

# Membuka isi email
with open("email.txt", "r") as email:
    string = email.read()

# Fungsi findall untuk mencari email dengan format a-zA-Z0-9 diawal, dipisah dengan @a-zA-Z0-9 dan .com atau .id
emails = re.findall(r"[a-zA-Z0-9.]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}", string)

# def mencari pass
def cari_pass():
    # Mengjoin huruf dan angka random sepanjang 8 karakter
    password = ''.join(random.choices(all_characters, k=8))
    return password

# def mencari username dengan split @ dan mengambil kata pertama
def cari_username(email):
    username = re.split("@", email)[0]
    return username

# print output
for i in range(len(emails)):
    print(f"{emails[i]} username: {cari_username(emails[i])}, password: {cari_pass()} ")