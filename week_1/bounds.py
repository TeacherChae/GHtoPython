# ! python3
# venv: HakLeeGHStudy

import Rhino.Geometry as rg # 이건 pip install로 설치 못하나...
from src.utility.core import make_number

print(type(I).__dict__.keys())

modified_input = make_number(N)

domain = rg.Interval(min(modified_input), max(modified_input))