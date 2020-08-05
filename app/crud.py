from sqlalchemy.orm import Session
import arrow, time

from . import models, schemas
from weatherApp import WeatherApi


# 미세먼지 관련 함수
# 받을 정보에 따라서 추가 예정

def get_dusts(db: Session):
    return db.query(models.Dust).all()


def get_dustId(db: Session, dust_id: int = 0):
    return db.query(models.Dust).get(dust_id)


def create_dust(db: Session, dust: schemas.DustCreate):
    measure_time = arrow.utcnow().to('Asia/Seoul').format(arrow.FORMAT_RFC1123)
    db_dust = models.Dust(CurrentTime=str(measure_time),
                          location=dust.location,
                          DustPm10=dust.DustPm10,
                          DustPm25=dust.DustPm25,
                          Humidity=dust.Humidity,
                          Temperature=dust.Temperature,
                          CarbonMonoxide=dust.CarbonMonoxide,
                          NitrogenDioxide=dust.NitrogenDioxide,
                          Ethanol=dust.Ethanol,
                          Hydrogen=dust.Hydrogen,
                          Ammonia=dust.Ammonia,
                          Methane=dust.Methane,
                          Propane=dust.Propane,
                          IsoButane=dust.IsoButane,
                          )
    db.add(db_dust)
    return db_dust


def create_apidata(db: Session):
    now = time.localtime()
    date = f"{now.tm_year}{now.tm_mon:02d}{now.tm_mday:02d}{now.tm_hour:02d}"
    lasttime = ''
    print("Time passed.\nGet the api data")
    result, lasttime = WeatherApi.get_all_api_data(date, lasttime)
    lasttime = date
    result['collected_time'] = lasttime
    print(result['collected_time'])
    weather = models.Weather_InfoTable()
    weather.getHeatFeelingIdx = result['getHeatFeelingIdx']
    weather.getDiscomfortIdx = result['getDiscomfortIdx']
    weather.getUVIdx = result['getUVIdx']
    weather.getSenTaIdx = result['getSenTaIdx']
    weather.getAirDiffusionIdx = result['getHeatFeelingIdx']
    weather.SO2 = result['SO2']
    weather.CO = result['CO']
    weather.O3 = result['O3']
    weather.NO2 = result['NO2']
    weather.PM10 = result['PM10']
    weather.PM25 = result['PM25']
    weather.collected_time = lasttime
    db.add(weather)

    info = db.query(models.Weather_InfoTable).all()
    return info

