from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# 미세먼지 관련 함수

def get_dusts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dust).offset(skip).limit(limit).all()


def create_dust(db: Session, dust: schemas.Dust):
    db_dust = models.Dust(Uv=dust.Uv,
                          Nitric=dust.Nitric,
                          Sulfuric=dust.Sulfuric,
                          Formal=dust.Formal)
    db.add(db_dust)
    db.commit()
    db.refresh(db_dust)
    return db_dust
