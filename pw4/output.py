def show_students(students):
    print("\nSTUDENT GPA LIST")
    print("-" * 55)
    print(f"{'ID':<12}{'Name':<25}{'Average GPA':>15}")
    print("-" * 55)

    for student in students:
        print(
            f"{student.student_id:<12}"
            f"{student.name:<25}"
            f"{student.average_gpa():>15.2f}"
        )