from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = []

# This will add all the questions into the list question_bank
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    next_question = Question(question_text, question_answer) # creating an object
    question_bank.append(next_question)

'''
# Note that this does the same thing
for i in range(len(question_data)):
    q_text = question_data[i]['text']
    q_answer = question_data[i]['answer']
    question = Question(q_text, q_answer)
    question_bank.append(question)
'''
# print(question_bank[0].answer)

'''
We are passing through the questions to the QuizBrain class and also creating
a object called ques. 
'''

ques = QuizBrain(question_bank) # creating another object
while ques.still_has_questions():
    ques.next_question()

# This will be the final code output that shows your score.
print("You've have completed the quiz")
print(f'Your final score was: {ques.score}/{ques.answered}')