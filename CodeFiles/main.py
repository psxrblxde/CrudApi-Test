from urllib import request

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Model(BaseModel):
    username: str
    password: int
    id: int
@app.post('/create')
def create(Model: id):

    return {'id': Model}

@app.get ('/users')
def list_users():
    return {"Users": Model.username}

@app.get('/users/{id}')
def get_users():
    return {'id': id}

@app.put('/update')
def update():
 Model.__call__(UserModel)

@app.delete('/delete/{id}')
def delete(id: int):
    return {'id': id}

