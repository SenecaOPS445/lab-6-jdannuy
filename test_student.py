from student import Student

# Create student objects
student1 = Student('John', '013454900')
student2 = Student('Jessica', '023384103')

# Display student details
student1.displayStudent()
student2.displayStudent()

# Add grades for student1
student1.addGrade('uli101', 4.0)
student1.addGrade('ops245', 3.5)
student1.addGrade('ops445', 3.0)

# Add grades for student2
student2.addGrade('ipc144', 4.0)
student2.addGrade('cpp244', 4.0)

# Display courses
print(student1.name, student1.courses)
print(student2.name, student2.courses)

# Display GPA
student1.displayGPA()
student2.displayGPA()
