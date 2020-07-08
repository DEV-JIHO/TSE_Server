from typing import List, Optional

from pydantic import BaseModel


# 미세먼지 관련 함수

# 하드웨어 수집 정보에 따라서 변수 추가 예정

class dustBase(BaseModel):
    DustPm10: float
    DustPm25: float
    Humidity: float
    Temperature: float
    CarbonMonoxide: float
    NitrogenDioxide: float
    Ethanol: float
    Hydrogen: float
    Ammonia: float
    Methane: float
    Propane: float
    IsoButane: float

    class Config:
        orm_mode = True


class dustCreate(dustBase):
    location: str


class Dust(dustBase):
    id: int
    CurrentTime: str
