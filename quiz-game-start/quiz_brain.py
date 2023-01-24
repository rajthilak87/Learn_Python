from data import question_data

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    current_question = ""
    def still_has_question(self):
        return self.question_number < len(question_data)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.ans = input(f"Q {self.question_number} : {current_question.text} (true / false) : ")
        print(current_question.answer)
        
    def check_answer(self):
        if self.current_question.answer == self.ans:
            print("You got it and scored 1")            
            print(f" Present score is {self.score}")
        else:
            print("You are wrong and haven't scored")
         
    def check_score(self):
        self.score +=1
        if self.question_number >= 12:
            print("\n")
            print("Quiz is completed")
            print("\n")
            print(f"Your Final Score  is {self.score}")   
        
            
            

