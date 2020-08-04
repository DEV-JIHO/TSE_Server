import time
from fastapi import FastAPI, Depends
from typing import List  # ネストされたBodyを定義するために必要
from starlette.middleware.cors import CORSMiddleware  # CORSを回避するために必要
from sqlalchemy.orm import Session
from .db import session  # DBと接続するためのセッション
from .model import UserTable, User, Weather_InfoTable  # 今回使うモデルをインポート
from weatherApp import WeatherApi


app = FastAPI()

# CORSを回避するために設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

# ----------APIの定義------------
# テーブルにいる全ユーザ情報を取得 GET
@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    users = db.query(UserTable).all()
    return users

@app.get("/dust")
def read_dust(db: Session = Depends(get_db)):
    now = time.localtime()
    date = f"{now.tm_year}{now.tm_mon:02d}{now.tm_mday:02d}{now.tm_hour:02d}"
    lasttime = ''
    print("Time passed.\nGet the api data")
    result, lasttime = WeatherApi.get_all_api_data(date, lasttime)
    lasttime = date
    result['collected_time'] = lasttime
    print(result['collected_time'])
    Weather = Weather_InfoTable()
    Weather.getHeatFeelingIdx = result['getHeatFeelingIdx']
    Weather.getDiscomfortIdx = result['getDiscomfortIdx']
    Weather.getUVIdx = result['getUVIdx']
    Weather.getSenTaIdx = result['getSenTaIdx']
    Weather.getAirDiffusionIdx = result['getHeatFeelingIdx']
    Weather.SO2 = result['SO2']
    Weather.CO = result['CO']
    Weather.O3 = result['O3']
    Weather.NO2 = result['NO2']
    Weather.PM10 = result['PM10']
    Weather.PM25 = result['PM25']
    Weather.collected_time = lasttime
    print('여기는 안전한가?')
    db.add(Weather)
    db.commit()
    print('여기는 안전한가?')

    info = db.query(Weather_InfoTable).all()
    return info

# idにマッチするユーザ情報を取得 GET
@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = session.query(UserTable).\
        filter(UserTable.id == user_id).first()
    return user

# ユーザ情報を登録 POST
@app.post("/user")
# クエリでnameとstrを受け取る
# /user?name="三郎"&age=10
async def create_user(name: str, age: int, db: Session = Depends(get_db)):
    user = UserTable()
    user.name = name
    user.age = age
    db.add(user)
    db.commit()


# 複数のユーザ情報を更新 PUT
@app.put("/users")
# modelで定義したUserモデルのリクエストbodyをリストに入れた形で受け取る
# users=[{"id": 1, "name": "一郎", "age": 16},{"id": 2, "name": "二郎", "age": 20}]
async def update_users(users: List[User]):
    for new_user in users:
        user = session.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        session.commit()
