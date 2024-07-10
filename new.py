"""
Happy Holidays fellow Code Warriors!
Now, Dasher! Now, Dancer! Now, Prancer, and Vixen!
On, Comet! On, Cupid! On, Donder and Blitzen!
That's the order Santa wanted his reindeer...right?
What do you mean he wants them in order by their last names!?
Looks like we need your help Code Warrior!

Sort Santa's Reindeer
Write a function that accepts a sequence of Reindeer names,
and returns a sequence with the Reindeer names sorted by their last names.

Notes:
It's guaranteed that each string is composed of two words, separated by a single space
In case of two identical last names, keep the original order
Examples
For this input:

[
  "Dasher Tonoyan",
  "Dancer Moore",
  "Prancer Chua",
  "Vixen Hall",
  "Comet Karavani",
  "Cupid Foroutan",
  "Donder Jonker",
  "Blitzen Claus"
]
You should return this output:

[
  "Prancer Chua",
  "Blitzen Claus",
  "Cupid Foroutan",
  "Vixen Hall",
  "Donder Jonker",
  "Comet Karavani",
  "Dancer Moore",
  "Dasher Tonoyan",
]
"""
import pytest


def sort_reindeer(reindeer_names):
    """My_solution"""
    k = [i.split() for i in reindeer_names]
    k.sort(key=lambda x: x[1])
    sorted_list = [' '.join(i) for i in k]
    return sorted_list


@pytest.mark.parametrize("reindeer_names, sorted_list", [
    (['Kenjiro Mori', 'Susumu Tokugawa', 'Juzo Okita', 'Akira Sanada'],
     ['Kenjiro Mori', 'Juzo Okita', 'Akira Sanada', 'Susumu Tokugawa']),
    ([], []),
    (['Yasuo Kodai', 'Kenjiro Sado', 'Daisuke Aihara',
      'Susumu Shima', 'Akira Sanada', 'Yoshikazu Okita',
      'Shiro Yabu', 'Sukeharu Nanbu', 'Sakezo Yamamoto',
      'Hikozaemon Ohta', 'Juzo Mori', 'Saburo Tokugawa'],
     ['Daisuke Aihara', 'Yasuo Kodai', 'Juzo Mori',
      'Sukeharu Nanbu', 'Hikozaemon Ohta', 'Yoshikazu Okita',
      'Kenjiro Sado', 'Akira Sanada', 'Susumu Shima',
      'Saburo Tokugawa', 'Shiro Yabu', 'Sakezo Yamamoto']),
    (['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto'],
     ['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto']),
    (["Sukeharu Yamamoto", "Juzo Yabu", "Saburo Shima", "Shiro Sanada", "Daisuke Mori"],
     ['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto']),
    (['aaa, ccc', 'aaa, aaa', 'aaa, bbb'], ['aaa, aaa', 'aaa, bbb', 'aaa, ccc'])
])
def test_sort_reindeer(reindeer_names, sorted_list):
    """Pytest"""
    assert sort_reindeer(reindeer_names) == sorted_list


if __name__ == '__main__':
    pytest.main()

