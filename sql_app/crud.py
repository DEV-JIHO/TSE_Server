from sqlalchemy.orm import Session
import arrow

from . import models, schemas


# 미세먼지 관련 함수
# 받을 정보에 따라서 추가 예정

def get_dusts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dust).offset(skip).limit(limit).all()


def create_dust(db: Session, dust: schemas.dustCreate):
    currentTime = arrow.utcnow().to('Asia/Seoul').format(arrow.FORMAT_RFC1123)
    db_dust = models.Dust(CurrentTime=str(currentTime),
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
    db.commit()
    db.refresh(db_dust)
    return db_dust
