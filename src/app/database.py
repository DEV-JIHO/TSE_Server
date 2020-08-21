import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# DB 연결 정보
DB = {
    'drivername': 'mysql',
    'host': '',
    'port': '',
    'username': "",
    'password': "",
    'database': "",
    'query': {'charset': 'utf8'}
}

ENGINE = create_engine(URL(**DB))

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()

Base.query = session.query_property()
