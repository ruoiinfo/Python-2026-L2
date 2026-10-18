from input import read_students
from output import show_students


def main():
    students = read_students()

    students.sort(
        key=lambda student: student.average_gpa(),
        reverse=True
    )

    show_students(students)


if __name__ == "__main__":
    main()