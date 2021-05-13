import unittest
import wc

class TestCase(unittest.TestCase):
    def test_wc1(self):
        self.assertEqual(wc.wordC("This is an activity"), 4)
    def test_wc2(self):
        self.assertEqual(wc.wordC("hello"), 1)
    def test_wc3(self):
        self.assertEqual(wc.wordC(""), 0)


if __name__ == '__main__':
    unittest.main()