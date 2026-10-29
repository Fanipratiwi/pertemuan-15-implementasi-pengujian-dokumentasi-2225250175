import unittest

from src.analisis import analisis_nilai
from src.utilitas import validasi_nilai, tentukan_status


class TestAnalisisNilai(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"nama": "Andi", "nilai": 80},
            {"nama": "Budi", "nilai": 60},
            {"nama": "Citra", "nilai": 90},
            {"nama": "Dina", "nilai": 70},
        ]

    def test_rata_rata(self):
        self.assertEqual(analisis_nilai(self.data)["rata_rata"], 75)

    def test_nilai_tertinggi(self):
        self.assertEqual(analisis_nilai(self.data)["tertinggi"], 90)

    def test_nilai_terendah(self):
        self.assertEqual(analisis_nilai(self.data)["terendah"], 60)

    def test_status_lulus(self):
        self.assertEqual(tentukan_status(75), "Lulus")

    def test_status_tidak_lulus(self):
        self.assertEqual(tentukan_status(74), "Tidak Lulus")

    def test_nilai_batas(self):
        self.assertTrue(validasi_nilai(0))
        self.assertTrue(validasi_nilai(100))

    def test_nilai_invalid(self):
        self.assertFalse(validasi_nilai(-1))
        self.assertFalse(validasi_nilai(101))
        self.assertFalse(validasi_nilai("abc"))

    def test_data_kosong(self):
        self.assertIsNone(analisis_nilai([]))


if __name__ == "__main__":
    unittest.main()