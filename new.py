import unittest

import pytest


def boredom(staff):
    # Определяем словарь с оценками скуки
    departments = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "trading": 6,
        "change": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25,
    }

    # Считаем общую скуку
    total_boredom = sum(departments[dept] for dept in staff.values() if dept in departments)

    # Возвращаем соответствующее сообщение
    if total_boredom <= 80:
        return 'kill me now'
    elif 80 < total_boredom < 100:
        return 'i can handle this'
    else:
        return 'party time!!'


def test_boredom():
    """Pytest"""
    assert boredom({"tim": "change", "jim": "accounts",
                    "randy": "canteen", "sandy": "change", "andy": "change", "katie": "IS",
                    "laura": "change", "saajid": "IS", "alex": "trading", "john": "accounts",
                    "mr": "finance"}) == "kill me now"
    assert boredom({"tim": "accounts", "jim": "accounts",
                    "randy": "pissing about", "sandy": "finance", "andy": "change",
                    "katie": "IS", "laura": "IS", "saajid": "canteen", "alex": "pissing about",
                    "john": "retail", "mr": "pissing about"}), "party time!!"


class Boredom(unittest.TestCase):

    def test_boredom(self):
        """Unittest"""
        self.assertEqual(boredom({"tim": "IS", "jim": "finance",
                                  "randy": "pissing about", "sandy": "cleaning", "andy": "cleaning",
                                  "katie": "cleaning", "laura": "pissing about", "saajid": "regulation",
                                  "alex": "regulation", "john": "accounts", "mr": "canteen"}), "i can handle this")


if __name__ == '__main__':
    pytest.main()
    unittest.main()

