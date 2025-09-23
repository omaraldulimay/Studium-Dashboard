
from models.student import Student, Module
from services.dashboard import print_dashboard
from services.storage import save_student, load_student

def main():
    # Beispielstudent
    s = Student(
        name="Omar",
        modules=[
            Module("Programmieren", 10, 1.7),
            Module("Datenbanken", 5, 2.3),
            Module("Data Science", 10, None), # noch offen
        ]
    )

    # Dashboard anzeigen
    print_dashboard(s)

    # Speichern & Laden
    save_student(s)
    s2 = load_student()
    print("\nNach Laden aus JSON:")
    print_dashboard(s2)

if __name__ == "__main__":
    main()
 