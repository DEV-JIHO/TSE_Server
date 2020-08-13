from fastapi import FastAPI, Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.database import session
from app.api import crud

# models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
async def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@router.get("/start")
async def read_root():
    message = "Start API!"
    return {"message": message}


@router.post("/creat_apidata/")
def create_apidata(db: Session = Depends(get_db)):
    return crud.create_apidata(db=db)
