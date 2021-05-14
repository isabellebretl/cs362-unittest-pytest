import pytest
import palindrome


class TestClass:
    def test_pal1(self):
        assert palindrome.pal("anna") == True
    def test_pal2(self):
        assert palindrome.pal("hello") == False
    def test_pal3(self):
        assert palindrome.pal("Anna") == False
    def test_pal4(self):
        assert palindrome.pal("121") == True