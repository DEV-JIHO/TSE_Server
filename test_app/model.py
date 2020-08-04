# -*- coding: utf-8 -*-
# モデルの定義
from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from .db import Base
from .db import ENGINE


# userテーブルのモデルUserTableを定義
class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)


# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class User(BaseModel):
    id: int
    name: str
    age: int


class Weather_InfoTable(Base):
    __tablename__ = 'weather_info'
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


class Weather_Info(BaseModel):
    getHeatFeelingIdx: int
    getDiscomfortIdx: int
    getUVIdx: int
    getSenTaIdx: int
    getAirDiffusionIdx: int
    SO2: float
    CO: float
    O3: float
    NO2: float
    PM10: int
    PM25: int
    collected_time: str



def main():
    # テーブルが存在しなければ、テーブルを作成
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
