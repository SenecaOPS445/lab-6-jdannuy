#!/usr/bin/env python3
# Author ID: Jhanlyn Brita Dannuy - jdannuy


#!/usr/bin/env python3
# Author ID: [seneca_id]  # Replace with your actual Seneca ID

class Student:
    # Constructor to initialize name, student number, and an empty courses dictionary
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    # Method to display student details
    def displayStudent(self):
        print('Student Name: ' + self.name)
        print('Student Number: ' + self.number)

    # Method to add a course and grade
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Method to calculate and display GPA
    def displayGPA(self):
        if len(self.courses) == 0:
            print('No courses available to calculate GPA.')
            return
        
        gpa = sum(self.courses.values()) / len(self.courses)
        print(f'GPA of student {self.name} is {gpa:.2f}')
