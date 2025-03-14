#!/usr/bin/env python3
# Author ID: Jhanlyn Brita Dannuy - jdannuy

class Student:
    # Define name and student ID number
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    # Display student name and number
    def displayStudent(self):
        print('Student Name: ' + self.name)
        print('Student Number: ' + self.number)

    # Add a new course and grade to the student record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate and display GPA
    def displayGPA(self):
        gpa = 0.0
        for course in self.courses.keys():
            gpa += self.courses[course]
        print(f'GPA of student {self.name} is {gpa / len(self.courses):.2f}')
