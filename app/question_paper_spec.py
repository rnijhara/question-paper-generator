from typing import Dict

from app.question_difficulty import Difficulty


class QuestionPaperSpec:
    def __init__(self, marks: int, difficulty_percent: Dict[Difficulty, int]):
        self.marks = marks
        self.difficulty_percent = difficulty_percent

    def get_marks(self, difficulty: Difficulty) -> int:
        return int(self.marks * self.difficulty_percent[difficulty]/100)
