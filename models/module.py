
from dataclasses import dataclass

@dataclass
class Module:
    name: str
    ects: int
    grade: float | None = None   # None = noch nicht abgeschlossen

    @property
    def passed(self) -> bool:
        return self.grade is not None and self.grade <= 4.0

