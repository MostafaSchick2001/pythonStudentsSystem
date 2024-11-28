import uuid


class Student:
    def __init__(self, number ,name, lastname):
        self.number = number
        self.name = name
        self.lastname = lastname
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
    def remove_course(self , course):
        self.courses.remove(course)
    def print_course(self):
        [print(c.name) for c in self.courses]


class Course:
    def __init__(self, name):
        self.name = name
        self.course_id = uuid.uuid4()
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def remove_student(self, student):
        self.students.remove(student)
    def print_students(self):
        [print(s.name + s.lastname) for s in self.students]


class Grading:
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade



def main():
    students = []
    exercises = []
    print("""
--------Willkommen--------
1 : Add student
2 : Add exercise grading
3 : View Exercise
4 : View Student
5:  Exit
""")
    choice = ""
    while True:
        choice = input("Enter a number from 1 to 4:\n")
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid Input, try again")
        else:
            break

    if choice == "1":
        print("Enter the data of a new student")
        number = int(input("Student Number: "))
        name = input("Student Name: ")
        lastname = input("Student Lastname: ")
        student = Student(number, name, lastname)
        #add the student
        if student in students:
            print("Student exists!")
            #gib einen wertgit
        else:
            students.append(student)
            print(students)
        if len(exercises) > 0 : #existieren exercises
            for exercise in exercises:
                print(exercise.name)
        else:
            return
    elif choice == "2":
        print(2)
    elif choice == "3":
        print(3)

    else:
        print(4)



if __name__ == "__main__":
    main()