from app.question_difficulty import Difficulty
from app.question_paper_generator import QuestionPaperGenerator
from app.question_paper_spec import QuestionPaperSpec

if __name__ == '__main__':
    question_paper_generator = QuestionPaperGenerator()
    question_paper_spec = QuestionPaperSpec(20, {
        Difficulty.EASY: 25,
        Difficulty.MEDIUM: 50,
        Difficulty.HARD: 25
    })
    try:
        easy, medium, hard = question_paper_generator.generate(question_paper_spec)
        print('easy', *list(map(lambda x: x.question_id, easy)), sep=" ")
        print('medium', *list(map(lambda x: x.question_id, medium)), sep=" ")
        print('hard', *list(map(lambda x: x.question_id, hard)), sep=" ")
    except Exception as e:
        print(e)
