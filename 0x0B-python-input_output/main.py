#!/usr/bin/python3
Student = __import__('10-student').Student

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', True])
j_student_3 = student_2.to_json([10, 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)
