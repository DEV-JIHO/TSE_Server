from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


# 하드웨어 수집 정보에 따라 속성 추가 예정

class Dust(Base):
    __tablename__ = "dust"

    # SQLAlchemy가 첫 integer 타입의 PK에 auto increment 속성을 알아서 부여함
    # 필요 여부는 아직 모름 일단 추가
    id = Column(Integer, primary_key=True, index=True)
    Date = Column(String, index=True)
    location = Column(String)
    Uv = Column(String)
    Nitric = Column(String)
    Sulfuric = Column(String)
    Formal = Column(String)
