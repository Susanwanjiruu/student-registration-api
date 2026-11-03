# Student Registration API

A small FastAPI application for managing student, teacher, and course records using SQLite.

## Project structure

```text
app/
├── database.py
├── main.py
├── models/
├── repositories/
├── routers/
├── schemas/
└── services/
```

The application separates database access, data models, request schemas, repository functions, and API routers.

## Requirements

- Python 3.10 or later
- FastAPI
- Uvicorn
- Pydantic

Install the dependencies:

```bash
python -m pip install fastapi uvicorn pydantic
```

## Run locally

From the repository root:

```bash
uvicorn main:app --app-dir app --reload
```

Then open:

- API: http://127.0.0.1:8000
- Interactive API documentation: http://127.0.0.1:8000/docs

The SQLite database file (`school.db`) is created in the process's current working directory when the application starts.

## Available API areas

- `/students` — student records
- `/teacher` — teacher records
- `/courses/courses` — course records

Use the interactive API documentation at `/docs` to inspect the available operations and request schemas.

## Important limitations

This repository is an educational/demo project, not a production-ready student information system.

- The API currently has no authentication or role-based access control.
- Personal information, including email addresses and ID numbers, is stored by the application.
- The database uses a local SQLite file and does not include a migration workflow.
- Input validation, error handling, and automated test coverage should be strengthened before real-world use.
- Do not use real student or staff personal information when experimenting with this demo.

## Repository hygiene

Python bytecode, cache directories, local virtual environments, SQLite database files, and environment-variable files are excluded through `.gitignore`.
