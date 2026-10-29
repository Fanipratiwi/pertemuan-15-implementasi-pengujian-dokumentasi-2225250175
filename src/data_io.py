from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILE_DATA = ROOT / "data" / "nilai_contoh.txt"
FILE_OUTPUT = ROOT / "output" / "hasil_rekap.txt"


def baca_data_contoh():
    data_siswa = []

    if not FILE_DATA.exists():
        return data_siswa

    with FILE_DATA.open("r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()

            if not baris:
                continue

            bagian = baris.split(",")

            if len(bagian) != 2:
                continue

            nama = bagian[0].strip()
            teks_nilai = bagian[1].strip()

            try:
                nilai = float(teks_nilai)
            except ValueError:
                continue

            if nama and 0 <= nilai <= 100:
                data_siswa.append({
                    "nama": nama,
                    "nilai": nilai
                })

    return data_siswa


def simpan_rekap(teks):
    FILE_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with FILE_OUTPUT.open("w", encoding="utf-8") as file:
        file.write(teks)