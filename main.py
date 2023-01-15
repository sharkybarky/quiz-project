from data import question_data_alt
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(question_dict["question"], question_dict["correct_answer"])
                 for question_dict in question_data_alt]
brain = QuizBrain(question_bank)
brain.run_quiz()
