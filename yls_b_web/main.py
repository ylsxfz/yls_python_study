# _*_ coding: utf-8 _*_
"""
 @Time : 2020/7/24 10:10 
 @Author : yls 
 @Version：V 0.1
 @File : main.py.py
 @desc :FastAPI 是一个现代、高性能 Web 框架，用于构建 APIs，基于 Python 3.6 及以上版本。
        最大特点：快！性能极高，可与 Node.js、Go 媲美。
        基于 Starlette 和 Pydantic，是 FastAPI 如此高性能的重要原因。
        还具备代码复用性高、容易上手、健壮性强的优点。
        FastAPI 还有一个非常强的优势：方便的 API 调试，生成 API 文档，
        直接能够做到调试自己构建的 API，这在实际应用中，价值凸显。
 """

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    friends: list
    


@app.get("/")
def index():
    return {'admin': 'welcome to FastAPI'}


@app.get("/users/{user_id}")
def read_user(user_id: int, name: str = None):
    return {'user_id': user_id, 'name:': name}


@app.get('/users/{user_id}')
def update_user(user_id: int, user: User):
    return {'user_name': user.name, 'user_id': user_id}

