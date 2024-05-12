# Do the imports here
import logging

from test_creator import TestGenerator

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO)

class Teacher():
    
    def __init__(self):
        
        print("Welcome to Quizz Creator!!")
        
        
    def create_full_test(self):
        
        topic = input("What topic do you want to create: ")
        num_questions = int(input("Enter the number of questions you need: "))
        num_possible_answers = int(input("Enter the number of possible answers for each questions: "))
        
        # Create Object of class TestGenerator
        self.test_creator = TestGenerator(topic, num_questions, num_possible_answers)
        test = self.test_creator.run()
 
        student_view = self.create_student_view(test, num_questions)
        answers = self.extract_answers(test, num_questions)

        return student_view, answers
    
    def create_student_view(self,test,num_question):
        questions = {1:''}
        question_number = 1
        question_block = test.split("\n")
        question_block = [block.strip() for block in question_block]
        for block in question_block:
            if not block.startswith("Answer: "):
                questions[question_number] += block+'\n'
            else:
                if question_number < num_question:
                    question_number += 1
                    questions[question_number] = ''
        return questions
        
        
    def extract_answers(self,test,num_question):
        answer = {1:''}
        question_number = 1
        question_block = test.split("\n")
        question_block = [block.strip() for block in question_block]
        for block in question_block:
            if  block.startswith("Answer: "):
                answer[question_number] +=  block+'\n'
                if question_number < num_question:
                    question_number += 1
                    answer[question_number] = ''
        return answer


# if __name__ == "__main__":
#     teacher = Teacher()
#     student_view, answers = teacher.create_full_test()
#     print(student_view)
#     print(answers)
    
    
    
    
    
    
    
    
