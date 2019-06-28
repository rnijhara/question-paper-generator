import random

from app.question_difficulty import Difficulty
from app.question_paper_spec import QuestionPaperSpec
from app.question_store import QuestionStore
from app.subset_sum import SubsetSum


class QuestionPaperGenerator:
    def __init__(self):
        self.question_store = QuestionStore()
        self.subset_sum = SubsetSum()
        self.easy_questions = self._filter_by_difficulty(Difficulty.EASY)
        self.medium_questions = self._filter_by_difficulty(Difficulty.MEDIUM)
        self.hard_questions = self._filter_by_difficulty(Difficulty.HARD)

    def _filter_by_difficulty(self, difficulty):
        return list(filter(lambda x: x.difficulty == difficulty, self.question_store.questions))

    def generate(self, spec: QuestionPaperSpec):
        easy_questions = self.subset_sum.get_all_subsets(self.easy_questions, spec.get_marks(Difficulty.EASY))
        medium_questions = self.subset_sum.get_all_subsets(self.medium_questions, spec.get_marks(Difficulty.MEDIUM))
        hard_questions = self.subset_sum.get_all_subsets(self.hard_questions, spec.get_marks(Difficulty.HARD))
        if not easy_questions or not medium_questions or not hard_questions:
            raise Exception('Unable to generate questions for given spec')
        return random.choice(easy_questions), random.choice(medium_questions), random.choice(hard_questions)
