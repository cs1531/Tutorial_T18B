import pytest

def test_add_works():
    assert (4 + 5 == 9)

class TestUS1():

    def setup_method(self):
        self.num = 6

    def test_add_num(self):
        self.num += 2
        assert(self.num  == 8)

    def test_init_six(self):
        assert self.num == 6
