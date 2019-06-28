import json
from typing import List

from app.question import Question
from app.question_difficulty import Difficulty


class QuestionStore:

    def __init__(self):
        self.questions: List[Question] = QuestionStore.load_questions()
        print('All questions =', self.questions)

    @staticmethod
    def load_questions():
        with open('app/questions.json') as f:
            data = json.load(f)
            return list(map(lambda x: Question(x['question_id'], Difficulty(x['difficulty']), x['marks']), data))
