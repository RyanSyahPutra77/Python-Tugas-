import requests
import mysql.connector
 
# Konfigurasi database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'database_hehe'
}
 
# Alamat URL API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/dpmptsp/od_19038_jml_nomor_induk_berush_nib_non_ush_mikro_kecil_umk_ter"
 
try:
    # Mengirim permintaan GET ke API
    response = requests.get(api_url)
 
    # Memeriksa status kode respons
    if response.status_code == 200:
        # Parse data JSON yang diterima 
        user_data = response.json().get("data")
 
        # Membuka koneksi ke database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
 
        # Menambahkan data pengguna ke dalam tabel
        for user in user_data:
            cursor.execute('''
                INSERT INTO 1akun (id, kode_provinsi, nama_provinsi, kode_kabupaten_kota, nama_kabupaten_kota, jumlah_nib_non_umk)
                VALUES (%s,%s,%s,%s,%s,%s)
            ''', (user['id'], user['kode_provinsi'], user['nama_provinsi'], user['kode_kabupaten_kota'], user['nama_kabupaten_kota'], user['jumlah_nib_non_umk']))
 
        # Menyimpan perubahan dan menutup koneksi
        conn.commit()
        conn.close()
 
        print("Data pengguna telah disimpan ke database MySQL.")
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
 
except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat menghubungi API: {str(e)}")
    
 
 