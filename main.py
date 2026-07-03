from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
Book = [
    {"id": 1, "title": "Harry Potter", "author": "Rowling"},
    {"id": 2, "title": "The Hobbit", "author": "Tolkien"},
    {"id": 3, "title": "The Great Gatsby", "author": "Fitzgerald"}
]
class BaseSchema(BaseModel):
    id: int
    title: str
    author: str
class BookUpdateSchema(BaseModel):
    title: str
    author: str
@app.get("/Book")
async def get_book(author: str = None, title: str = None, limit: int = 10):
    if author:
        filter_author = []
        for book in Book:
            if book["author"].lower() == author.lower():
                filter_author.append(book)
        return filter_author[:limit]
    if title:
        filter_title = []
        for book in Book:
            if book["title"].lower() == title.lower():
                filter_title.append(book)
        return filter_title[:limit]
    return Book[:limit]
@app.get("/Book/{book_id}", response_model=BaseSchema)
async def get_book_by_id(book_id: int):
    for book in Book:
        if book["id"] == book_id:
            return book 
    raise HTTPException(status_code=404, detail="Book not found")
@app.post("/Book", response_model=BaseSchema)
async def post_book(bookadded: BookUpdateSchema):
    book_added= bookadded.dict()
    new_id = len(Book) + 1
    new_book = {"id": new_id, **book_added} 
    Book.append(new_book)
    return new_book
@app.put("/Book/{book_id}", response_model=BaseSchema)
async def put_book(book_id: int, bookupdated: BookUpdateSchema):
    for book in Book:
        if book["id"] == book_id:
            updated_book = bookupdated.dict()
            book["title"] = updated_book["title"]
            book["author"] = updated_book["author"]
            return book
    raise HTTPException(status_code=404, detail="Book not found")
@app.delete("/Book/{book_id}", response_model=BaseSchema)
async def delete_book(book_id: int):
    for book in Book :
        if book["id"] == book_id:
            Book.remove(book)
            return book

    raise HTTPException(status_code=404, detail="Book not found")