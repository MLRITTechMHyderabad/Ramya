students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
]

# Convert list to dictionary
student_dict = dict(students)

# Print dictionary (optional)
print(student_dict)

# Get user input for a specific student's grade
student_name = input("Enter student name (to find avg grade): ")
if student_name in student_dict:
    average_score = sum(student_dict[student_name]) / len(student_dict[student_name])
    print("Grade:", average_score)
else:
    print("Student not found!")

# Function to find student with the highest average
def find_topper():
    max_average = 0
    best_student = ""

    for name, marks in student_dict.items():
        avg_marks = sum(marks) / len(marks)
        if avg_marks > max_average:
            max_average = avg_marks
            best_student = name
    
    print(f"Top student: {best_student} with an average grade of {max_average}")

# Call the function
find_topper()

# Count number of students who passed
passed_students = sum(1 for marks in student_dict.values() if sum(marks) / len(marks) >= 50)
print(f"Number of students who passed: {passed_students}")