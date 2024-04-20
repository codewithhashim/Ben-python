# Define a dictionary to store students and their grades
students = {}

def add_student():
    student_name = input("Enter student name: ")
    students[student_name] = []  # Initialize an empty list for grades

def add_grade():
    student_name = input("Enter student name: ")
    if student_name in students:
        grade = float(input("Enter grade: "))
        students[student_name].append(grade)
    else:
        print("Student not found")

def view_grades():
    student_name = input("Enter student name: ")
    if student_name in students:
        grades = students[student_name]
        print(f"Grades for {student_name}: {grades}")
    else:
        print("Student not found")

def calculate_average():
    student_name = input("Enter student name: ")
    if student_name in students:
        grades = students[student_name]
        average = sum(grades) / len(grades)
        print(f"Average grade for {student_name}: {average:.2f}")
    else:
        print("Student not found")

def main():
    while True:
        print("1. Add student")
        print("2. Add grade")
        print("3. View grades")
        print("4. Calculate average grade")
        print("5. EXIT")
        choice = input("Choose an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            view_grades()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()