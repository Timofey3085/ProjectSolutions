"""
The bloody photocopier is broken... Just as you were sneaking around the office to print off your favourite binary code!

Instead of copying the original, it reverses it: '1' becomes '0' and vice versa.

Given a string of binary, return the version the photocopier gives you as a string.
"""
import pytest


def broken(inp):
    """My_solution"""
    res = []
    for i in inp:
        if i == "1":
            res.append("0")
        elif i == "0":
            res.append("1")
    return "".join(res)


@pytest.mark.parametrize("inp, expected_result", [
    ('001111110011001110101111101001', '110000001100110001010000010110'),
    ('00110100110010011100110010100111100000011', '11001011001101100011001101011000011111100'),
    ('01001000010010011110100010010110111011100101101011100001110100101110001110010111',
     '10110111101101100001011101101001000100011010010100011110001011010001110001101000'),
    ('00000011111010001100010101001110', '11111100000101110011101010110001'),
    ('00010011011010110000100110011000010011011000101111011000101',
     '11101100100101001111011001100111101100100111010000100111010'),
    ('0010001110111011101011101010110000111100010000101011001011000000010',
     '1101110001000100010100010101001111000011101111010100110100111111101'),
    ('0101100110010010111110101100100100010110100000111011101000110',
     '1010011001101101000001010011011011101001011111000100010111001'),
    ('101010010000011010011101010111111110001101001100010101011001100000111000101101000110010000',
     '010101101111100101100010101000000001110010110011101010100110011111000111010010111001101111'),
    ('0100010111001110111010010110111010000110111101000101001111000001011011111010010001',
     '1011101000110001000101101001000101111001000010111010110000111110100100000101101110'),
    ('100011101111', '011100010000'),
])
def test_broken(inp, expected_result):
    """Pytest"""
    assert broken(inp) == expected_result


if __name__ == '__main__':
    pytest.main()

