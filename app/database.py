from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# database URL 필요
# 接続したいDBの基本情報を設定
user_name = "madang"
password = "madang"
host = "localhost"  # docker-composeで定義したMySQLのサービス名
database_name = "dustdata"

#SQLALCHEMY_DATABASE_URL = "mysql://user:password@localhost/tse?charset=utf8"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# 接続したいDBの基本情報を設定
DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)


engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するか
    sessionmaker(
        autocommit=True,
        autoflush=True,
        bind=engine
    )
)

Base = declarative_base()

Base.query = session.query_property()