from pydantic import BaseModel


# 미세먼지 관련 함수

# 하드웨어 수집 정보에 따라서 변수 추가 예정

class DustBase(BaseModel):
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


class DustCreate(DustBase):
    location: str

class ApiData(BaseModel):
    getHeatFeelingIdx: int
    getDiscomfortIdx: int
    getUVIdx: str
    getSenTaIdx: int
    getAirDiffusionIdx: int
    SO2: float
    CO: float
    O3: float
    NO2: float
    PM10: int
    PM25: int
    collected_time: str

    class Config:
        orm_mode = True
