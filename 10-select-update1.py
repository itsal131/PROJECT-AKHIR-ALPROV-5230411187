import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

# SELECT ALL FAUNA
kursor = koneksi.cursor()

# ubah berdasarkan id_fauna
id_fauna = 10
jml_skrg = 650

# gunakan Querry UPDATE SET
kursor.execute(f"UPDATE fauna SET jml_skrg= {jml_skrg} WHERE id_fauna = {id_fauna}")
koneksi.commit()

# CEK DATA
if kursor.rowcount > 0:
    print(f'Data dengan ID {id_fauna} berhasil diubah')
else:
    print(f'Sayangnya tidak ada fauna dengan ID {id_fauna}')

koneksi.close