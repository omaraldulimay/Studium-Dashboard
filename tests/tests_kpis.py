from models.module import Module
from models.student import Student

def test_kpis():
    s = Student("X", [Module("A", 5, 1.0), Module("B", 5, None)])
    assert s.ects_total == 5
    assert s.average_grade == 1.0
