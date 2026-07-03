# 📚 Books Management API

A lightweight RESTful API built with **FastAPI** to manage a collection of books.

This project demonstrates:

- CRUD Operations
- Request Validation with Pydantic
- HTTP Exception Handling
- REST API Design

---

## 🚀 Features

- Get all books
- Search books by title
- Search books by author
- Get a book by ID
- Add a new book
- Update an existing book
- Delete a book
- Automatic ID generation
- Data validation using Pydantic
- Proper HTTP status codes

---

## 🛠️ Technologies Used

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic

---

## ▶️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project:

```bash
cd books-management-api
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

---

## ▶️ Run the Server

```bash
py -3.12 -m uvicorn main:app --reload --port 8080
```

---

## 📖 API Documentation

After starting the server, open:

Swagger UI

```
http://localhost:8080/docs
```

---

## 📌 Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /books | Get all books |
| GET | /books/{id} | Get book by ID |
| POST | /books | Add a new book |
| PUT | /books/{id} | Update a book |
| DELETE | /books/{id} | Delete a book |

---

## 🎯 Learning Goals

This project was created to practice:

- FastAPI fundamentals
- REST APIs
- CRUD operations
- Routing
- Request validation
- HTTP exception handling