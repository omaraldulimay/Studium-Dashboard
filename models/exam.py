
from dataclasses import dataclass
from .module import Module

@dataclass
class Exam(Module):
    attempt: int = 1

    def retake(self):
        """Neue Prüfung schreiben"""
        self.attempt += 1
        self.grade = None

