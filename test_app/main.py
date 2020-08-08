from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from .database import session
from test_app.crud import *

# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
async def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.post("/creat_dustdata/")
def create_dust(dust: schemas.DustCreate, db: Session = Depends(get_db)):
    return create_dust(db=db, dust=dust)


# 위치 정보에 따라서 값을 반환
# 위치를 좌표로 받기 때문에 이 부분을 어떻게 할 것인가 상의
@app.get("/dust/all")
async def read_dusts(db: Session = Depends(get_db)):
    dusts = get_dusts(db)
    return dusts


@app.get("/creat_apidata/")
async def create_apidata(db: Session = Depends(get_db)):
    return create_apidata(db=db)
