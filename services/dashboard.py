
from models.student import Student

def print_dashboard(student: Student):
    print(f"📊 Dashboard für {student.name}")
    print(f"ECTS erreicht: {student.ects_total}")
    print(f"Durchschnittsnote: {student.average_grade}")
    print("-" * 30)
    for m in student.modules:
        status = "✅ bestanden" if m.passed else "❌ offen"
        print(f"{m.name} ({m.ects} ECTS): {status}, Note: {m.grade}")
