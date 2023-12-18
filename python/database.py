# Buat koneksi ke server MySQL
import mysql.connector
db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="database_hehe"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan struktur tabel 'mahasiswa'

create_table_query = """

CREATE TABLE 1akun (

    no INT AUTO_INCREMENT PRIMARY KEY,

    kota_kabupaten VARCHAR(255),

    kota_kacamatan VARCHAR(255),

    nama_kecamatan VARCHAR(255),

    nama_puskesmas VARCHAR(255),
    
    penyakit yang tidak menular VARCHAR(255),
    
    jumlah INT(20),
    
    satuan VARCHAR(255),
    
    tahun date()
)

"""

 

# Eksekusi perintah SQL untuk membuat tabel

db_cursor.execute(create_table_query)

 

# Komit perubahan ke database

db_connection.commit()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()