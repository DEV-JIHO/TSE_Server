from sqlalchemy import Column, Integer, String, Float

from app.database import Base


# 하드웨어 수집 정보에 따라 속성 추가 예정

class Dust(Base):
    __tablename__ = "devicedata"

    # SQLAlchemy가 첫 integer 타입의 PK에 auto increment 속성을 알아서 부여함
    # 필요 여부는 아직 모름 일단 추가
    index = Column(Integer, primary_key=True, autoincrement=True)
    CurrentTime = Column(String, index=True)
    location = Column(String)

    # 미세먼지 데이터
    DustPm10 = Column(Float)
    DustPm25 = Column(Float)
    Humidity = Column(Float)
    Temperature = Column(Float)
    CarbonMonoxide = Column(Float)
    NitrogenDioxide = Column(Float)
    Ethanol = Column(Float)
    Hydrogen = Column(Float)
    Ammonia = Column(Float)
    Methane = Column(Float)
    Propane = Column(Float)
    IsoButane = Column(Float)


class Weather_InfoTable(Base):
    __tablename__ = 'weatherapidata'
    index = Column(Integer, primary_key=True,autoincrement=True)
    getHeatFeelingIdx = Column(Integer)
    getDiscomfortIdx = Column(Integer)
    getUVIdx = Column(String)
    getSenTaIdx = Column(Integer)
    getAirDiffusionIdx = Column(Integer)
    SO2 = Column(Float)
    CO = Column(Float)
    O3 = Column(Float)
    NO2 = Column(Float)
    PM10 = Column(Integer)
    PM25 = Column(Integer)
    collected_time = Column(String)
