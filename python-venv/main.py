from fastapi import FastAPI

app = FastAPI()


@app.get('/hleb')
def func():
    return 'hello gleb'



@app.get('/test/{name}')
def home(name:str):
    return f'<h1>{name}</h1>'





