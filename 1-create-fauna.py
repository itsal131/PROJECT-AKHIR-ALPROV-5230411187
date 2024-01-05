import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

# CREATE TABEL FAUNA
koneksi.execute('''
            CREATE TABLE fauna(
                id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_fauna VARCHAR(50),
                jenis VARCHAR(50),
                asal VARCHAR(50),
                jml_skrg INTEGER(10),
                thn_ditemukan INTEGER(10)
                )    
                ''')
koneksi.close()