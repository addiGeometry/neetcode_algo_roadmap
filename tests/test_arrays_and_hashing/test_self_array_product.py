import pytest
from . import productExceptSelf

class TestProductExceptSelf:
    def test_case_1(self):
        assert productExceptSelf([1,2]) == [2,1]

    def test_case_2(self):
        assert productExceptSelf([1,2,3,4]) == [24,12,8,6]

    def test_case_3(self):
        assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
        