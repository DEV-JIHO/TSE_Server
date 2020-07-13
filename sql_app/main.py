from typing import List
import time

from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 미세먼지 데이터 관련 함수 추가
# 주고 받을 정보에 따라 추가 예정


@app.post("/dust/")
def create_dust(dust: schemas.dustCreate, db: Session = Depends(get_db)):
    return crud.create_dust(db=db, dust=dust)


# 위치 정보에 따라서 값을 반환
# 위치를 좌표로 받기 때문에 이 부분을 어떻게 할 것인가 상의
@app.get("/dust/all", response_model=List[schemas.Dust])
async def read_dusts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dusts = crud.get_dusts(db, skip=skip, limit=limit)
    return dusts


@app.get("/dust/{dust_id}", response_model=schemas.Dust)
async def read_dusts(dust_id: int = 0, db: Session = Depends(get_db)):
    dusts = crud.get_dustId(db, dust_id=dust_id)
    return dusts
