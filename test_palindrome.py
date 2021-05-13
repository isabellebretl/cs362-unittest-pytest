import unittest
import palindrome

class TestCase(unittest.TestCase):
    def test_pal1(self):
        self.assertEqual(palindrome.pal("anna"), True)
    def test_pal2(self):
        self.assertEqual(palindrome.pal("Anna"), False)
    def test_pal3(self):
        self.assertEqual(palindrome.pal("hello"), False)
    def test_pal4(self):
        self.assertEqual(palindrome.pal("121"), True)


if __name__ == '__main__':
    unittest.main()