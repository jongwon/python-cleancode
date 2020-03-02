from ch8.test1.myfuncs import add_one


class TestMyfuncs2:

    def test_1_더하기_1_은2(self):
        assert add_one(1) == 2


