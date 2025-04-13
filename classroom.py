from school import School
from subject import Subject
class ClassRoom:
    def __init__(self,name):
        self.name=name
        self.subjects=[]
        self.students=[]
    def add_student(self,student):
        student.id=f"{self.name}-{len(self.students)+1}"
        self.students.append(student)
    def add_subject(self,subject):
        self.subjects.append(subject)

    def take_semester(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.final_grade()        
            
        