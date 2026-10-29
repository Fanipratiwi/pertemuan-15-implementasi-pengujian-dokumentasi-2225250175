from src.analisis import analisis_nilai
from src.data_io import baca_data_contoh, simpan_rekap
from src.utilitas import validasi_nilai, tentukan_status


def tampilkan_rekap(data_siswa):
    hasil = analisis_nilai(data_siswa)

    if hasil is None:
        return "Belum ada data siswa."

    baris = [
        "REKAP DAN ANALISIS NILAI MATEMATIKA",
        "=" * 40,
        ""
    ]

    for nomor, siswa in enumerate(data_siswa, start=1):
        status = tentukan_status(siswa["nilai"])
        baris.append(
            f"{nomor}. {siswa['nama']} | "
            f"Nilai: {siswa['nilai']:g} | Status: {status}"
        )

    baris.extend([
        "",
        "-" * 40,
        f"Jumlah siswa   : {hasil['jumlah_siswa']}",
        f"Rata-rata      : {hasil['rata_rata']:.2f}",
        f"Nilai tertinggi: {hasil['tertinggi']:g}",
        f"Nilai terendah : {hasil['terendah']:g}",
        f"Jumlah lulus   : {hasil['lulus']}",
        f"Tidak lulus    : {hasil['tidak_lulus']}",
    ])

    return "\n".join(baris)


def main():
    data_siswa = baca_data_contoh()

    print("PROGRAM REKAP NILAI MATEMATIKA")
    print("1. Gunakan data contoh")
    print("2. Masukkan data siswa sendiri")

    pilihan = input("Pilih menu (1/2): ").strip()

    if pilihan == "2":
        data_siswa = []
        jumlah = input("Masukkan jumlah siswa: ").strip()

        try:
            jumlah = int(jumlah)
            if jumlah <= 0:
                print("Jumlah siswa harus lebih dari 0.")
                return
        except ValueError:
            print("Jumlah siswa harus berupa bilangan bulat.")
            return

        for nomor in range(1, jumlah + 1):
            nama = input(f"Nama siswa ke-{nomor}: ").strip()

            if not nama:
                print("Nama tidak boleh kosong. Silakan ulangi.")
                return

            teks_nilai = input(f"Nilai {nama} (0-100): ").strip()

            if not validasi_nilai(teks_nilai):
                print("Nilai tidak valid. Masukkan angka dari 0 sampai 100.")
                return

            data_siswa.append({
                "nama": nama,
                "nilai": float(teks_nilai)
            })

    elif pilihan != "1":
        print("Pilihan menu tidak valid.")
        return

    if not data_siswa:
        print("Data siswa kosong atau tidak tersedia.")
        return

    hasil_rekap = tampilkan_rekap(data_siswa)
    print()
    print(hasil_rekap)

    simpan_rekap(hasil_rekap)
    print("\nHasil berhasil disimpan di output/hasil_rekap.txt")


if __name__ == "__main__":
    main()