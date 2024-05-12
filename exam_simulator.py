

class Exam():
    
    def __init__(self,student_view,answers):
        self.student_view = student_view
        self.answers = answers
    
    # Take the exam

    def take(self):
        
        student_answer = {}
        for question, question_view in self.student_view.items():
            print(question_view)
            answer = input("Enter Your Answer: ")
            student_answer[question] = answer
        return student_answer
    
    def grade(self,student_answers):
        score = 0
        l = len(self.answers)
        for question,answer in self.answers.items():
            ans  = answer.split(":")[1].strip()[0]
            if student_answers[question].lower() == ans.lower():
                score += 1
        return score 