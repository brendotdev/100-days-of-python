class Student:
    school_name = "Python High School"  # Class variable

    def __init__(self, name, grade):
        self.name = name        # Instance variable
        self.grade = grade      # Instance variable

# Create instances
student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

# Modify instance variable
student2.grade = "A+"

# Access class and instance variables
print(f"{student1.name} attends {student1.school_name} and got grade {student1.grade}")
print(f"{student2.name} attends {student2.school_name} and got grade {student2.grade}")

# Modify class variable from class
Student.school_name = "Advanced Python Academy"

print(f"{student1.name} now attends {student1.school_name}")
print(f"{student2.name} now attends {student2.school_name}")
