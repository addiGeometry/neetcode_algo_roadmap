import pytest
from . import topKFrequent

class TestTopK:
    def test_case_1(self):
        assert topKFrequent([1,1,1,2,2,3], 2) == [1,2]

    def test_case_2(self):
        assert topKFrequent([1], 1) == [1]

    def test_case_3(self):
        assert topKFrequent([-1,-1], 1) == [-1]

    def test_case_4(self):
        assert topKFrequent([4,1,-1,2,-1,2,3], 2) == [-1,2]
        