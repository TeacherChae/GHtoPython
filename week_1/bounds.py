# ! python3
# venv: HakLeeGHStudy
from typing import Union, Optional

def make_number(input_list:list[Optional[int]])->list[Union[int, float]]:
    number_list = []
    for element in input_list:
        try:
            number_list.append(int(element))
        except ValueError:
            try:
                number_list.append(float(element))
            except:
                raise ValueError
    return number_list
modified_input = make_number(N)

domain = ' To '.join(map(str, [min(modified_input), max(modified_input)]))