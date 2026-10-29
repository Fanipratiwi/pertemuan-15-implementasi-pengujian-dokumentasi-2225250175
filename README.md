Nama: Fani Pratiwi Nur Indah
Nim: 2225250175
Kelas: 3B

## Deskripsi
Program Python untuk merekap nilai matematika siswa,
menghitung statistik nilai, menentukan kelulusan, dan
menyimpan hasil rekap ke file teks.

## Fitur
- Menggunakan data contoh atau memasukkan data sendiri.
- Memvalidasi nilai antara 0 sampai 100.
- Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
- Menentukan status kelulusan.
- Menghitung jumlah siswa lulus dan tidak lulus.
- Menyimpan hasil ke output/hasil_rekap.txt.
- Menyediakan pengujian otomatis.

## Ketentuan Kelulusan
Nilai 75 atau lebih dinyatakan Lulus.
Nilai di bawah 75 dinyatakan Tidak Lulus.

## Struktur Folder
- src/: kode program.
- data/: data nilai contoh.
- tests/: test case dan pengujian otomatis.
- docs/: dokumentasi bug dan demo.
- output/: hasil rekap.

## Cara Menjalankan
Jalankan dari terminal pada folder utama proyek:

python -m src.main

## Cara Menguji
Jalankan:

python -m unittest discover -s tests -v

## File Hasil
Hasil rekap disimpan di:
output/hasil_rekap.txt

## Pengembang
Nama: Fani Pratiwi Nur Indah
Nim: 2225250175
Kelas: 3B