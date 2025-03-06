class QuizBrain():
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
        for i in self.question_list:
            answer = input(f"Q{self.question_number+1}: {self.question_list[0].text} ('True' or 'False'): ")
            
            if answer == self.question_list[self.question_number].answer:
                self.score += 1
                print(f"Thats right.\nThe answer is '{self.question_list[self.question_number].answer}'")
                
                self.question_number += 1
                print(f"Your score {self.score}/{self.question_number}")
            
            else:
                print(f"Your answer is wrong.\nThe answer is '{self.question_list[self.question_number].answer}'")
                
                self.question_number += 1
                print(f"Your score {self.score}/{self.question_number}")