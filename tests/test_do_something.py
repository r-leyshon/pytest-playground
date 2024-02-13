import os

from example_pkg.do_something import double_a_number, half_a_number, wrap_n_write_txt

# display TAD
def test_double_a_number_doubles():
    out = double_a_number(2)
    assert out == 4

class TestHalfANumber(object):
# display TDD below
    def test_half_a_number_halves(self):
        out = half_a_number(2)
        assert out == 1
        out = half_a_number(5)
        assert out == 2.5


    def test_half_a_number_always_returns_float(self):
        assert isinstance(half_a_number(0), float)
        assert isinstance(half_a_number(1), float)
        assert isinstance(half_a_number(2), float)


# example e2e test
class TestDoSomethingE2E(object):
    def test_end_to_end(self):
        num = 2
        num = double_a_number(num)
        num = double_a_number(num)
        num = half_a_number(num)
        assert num == 4

# no lint in directory
class TestWrapNWriteTxt(object):
    def test_wrap_n_write_txt_writes(self, tmp_path):
        num = 2
        tmp = os.path.join(tmp_path, "foo.txt")
        wrap_n_write_txt(num=num, pth=tmp)
        assert os.path.exists(tmp)

        with open(tmp, "r") as f:
            txt = f.readlines()
        
        assert txt[0] == "4.0"
            