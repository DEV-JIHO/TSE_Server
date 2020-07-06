from typing import List, Optional

from pydantic import BaseModel

# 미세먼지 관련 함수

# 하드웨어 수집 정보에 따라서 변수 추가 예정

class DustBase(BaseModel):
    Uv: str
    Nitric: str
    Sulfuric: str
    Formal: str

    class Config:
        orm_mode = True


class DustCreate(DustBase):
    pass


class Dust(DustBase):
    id: int
    Date: str

