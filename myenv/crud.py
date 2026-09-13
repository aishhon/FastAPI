from os import stat
from unittest.mock import Base

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

books=[
    {
        'id':1,
        'title':"Book 1", 
        'author':"Author 1",
        'published_date':"2020-01-01"
    },
    {
        'id':2,
        'title':"Book 2",
        'author':"Author 2",
        'published_date':"2021-01-01"
    },
    {
        'id':3,
        'title':"Book 3",
        'author':"Author 3",
        'published_date':"2022-01-01"
    },
    {
        'id':4,
        'title':"Book 4",
        'author':"Author 4",
        'published_date':"2023-01-01"
    }

]

app=FastAPI()

@app.get('/books')
def get_books():
    return books

#get a book by its id
@app.get('/books/{book_id}')
def get_book(book_id:int):
    for book in books:
        if book['id']==book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")

class Book(BaseModel):
    id:int
    title:str
    author:str
    published_date:str

@app.post('/books')
def create_book(book:Book):
    new_book=book.model_dump()
    books.append(new_book)

#update the data in our list
class BookUpdate(BaseModel):
    title:str
    author:str
    published_date:str

    
@app.put('/books/{book_id}')
def update_book(book_id:int,book_update:BookUpdate):
    for book in books:
        if book['id']==book_id:
            book['title']=book_update.title
            book['author']=book_update.author
            book['published_date']=book_update.published_date
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='book not found')

@app.delete('/books/{book_id}')
def delete_book(book_id:int):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return {"message":"Book deleted successfully"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='book not found')
