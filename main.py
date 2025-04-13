from classroom import ClassRoom
from person import Person,Student,Teacher
from subject import Subject
from school import School

school=School("ABC","Dhaka")

eight=ClassRoom("Eight")
nine=ClassRoom("Nine")
ten=ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim=Student("Rahim",eight)
karim=Student("Karim",ten)
hamim=Student("Hamim",nine)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(hamim)

abul=Teacher("Abul Khan")
babul=Teacher("Babul Khan")
kabul=Teacher("Kabul Khan")


cse=Subject("CSE",kabul)
math=Subject("Math",abul)
physics=Subject("Physics",babul)

eight.add_subject(physics)
nine.add_subject(math)
ten.add_subject(cse)

eight.take_semester()



