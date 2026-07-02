from fastapi import FastAPI
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
async def get_book(author: str = None, limit: int = 10):
    if author:
        filter_author = []
        for book in Book:
            if book["author"].lower() == author.lower():
                filter_author.append(book)
        return filter_author[:limit]
    return Book[:limit]
@app.get("/Book/{book_id}")
async def get_book_by_id(book_id: int):
    for book in Book:
        if book["id"] == book_id:
            return book 

    return {"error": "Book not found"}
@app.post("/Book")
async def post_book(bookadded: BaseSchema):
    book_added= bookadded.model_dump()
    Book.append(book_added)
    return {"message": "Book was added", "book": book_added}
@app.put("/Book/{book_id}")
async def put_book(book_id: int, bookupdated: BookUpdateSchema):
    for book in Book:
        if book["id"] == book_id:
            updated_book = bookupdated.model_dump()
            book["title"] = updated_book["title"]
            book["author"] = updated_book["author"]
            return {"message" : "Book was updated", "The book": book}
    return {"Error" : "The book does not exist"}
@app.delete("/Book/{book_id}")
async def delete_book(book_id: int):
    for book in Book :
        if book["id"] == book_id:
            Book.remove(book)
            return {"Message" :"The book was deleted"}
    return {"Error" :"The book does not presented"}