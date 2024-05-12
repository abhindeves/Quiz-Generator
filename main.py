from teacher import Teacher
from exam_simulator import Exam
import logging

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO)
## Create a Teacher Instance which ask about the topic, number of question and possible answer

teacher = Teacher()
student_view, answers = teacher.create_full_test()


exam = Exam(student_view,answers)
student_answers = exam.take()


grade = exam.grade(student_answers)
print(grade)


