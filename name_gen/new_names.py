import random
import os

from typing import List

from name_gen.fantasy.new_names import \
    generate_names as fantasy_generate_names


def generate_name(gender, origin="anglo-saxon") -> str:
    assert(origin in [
        "fantasy", "arthurian", "welsh",
        "irish", "scottish", "anglo-saxon", "norman"
    ])
    # Welsh name source
    # http://www.behindthename.com/names/usage/welsh
    if origin == "fantasy":
        # Create new names based on Arthurian names
        return fantasy_generate_names(gender, 1)[0]
    else:
        possible_names = read_names(origin, gender)
        # Capitalize correctly
        capitalized_names = []
        for name in possible_names:
            capitalized_name = name.capitalize()
            capitalized_names.append(capitalized_name)

        return random.choice(capitalized_names)


def read_names(origin: str, gender: str) -> List[str]:
    filename = "%s.txt" % gender
    filepath = os.path.join(os.path.dirname(__file__), 'data', origin, filename)
    with open(filepath, 'r') as fin:
        names = [name.strip() for name in fin.readlines()]
    return names
