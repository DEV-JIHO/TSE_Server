from sqlalchemy.orm import Session
import datetime

from . import models, schemas

# 미세먼지 관련 함수
# 받을 정보에 따라서 추가 예정

def get_dusts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dust).offset(skip).limit(limit).all()


def create_dust(db: Session, dust: schemas.DustCreate):
    db_dust = models.Dust(Date=str(datetime.datetime.now()),
                          Uv=dust.Uv,
                          Nitric=dust.Nitric,
                          Sulfuric=dust.Sulfuric,
                          Formal=dust.Formal)
    db.add(db_dust)
    db.commit()
    db.refresh(db_dust)
    return db_dust
