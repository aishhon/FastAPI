from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/greet')
def greet():
    return {"message": "Hello from FastAPI!"}

#path parameter
@app.get('/greet/{name}')
def greet_name(name: str):
    return {"message": f"Hello, {name}!"}

#path & query parameters
@app.get('/query/{name}')
def greet_name(name: str, age: int):
    return {"message": f"Hello, {name}! You are {age} years old."}

#optional query parameter
@app.get('/optional_query/{name}')
def greet_name(name: str, age: Optional[int] = None):
    if age:
        return {"message": f"Hello, {name}! You are {age} years old."}
    else:
        return {"message": f"Hello, {name}!"}

#POST METHOD
class Student(BaseModel):
    name:str
    age:int
    roll_no:int

@app.post('/student')
def create_student(student:Student):
    return{
        "name": student.name,
        "age": student.age,
        "roll_no": student.roll_no
    }
