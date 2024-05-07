# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells
# and carries the "instructions" for the development and functioning of living organisms.
# If you want to know more: http://en.wikipedia.org/wiki/DNA
# In DNA strings, symbols "A" and "T" are complements of each other,
# as "C" and "G". Your function receives one side of the DNA (string, except for Haskell);
# you need to return the other complementary side.
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).
# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)
# Example: (input --> output)
import pytest


# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"


def dna_strand(dna):
    """My_solution"""
    return (dna.translate(str.maketrans({'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'})))


def test_dna_strand():
    """My_test_Pytest"""
    assert dna_strand("ATGC") == "TACG"
    assert dna_strand("AAAACCCGGT") == "TTTTGGGCCA"


if __name__ == "__main__":
    pytest.main()
