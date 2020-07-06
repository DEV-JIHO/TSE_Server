from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

#하드웨어 수집 정보에 따라 속성 추가 예정

class Dust(Base):
    __tablename__ = "dust"

    id = Column(Integer, primary_key=True, index=True)
    Date = Column(String, index=True)
    Uv = Column(String)
    Nitric = Column(String)
    Sulfuric = Column(String)
    Formal = Column(String)
