
from dataclasses import dataclass, field
from typing import List
from .module import Module

@dataclass
class Student:
    name: str
    modules: List[Module] = field(default_factory=list)

    @property
    def ects_total(self) -> int:
        return sum(m.ects for m in self.modules if m.passed)

    @property
    def average_grade(self) -> float:
        grades = [m.grade for m in self.modules if m.grade is not None]
        return round(sum(grades) / len(grades), 2) if grades else 0.0
