# 📚 Books Management API

A lightweight RESTful API built with **FastAPI** to manage a collection of books. This project demonstrates basic CRUD operations, request validation using Pydantic, and explicit HTTP exception handling.

## 🚀 Features
- **Get Books:** Retrieve all books, or filter them dynamically by `author` or `title`.
- **Get Book by ID:** Fetch a specific book with error handling (`404 Not Found`).
- **Add Book:** Append new books to the list with automatic ID generation.
- **Update Book:** Modify existing book properties safely.
- **Delete Book:** Remove books from the collection securely.

## 🛠️ How to Run the Project

1. Ensure you have Python installed.
2. Run the Uvicorn server on a custom port to avoid local conflicts:
   ```bash
   py -3.12 -m uvicorn main:app --reload --port 8080