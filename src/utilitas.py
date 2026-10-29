def validasi_nilai(nilai):
    """Memeriksa apakah nilai berupa angka antara 0 dan 100."""
    try:
        nilai = float(nilai)
    except (ValueError, TypeError):
        return False

    return 0 <= nilai <= 100


def tentukan_status(nilai):
    """Nilai minimal 75 dinyatakan lulus."""
    if nilai >= 75:
        return "Lulus"
    return "Tidak Lulus"