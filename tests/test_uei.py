import pytest
from procurement_tools import UEI

testdata = [
    ("1234G678912F1", False, "too long"),
    ("023456789123", False, "starts with 0"),
    ("ABC456789123", False, "too many consecutive digits"),
    ("123E56789I23", False, "contains an I"),
    ("123E56789O23", False, "contains an O"),
    ("N4YFFGL4CDX6", False, "invalid checksum"),
    ("N4YFFGL4CDX5", True, "valid uei"),
    ("VN1AJFAD19J9", True, "valid uei"),
    ("DC2LX4S1GGF3", True, "valid uei"),
]


@pytest.mark.parametrize("uei,expected,reason", testdata)
def test_valid_uei(uei, expected, reason):
    assert UEI.is_valid(uei) == expected, reason
