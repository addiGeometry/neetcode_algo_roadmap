import pytest
from . import groupAnagrams

@pytest.mark.skip(reason="no way of currently testing this")
class TestAnaGroups:
    def test_case_1(self):
        assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]