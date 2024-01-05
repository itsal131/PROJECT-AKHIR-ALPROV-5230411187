import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

# SELECT ALL FAUNA
kursor = koneksi.cursor()

# Mengambil semua data dalam tabel dan menampilkannya
kursor.execute("SELECT *FROM fauna ORDER BY jml_skrg DESC")

# Menampilkan dalam bentuk baris
baris_tabel = kursor.fetchall()

print("TABEL FAUNA")
print("="*100)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("-"*100)

# TAMPILKAN DATA SESUAI FORMAT TABEL DENGAN PERULANGAN
for baris in baris_tabel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],
    baris[1], baris[2], baris[3], baris[4], baris[5]))
    print("-"*100)
koneksi.close