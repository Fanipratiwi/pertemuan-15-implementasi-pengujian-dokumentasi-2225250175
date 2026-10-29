# Test Case Program Rekap Nilai

| ID | Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|---|
| T1 | Rata-rata nilai | 80, 60, 90, 70 | 75.0 |
| T2 | Nilai tertinggi | 80, 60, 90, 70 | 90 |
| T3 | Nilai terendah | 80, 60, 90, 70 | 60 |
| T4 | Batas kelulusan | 75 | Lulus |
| T5 | Di bawah batas kelulusan | 74 | Tidak Lulus |
| T6 | Nilai minimum | 0 | Valid |
| T7 | Nilai maksimum | 100 | Valid |
| T8 | Nilai di bawah batas | -1 | Tidak valid |
| T9 | Nilai di atas batas | 101 | Tidak valid |
| T10 | Input berupa huruf | abc | Tidak valid |
| T11 | Data kosong | [] | Tidak ada hasil analisis |

## Kesimpulan
Pengujian dilakukan untuk memeriksa perhitungan, batas nilai,
status kelulusan, dan penanganan input yang tidak valid.