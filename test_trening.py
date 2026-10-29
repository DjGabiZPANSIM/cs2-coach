import unittest
from trening import oblicz_koszt


class TestKosztTreningu(unittest.TestCase):
    def test_godzina_treningu(self):
        self.assertEqual(oblicz_koszt(100, 60), 100)

    def test_pol_godziny(self):
        self.assertEqual(oblicz_koszt(100, 30), 50)

    def test_90_minut(self):
        self.assertEqual(oblicz_koszt(100, 90), 150)

    def test_zaokraglenie_do_groszy(self):
        self.assertEqual(oblicz_koszt(100, 20), 33.33)

    def test_ujemna_cena(self):
        with self.assertRaises(ValueError):
            oblicz_koszt(-100, 60)

    def test_zerowy_czas(self):
        with self.assertRaises(ValueError):
            oblicz_koszt(100, 0)

    def test_ujemny_czas(self):
        with self.assertRaises(ValueError):
            oblicz_koszt(100, -30)


if __name__ == "__main__":
    unittest.main()