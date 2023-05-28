from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# @で始まるものはデコレータ，直下の関数を実行する
# @app.get("/contries/japan")   # パスオペレーション
# async def contry():
#     return {"message": 'This is Japan!'}

# @app.get("/contries/{contry_name}")   # パスオペレーション
# async def contry(contry_name: str):
#     return {"contry_name": contry_name}

# ?マーク移行がクエリパラメータ，&でつないで複数クエリが書ける
# パスパラメータが無いが引数が設定されている場合クエリパラメータになる
@app.get("/contries/{contry_name}")
async def contry(contry_name: str = 'japan', city_name: str = 'tokyo'):   #デフォルトの値が設定できる
    return {
        "contry_name": contry_name,
        "city_name": city_name
    }

# オプションパラメータ(必須ではないパラメータ) Optional
@app.get("/contries/")
async def contry(contry_name: Optional[str] = None, contry_no: Optional[int] = None):
    return {
        "contry_name": contry_name,
        "contry_no": contry_no
    }
