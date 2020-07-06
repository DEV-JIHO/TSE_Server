from typing import List, Optional

from pydantic import BaseModel


# 미세먼지 관련 함수

# 하드웨어 수집 정보에 따라서 변수 추가 예정

class dustBase(BaseModel):
    Uv: str
    Nitric: str
    Sulfuric: str
    Formal: str

    class Config:
        orm_mode = True


class dustCreate(dustBase):
    location: str


class Dust(dustBase):
    id: int
    Date: str
