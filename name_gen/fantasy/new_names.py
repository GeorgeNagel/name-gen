import os
import random
import sys

from typing import List


def generate_names(gender: str, number_of_names: int) -> List[str]:
    """
    Generate a list of Arthurian-sounding names.

    gender: one of "male" or "female"
    number_of_names: how many names to generate
    """

    assert name_type in ["male", "female"]
    if name_type == "female":
        name_lengths = [2, 3]
    elif name_type == "male":
        name_lengths = [2, 3, 4]

    filename = "%s_names.txt" % name_type
    filepath = os.path.join(os.path.dirname(__file__), filename)

    names_by_syllable = []  # type: List[str]
    with open(filepath, 'r') as fin:
        names_by_syllable = [name.strip() for name in fin.readlines()]

    syllables = []  # type: List[List[str]]
    for name in names_by_syllable:
        for index, syllable in enumerate(name.split()):
            if len(syllables) < index + 1:
                syllables.append([])
            if syllable not in syllables[index]:
                syllables[index].append(syllable)

    names = []  # type: List[str]
    while number_of_names > 0:
        number_of_names -= 1
        name = ""
        name_length = random.choice(name_lengths)
        for index in range(name_length):
            possible_syllables = syllables[index]
            selected_syllable = random.choice(possible_syllables)
            name += selected_syllable
        names.append(name)
    return names

if __name__ == "__main__":
    arguments = sys.argv[1:]
    name_type = "male"
    number_of_names = 1000
    if len(arguments) > 0:
        name_type = arguments[0]
    if len(arguments) > 1:
        number_of_names = int(arguments[1])
    names = generate_names(name_type, number_of_names)
    print(names)
