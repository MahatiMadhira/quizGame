from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for q_data in question_data:
    q_text = q_data["question"]
    q_answer = q_data["correct_answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_q()

print(f"You have completed the Quiz. Your final score is: {quiz.score}/{len(question_bank)}")
