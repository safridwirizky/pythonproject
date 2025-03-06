from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_bank.append(Question(i['text'], i['answer']))

QuizBrain(question_bank).next_question()





















