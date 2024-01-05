import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

# SELECT ALL FAUNA
kursor = koneksi.cursor()

# ubah berdasarkan id_fauna
asal = "Kalimantan"

# gunakan Querry UPDATE SET
kursor.execute(f"DELETE FROM fauna WHERE asal = ?", (asal,))
koneksi.commit()

# CEK DATA
if kursor.rowcount > 0:
    print(f'Data dengan asal {asal} berhasil dihapus')
else:
    print(f'Sayangnya tidak ada fauna dengan ID {asal}')

koneksi.close