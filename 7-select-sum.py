import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

# INSERT DATA KE TABEL FAUNA
kursor.execute("SELECT SUM(jml_skrg) FROM fauna")
total_populasi = kursor.fetchone()[0]

print(f'Total Populasi hewan langka saat ini: {total_populasi}')
koneksi.close