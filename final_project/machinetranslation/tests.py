import unittest

from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    """French to English tests"""
    def test_english_to_french(self):
        self.assertNotEqual(french_to_english("None"), '')
        self.assertEqual(french_to_english('Hello'), 'Bonjour')

    """English to French tests"""
    def test_english_to_french(self):
        self.assertNotEqual(english_to_french("None"), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

if __name__=='__main__':
    unittest.main()