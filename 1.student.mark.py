classroom = {
    "students": [],
    "courses": []
}


# Input function

def input_number_of_students():
    while True:
        try:
            student_number = int(input("Enter the number of students in the class: "))
            if student_number < 0:
                print("Number of students in the class can't be negative. Please enter again.")
            else:
                return student_number
        except ValueError:
            print("Number of students in thew class must be an integer. Please enter again.")


def input_student_information():
    student_info = {}
    student_info["ID"] = str(input("Enter student ID: ")).upper()
    student_info["Name"] = str(input("Enter student name: ")).title()
    student_info["DoB"] = str(input("Enter student DoB: "))
    print(" ")
    return student_info


def input_number_of_courses():
    while True:
        try:
            course_number = int(input("Enter the number of courses: "))
            if course_number < 0:
                print("Number of courses can't be negative. Please enter again.")
            else:
                return course_number
        except ValueError:
            print("Number of courses must be an integer. Please enter again.")


def input_course_information():
    course_info = {}
    course_info["ID"] = str(input("Enter course ID: ")).upper()
    course_info["Name"] = str(input("Enter course name: ")).title()
    print(" ")
    return course_info


def select_course_and_input_marks(classroom):
    course_id = str(input("Enter the course ID for which you want to input marks: ")).upper()

    selected_course = next((course for course in classroom["courses"] if course["ID"] == course_id), None)

    if selected_course:
        for student in classroom["students"]:
            while True:
                try:
                    mark = float(input(f"Enter marks for {student['Name']} in {selected_course['Name']}: "))
                    if mark < 0:
                        print("Grade can't be negative. Please enter again.")
                    else:
                        student.setdefault("marks", {})[course_id] = mark
                        break
                except ValueError:
                    print("Grade must be a number. Please enter again.")
    else:
        print("Course not found.")



# Listing functions

def list_courses():
    print("\nCourses:")
    for course in classroom["courses"]:
        print(f"ID: {course['ID']}")
        print(f"Name: {course['Name']}\n")


def list_students():
    print("\nStudents:")
    for student in classroom["students"]:
        print(f"ID: {student['ID']}")
        print(f"Name: {student['Name']}\n")


def show_student_marks_for_course():
    student_id = str(input("Enter student ID to show marks: ")).upper()

    selected_student = next((student for student in classroom["students"] if student["ID"] == student_id), None)

    if selected_student:
        course_id = str(input("Enter course ID to show marks: ")).upper()
        marks = selected_student.get("marks", {}).get(course_id, None)

        if marks is not None:
            print(f"Marks for {selected_student['Name']} in {course_id}: {marks}")
        else:
            print(f"Marks not found for {selected_student['Name']} in {course_id}.")
    else:
        print("Student not found.")


# Main

number_of_students = input_number_of_students()
for i in range(number_of_students):
    student_data = input_student_information()
    classroom["students"].append(student_data)

number_of_courses = input_number_of_courses()
for i in range(number_of_courses):
    course_data = input_course_information()
    classroom["courses"].append(course_data)

while True:
    print("\nOptions:")
    print("1. List Courses")
    print("2. List Students")
    print("3. Input Marks for a Course")
    print("4. Show Student Marks for a Course")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        list_courses()
    elif choice == "2":
        list_students()
    elif choice == "3":
        select_course_and_input_marks(classroom)
    elif choice == "4":
        show_student_marks_for_course()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
