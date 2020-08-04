from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from . import crud, models, schemas
from .database import session, engine
from .models import UserTable

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.post("/creat_dustdata/")
def create_dust(dust: schemas.dustCreate, db: Session = Depends(get_db)):
    return crud.create_dust(db=db, dust=dust)


# 위치 정보에 따라서 값을 반환
# 위치를 좌표로 받기 때문에 이 부분을 어떻게 할 것인가 상의
@app.get("/dust/all", response_model=List[schemas.Dust])
async def read_dusts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dusts = crud.get_dusts(db, skip=skip, limit=limit)
    return dusts


@app.get("/get_dustdata/{dust_id}", response_model=schemas.Dust)
async def read_dusts(dust_id: int = 0, db: Session = Depends(get_db)):
    dusts = crud.get_dustId(db, dust_id=dust_id)
    return dusts


@app.post("/user")
async def create_user(name: str, age: int):
    user = UserTable()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()

@app.get("/users")
def read_users():
    print("흑흑")
    users = session.query(UserTable).all()
    return users