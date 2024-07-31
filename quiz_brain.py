class QuizBrain:
    # Below is the constructor.
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        self.answered = 0

        '''
        Checks if there are still questions remaining to be asked and if 
        so it will return true, else false
        '''

    def still_has_questions(self):
        if len(self.question_list) == self.question_number:
            return False
        else:
            return True

    # Gives you the next question. 
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        self.check_answer(user_answer, current_question.answer)  # Notice how you are calling the method
        # I believe that self refers to the object being used.

    # You are passing user and correct_answer values over.
    def check_answer(self, user_answer, current_question):
        self.answered += 1
        if user_answer.lower() == current_question.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f'The correct answer was: {current_question}.')
        print(f'Your current score is: {self.score}/{self.answered}.')
        print('\n')


