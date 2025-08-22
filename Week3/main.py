from conn import get_connection
from course import list_courses_with_students, list_courses_with_teachers
from student import get_student_by_id,add_student,delete_student
from database import setup_database
from report import show_all_data

def menu():
    while True:
        print("\n--- YOOBEE COLLEGE MENU ---")
        print("1: Which student is enrolled in which course")
        print("2: Which teacher is connected to which course")
        print("3: Search a student by ID")
        print("4: FULL DATA REPORT")
        print("5: Add Student")
        print("6: Delete Student")
        print("7: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data = list_courses_with_students()
            print("\n--- Students Enrolled in Courses ---")
            for student, course in data:
                print(f"{student} → {course}")

        elif choice == "2":
            data = list_courses_with_teachers()
            print("\n--- Teachers Connected to Courses ---")
            for course, teacher in data:
                print(f"{teacher} teaches {course}")

        elif choice == "3":
            student_id = input("Enter Student ID: ")
            student, courses = get_student_by_id(student_id)
            if student:
                print(f"\nStudent ID: {student[0]}")
                print(f"Name: {student[1]}")
                print("Enrolled Courses: " + (", ".join(courses) if courses else "None"))
            else:
                print("No student found with that ID.")

        elif choice == "4":
            print("\n--- FULL DATA REPORT ---")
            for row in show_all_data():
                print(row)

        elif choice == "5":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            add_student(student_id, name)

        elif choice == "6":
            student_id = input("Enter Student ID to delete: ")
            delete_student(student_id)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again!")

def main():
    print("Setting up YOOBEE College database...")
    setup_database()
    menu()

if __name__ == "__main__":
    main()
