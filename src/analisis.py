from src.utilitas import tentukan_status


def hitung_rata_rata(nilai):
    if not nilai:
        return 0

    return sum(nilai) / len(nilai)


def hitung_nilai_tertinggi(nilai):
    if not nilai:
        return 0

    return max(nilai)


def hitung_nilai_terendah(nilai):
    if not nilai:
        return 0

    return min(nilai)


def analisis_nilai(data_siswa):
    if not data_siswa:
        return None

    semua_nilai = [siswa["nilai"] for siswa in data_siswa]

    hasil = {
        "jumlah_siswa": len(data_siswa),
        "rata_rata": hitung_rata_rata(semua_nilai),
        "tertinggi": hitung_nilai_tertinggi(semua_nilai),
        "terendah": hitung_nilai_terendah(semua_nilai),
        "lulus": sum(
            1 for nilai in semua_nilai if tentukan_status(nilai) == "Lulus"
        ),
        "tidak_lulus": sum(
            1 for nilai in semua_nilai if tentukan_status(nilai) == "Tidak Lulus"
        ),
    }

    return hasil