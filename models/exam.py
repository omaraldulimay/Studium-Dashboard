
from dataclasses import dataclass
from .module import Module

@dataclass
class Exam:
    module: Module
    attempt: int = 1
    grade: float | None = None
    
    def retake(self):
        """Neue Prüfung schreiben"""
        self.attempt += 1
        self.grade = None

