# Import re dan datetime
import re
from datetime import datetime

# Mencari tanggal sekarang
x = datetime.now()
date = x.strftime("%x")

# String
string = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, 
seperti Pangeran Diponegoro (TL: 1785-11-11), 
Pattimura (TL: 1783-06-08) dan KiHajar Dewantara (1889-05-02).
"""
# Mencari tanggal tanggal di dalam string
tanggal = re.findall(r"\d*[-]\d*[-]\d*", string)

# def mencari selisih
def selisih(d1, d2):
    # strptime untuk mengubah string tanggal menjadi format tanggal buat dihitung
    d1 = datetime.strptime(d1, "%m/%d/%y")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

# def membalik tanggal
def balik(t):
    tanggal_balik = ""
    # Mengsplit tahun bulan dan hari menggunakan re split 
    t = re.split("-", t)
    
    # Menambahkan tanggal kedalam string secara terbalik
    for i in range(2,-1,-1):
        tanggal_balik += t[i]
        tanggal_balik += "-"
    tanggal_balik = tanggal_balik[:-1]
    return tanggal_balik
    
# Print setiap output
for i in range(len(tanggal)):
    print(f"{balik(tanggal[i])} 00:00:00 berselisih {selisih(date, tanggal[i])} hari")
