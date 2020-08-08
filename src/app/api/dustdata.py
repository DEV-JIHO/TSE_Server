from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import session
from app.api.schemas import DustCreate
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


@router.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python"
    return {"message": message}


@router.post("/creat_dustdata/")
def create_dust(dust: DustCreate, db: Session = Depends(get_db)):
    return crud.create_dust(db=db, dust=dust)
