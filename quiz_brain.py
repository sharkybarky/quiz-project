from question_model import Question


class QuizBrain:
    """ Abstract the inner workings of the game from the player
    """
    def __init__(self, question_bank: [Question]):
        self.question_number = 0
        self.score = 0
        self.question_bank = question_bank

    def next_question(self):
        question = self.question_bank[self.question_number]
        user_answer = input(f"Q{self.question_number + 1})"
                            f" {question.text} (True/False): ")
        self.question_number += 1
        self.check_answer(user_answer, question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.lower() == correct_answer.lower():
            print("You are correct!")
            self.score += 1
        else:
            print("Sorry, that is wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your score is: {self.score}")

    def run_quiz(self):
        while self.still_has_questions():
            self.next_question()
            print("\n")

        print(f"Your final score was {self.score}/{self.question_number}")
