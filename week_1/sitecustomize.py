# 워크스페이스에서 커스텀으로 정의한 모듈들을 전역 런타임에 로드시켜서
# from src.utility import core
# 와 같이 스크립트에서 직접 불러올 수 있게 해줌.
# 파일 삽입 위치 : C:\Users\<UserName>\.rhinocode\py39-rh8\Lib
# *Rhino8부터 가능...

import sys
from pathlib import Path

# 네 프로젝트의 src 절대경로 (Windows 경로 그대로)
PROJ_SRC = Path(r"D:\Keon Chae\Workshop\HakLeeGHStudy")

if PROJ_SRC.exists():
    p = str(PROJ_SRC)
    if p not in sys.path:
        sys.path.insert(0, p)
else:
    sys.stderr.write(f"[sitecustomize] Not found: {PROJ_SRC}\n")