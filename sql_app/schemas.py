from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# 유저 관련 함수

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


# 미세먼지 관련 함수

class DustBase(BaseModel):
    Uv: str
    Nitric: str
    Sulfuric: str
    Formal: str

    class Config:
        orm_mode = True



class DustCreate(DustBase):
    pass


class Dust(DustBase):
    id: int

