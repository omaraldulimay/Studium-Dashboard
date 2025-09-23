
import json
from models.student import Student, Module

def save_student(student: Student, filename: str = "data/student.json"):
    data = {
        "name": student.name,
        "modules": [{"name": m.name, "ects": m.ects, "grade": m.grade} for m in student.modules]
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_student(filename: str = "data/student.json") -> Student:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    modules = [Module(**m) for m in data["modules"]]
    return Student(name=data["name"], modules=modules)
