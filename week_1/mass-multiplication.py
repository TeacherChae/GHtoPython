# ! python3
# venv: HakLeeGHStudy
from typing import Union, Optional
import numpy as np

c = np.zeros(shape=[3,3])

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

modified_inputs = make_number(l)

Pr = []
mm = 1
for element in modified_inputs:
    mm *= element
    Pr.append(mm)
R = mm