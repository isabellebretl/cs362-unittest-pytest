import pytest
import wc


class TestClass:
    def test_wc1(self):
        assert wc.wordC("This is an activity") == 4
    def test_wc2(self):
        assert wc.wordC("hello") == 1
    def test_wc3(self):
        assert wc.wordC("") == 0