# -*- coding: UTF-8 -*-


class TestClass:
    @staticmethod
    def func(x):
        return x + 1

    def test_func(self):
        assert self.func(3) == 5
