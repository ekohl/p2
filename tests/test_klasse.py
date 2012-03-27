import unittest
import klasse

class TestKlasse(unittest.TestCase):
    def test_hello(self):
        k = klasse.Klasse()
        self.assertEqual("Hello world", k.hello())
