import datetime

class Classroom:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number_of_students(self):
        while True:
            try:
                student_number = int(input("Enter the number of students in the class: "))
                if student_number < 0:
                    print("Number of students in the class can't be negative. Please enter again.")
                else:
                    return student_number
            except ValueError:
                print("Number of students in the class must be an integer. Please enter again.")

    def input_student_information(self):
        student_info = {}
        student_info["ID"] = str(input("Enter student ID: ")).upper()
        student_info["Name"] = str(input("Enter student name: ")).title()
        
        while True:
            dob = input("Enter student date of birth (DD/MM/YYYY): ")
            try:
                student_info["DoB"] = datetime.datetime.strptime(dob, "%d/%m/%Y")
                break
            except ValueError:
                print("Incorrect date format. Please use the format DD/MM/YYYY.")
        
        print(" ")
        return student_info


    def input_number_of_courses(self):
        while True:
            try:
                course_number = int(input("Enter the number of courses: "))
                if course_number < 0:
                    print("Number of courses can't be negative. Please enter again.")
                else:
                    return course_number
            except ValueError:
                print("Number of courses must be an integer. Please enter again.")

    def input_course_information(self):
        course_info = {}
        course_info["ID"] = str(input("Enter course ID: ")).upper()
        course_info["Name"] = str(input("Enter course name: ")).title()
        print(" ")
        return course_info

    def select_course_and_input_marks(self, classroom):
        course_id = str(input("Enter the course ID for which you want to input marks: ")).upper()

        selected_course = next((course for course in classroom.courses if course["ID"] == course_id), None)

        if selected_course:
            for student in classroom.students:
                while True:
                    try:
                        mark = float(input(f"Enter marks for {student['Name']} in {selected_course["Name"]}: "))
                        if mark < 0:
                            print("Grade can't be negative. Please enter again.")
                        elif mark > 20:
                            print("Grade must be smaller than 20. Please enter again.")
                        else:
                            student.setdefault("marks", {})[course_id] = mark
                            break
                    except ValueError:
                        print("Grade must be a number. Please enter again.")
        else:
            print("Course not found.")

    def list_courses(self, classroom):
        print("\nCourses:")
        for course in classroom.courses:
            print(f"ID: {course["ID"]}")
            print(f"Name: {course["Name"]}\n")

    def list_students(self, classroom):
        print("\nStudents:")
        for student in classroom.students:
            print(f"ID: {student["ID"]}")
            print(f"Name: {student["Name"]}\n")

    def show_student_marks_for_course(self, classroom):
        student_id = str(input("Enter student ID to show marks: ")).upper()

        selected_student = next((student for student in classroom.students if student["ID"] == student_id), None)

        if selected_student:
            course_id = str(input("Enter course ID to show marks: ")).upper()
            marks = selected_student.get("marks", {}).get(course_id, None)

            if marks is not None:
                print(f"Marks for {selected_student["Name"]} in {course_id}: {marks}")
            else:
                print(f"Marks not found for {selected_student["Name"]} in {course_id}.")
        else:
            print("Student not found.")

# Main
classroom = Classroom()

num_students = classroom.input_number_of_students()
for _ in range(num_students):
    classroom.students.append(classroom.input_student_information())

num_courses = classroom.input_number_of_courses()
for _ in range(num_courses):
    classroom.courses.append(classroom.input_course_information())

while True:
    print("\nOptions:")
    print("1. List Courses")
    print("2. List Students")
    print("3. Input Marks for a Course")
    print("4. Show Student Marks for a Course")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        classroom.list_courses(classroom)
    elif choice == "2":
        classroom.list_students(classroom)
    elif choice == "3":
        classroom.select_course_and_input_marks(classroom)
    elif choice == "4":
        classroom.show_student_marks_for_course(classroom)
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
