## B01 - Input nilai tidak valid
- Gejala: Pengguna memasukkan huruf atau nilai di luar 0-100.
- Penyebab: Input tidak sesuai dengan format nilai yang diperlukan.
- Perbaikan: Membuat fungsi validasi_nilai().
- Pengujian ulang: Uji nilai -1, 101, dan abc.

## B02 - Data siswa kosong
- Gejala: Statistik tidak dapat dihitung jika data kosong.
- Penyebab: Tidak ada nilai yang dapat dianalisis.
- Perbaikan: Memeriksa data sebelum menghitung statistik.
- Pengujian ulang: Uji dengan data kosong.

## B03 - Hasil rekap belum tersimpan
- Gejala: File hasil belum tersedia jika folder output belum ada.
- Penyebab: Folder tujuan belum dibuat.
- Perbaikan: Membuat folder output secara otomatis sebelum menyimpan.
- Pengujian ulang: Jalankan program dan periksa output/hasil_rekap.txt.