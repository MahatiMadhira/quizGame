class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.score = 0
        self.question_list = q_list

    def next_q(self):
        current_q = self.question_list[self.q_number]
        self.q_number += 1
        choice = input(f"Q.{self.q_number}: {current_q.text} (True/False): ")
        self.check_answer(choice, current_q.answer)

    def still_has_questions(self):
        return self.q_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"You got it wrong.")

        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.q_number}")
        print("\n")
