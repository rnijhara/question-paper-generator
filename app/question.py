from app.question_difficulty import Difficulty


class Question:

    def __init__(self, question_id: str, difficulty: Difficulty, marks: int):
        self.question_id = question_id
        self.difficulty = difficulty
        self.marks = marks

    def __repr__(self):
        return 'Question = {0} {1} {2}'.format(self.question_id, self.difficulty, self.marks)
