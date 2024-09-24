"""
I have a cat and a dog which I got as kitten / puppy.
I forget when that was, but I do know their current ages as catYears and dogYears.
Find how long I have owned each of my pets and return as a list [ownedCat, ownedDog]

NOTES:

Results are truncated whole numbers of "human" years
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
"""
import pytest


def owned_cat_and_dog(cat_years, dog_years):
    """My_solution"""
    # Инициализация x и y
    x = 0
    y = 0

    if 0 < cat_years < 15:
        x = 0
    elif 15 <= cat_years < 24:
        x = 1
    elif 24 <= cat_years < 28:
        x = 2
    elif cat_years == 28:
        x = 3
    elif cat_years > 28:
        x = (cat_years - 28) // 4 + 3

    if 0 < dog_years < 15:
        y = 0
    elif 15 <= dog_years < 24:
        y = 1
    elif 24 <= dog_years < 29:
        y = 2
    elif dog_years == 29:
        y = 3
    elif dog_years > 29:
        y = (dog_years - 29) // 5 + 3

    return [x, y]


@pytest.mark.parametrize("cat_years, dog_years, expected_result", [
    (9, 7, [0, 0]),
    (15, 15, [1, 1]),
    (18, 21, [1, 1]),
    (19, 17, [1, 1]),
    (24, 24, [2, 2]),
    (25, 25, [2, 2]),
    (26, 26, [2, 2]),
    (27, 27, [2, 2]),
    (56, 64, [10, 10]),
])
def test_owned_cat_and_dog(cat_years, dog_years, expected_result):
    """Pytest"""
    assert owned_cat_and_dog(cat_years, dog_years) == expected_result


if __name__ == '__main__':
    pytest.main()

