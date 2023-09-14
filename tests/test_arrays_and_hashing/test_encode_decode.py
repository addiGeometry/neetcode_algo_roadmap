import pytest
from . import encode, decode

class TestEncode:
    def test_case_1(self):
        assert encode(["lint", "code", "loves", "you"]) == "4#lint4#code5#loves3#you"

    def test_case_2(self):
        assert  encode(["we", "say", ":", "yes"]) == "2#we3#say1#:3#yes"

    def test_edge_case_1(self):
        assert  encode(["we", "say", "::", "yes"]) == "2#we3#say2#::3#yes"

    def test_edge_case_2(self):
        assert  encode(["x", ";", "y"]) == "1#x1#;1#y"
    
    def test_edge_case_3(self):
        assert  encode(["x", ":;", "y"]) == "1#x2#:;1#y"

class TestDecode:
    def test_case_1(self):
        assert decode("4#lint4#code5#loves3#you") == ["lint", "code", "loves", "you"]

    def test_case_2(self):
        assert decode("2#we3#say1#:3#yes") == ["we", "say", ":", "yes"]
    
    def test_edge_case_1(self):
        assert  decode("2#we3#say2#::3#yes") == ["we", "say", "::", "yes"]

class TestEncodeDecode:
    def test_case_1(self):
        assert decode(encode(["lint", "code", "love", "you"])) == ["lint", "code", "love", "you"]

    def test_case_2(self):
        assert decode(encode(["we", "say", "::", "yes"])) == ["we", "say", "::", "yes"]
    
    def test_case_3(self):
        assert decode(encode(["we", "say", ":;", "yes"])) == ["we", "say", ":;", "yes"]
        