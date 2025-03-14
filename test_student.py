from student import Student  # Import the Student class

# Create a student object
student1 = Student('John', '013454900')

# Display student details
student1.displayStudent()

# Add courses and grades
student1.addGrade('uli101', 4.0)
student1.addGrade('ops245', 3.5)
student1.addGrade('ops445', 3.0)

# Display GPA
student1.displayGPA()

# Create another student
student2 = Student('Jessica', '023384103')

# Add courses and grades
student2.addGrade('ipc144', 4.0)
student2.addGrade('cpp244', 4.0)

# Display student2 details and GPA
student2.displayStudent()
student2.displayGPA()
