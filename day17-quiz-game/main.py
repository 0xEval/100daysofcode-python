from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    q = Question(item['question'], item['correct_answer'])
    question_bank.append(q)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    ans = quiz_brain.next_question()
    quiz_brain.check_answer(ans)
