import mysql.connector, os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL


DB = {
    'drivername': 'mysql',
    'host': 'sangmin9.synology.me',
    'port': '3307',
    'username': os.environ['DBUNAME'],
    'password': os.environ['DBPASS'],
    'database': os.environ['DBNAME'],
    'query': {'charset':'utf8'}
}

ENGINE = create_engine(URL(**DB))

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するか
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

# modelで使用する
Base = declarative_base()
# DB接続用のセッションクラス、インスタンスが作成されると接続する
Base.query = session.query_property()
