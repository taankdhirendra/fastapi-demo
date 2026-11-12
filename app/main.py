from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Student Management API",
    description="FastAPI project with GitHub Actions CI/CD",
    version="1.0.0"
)

# Sample database
students = {
    1: {"id": 1, "name": "Rahul", "age": 20},
    2: {"id": 2, "name": "Amit", "age": 22}
}


class Student(BaseModel):
    name: str
    age: int


@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


@app.get("/students")
def get_students():
    return list(students.values())


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    return students[student_id]


@app.post("/students")
def create_student(student: Student):
    student_id = max(students.keys(), default=0) + 1

    students[student_id] = {
        "id": student_id,
        "name": student.name,
        "age": student.age
    }

    return students[student_id]


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    students[student_id] = {
        "id": student_id,
        "name": student.name,
        "age": student.age
    }

    return students[student_id]


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    del students[student_id]

    return {"message": "Student deleted successfully"}
