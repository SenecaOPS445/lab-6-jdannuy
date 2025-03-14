#!/usr/bin/env python3
# Author ID: jdannuy

#!/usr/bin/env python3
# Author ID: [seneca_id]

class Student:
    # Initialize the student object
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure student number is always a string
        self.courses = {}

    # Display student details
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # Add a new course and grade
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate and return GPA safely
    def displayGPA(self):
        if not self.courses or all(grade == 0.0 for grade in self.courses.values()):
            return f'GPA of student {self.name} is 0.0'  # Avoid ZeroDivisionError
        gpa = sum(self.courses.values()) / len(self.courses)
        return f'GPA of student {self.name} is {gpa:.1f}'

    # Return a list of passed courses (grade > 0.0)
    def displayCourses(self):
        return [course for course, grade in self.courses.items() if grade > 0.0]


if __name__ == '__main__':
    # Create first student object and add grades
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades
    student2 = Student('Jessica', 123456)  # Now works with an integer
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display results for student1
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display results for student2
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
