**Deskripsi Program**
Program ini adalah sistem manajemen penyewaan helm sederhana yang memungkinkan pengguna untuk:
- Melihat daftar helm yang tersedia.
- Menyewa helm berdasarkan kode.
- Mengembalikan helm yang telah disewa.
- Melihat riwayat transaksi penyewaan.

Program dibangun menggunakan Python dengan memanfaatkan:
- Struktur data: Dictionary dan List untuk menyimpan informasi.
- Struktur Kontrol : if else, for loop, while untuk menu dan validasi input
- Library : datetime dan tabulate untuk tampilan yang lebih baik.

**Fitur Utama**
- Manajemen Stok Helm : Tampilkan daftar helm beserta status ketersediaan, Update status helm otomatis (Tersedia/Disewa).
- Penyewaan Helm : Input data pelanggan dan durasi sewa, Hitung biaya sewa otomatis.
- Pengembalian Helm : Ubah status helm dari "Disewa" menjadi "Tersedia".
- Riwayat Transaksi : Tampilkan semua transaksi dalam format tabel rapi.

Untuk menjalankan program ini jangan lupa install library tabulate
**pip install tabulate**
