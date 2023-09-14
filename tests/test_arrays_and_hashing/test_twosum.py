import pytest
from . import two_sum

class TestTwoSum:
    def test_twosum_case_1(self):
        assert two_sum([2,7,11,15], 9) == [0,1]

    def test_twosum_case_2(self):
        assert two_sum( [3,2,4], 6) == [1,2]
    
    def test_twosum_case_3(self):
        assert two_sum( [3,3], 6) == [0,1]

    def test_twosum_negative_case_1(self):
        assert not two_sum( [3,2,4], 6) == [2,3]