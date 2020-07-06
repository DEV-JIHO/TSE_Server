from typing import List

from fastapi import Depends, FastAPI, HTTPException
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


@app.get("/dust/", response_model=List[schemas.Dust])
def read_dusts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dusts = crud.get_dusts(db, skip=skip, limit=limit)
    return dusts
