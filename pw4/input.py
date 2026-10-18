def read_students():
    from domains.student import Student

    students = []
    number = int(input("Number of students: "))

    for i in range(number):
        print(f"\nStudent {i + 1}")

        student_id = input("Student ID: ")
        name = input("Student name: ")

        student = Student(student_id, name)
        course_count = int(input("Number of courses: "))

        for j in range(course_count):
            course_name = input("Course name: ")
            mark = float(input("Mark: "))
            credits = float(input("Credits: "))

            student.add_course(course_name, mark, credits)

        students.append(student)

    return students