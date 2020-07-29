from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


# 하드웨어 수집 정보에 따라 속성 추가 예정

class Dust(Base):
    __tablename__ = "dust"

    # SQLAlchemy가 첫 integer 타입의 PK에 auto increment 속성을 알아서 부여함
    # 필요 여부는 아직 모름 일단 추가
    id = Column(Integer, primary_key=True, index=True)
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
