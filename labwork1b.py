students = []
courses = []
marks = {}

# ==================== INPUT FUNCTIONS ====================

def input_students():
    """Input number of students in a class and their information"""
    num_students = int(input("Enter the number of students in the class: "))
    for i in range(num_students):
        print(f"\n--- Enter information for student {i+1} ---")
        student_id = input("  ID: ")
        name = input(" Name: ")
        dob = input("  DoB (Date of Birth): ")
        
        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }
        students.append(student)
    print("\n✅ Student information recorded successfully!")

def input_courses():
    """Input number of courses and their information[cite: 1]"""
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        print(f"\n--- Enter information for course {i+1} ---")
        course_id = input("  Course ID: ")
        name = input("  Course Name: ")
        
        course = {
            "id": course_id,
            "name": name
        }
        courses.append(course)
    print("\n✅ Course information recorded successfully!")

def input_marks():
    """Select a course, input marks for student in this course[cite: 1]"""
    if not courses:
        print("No courses available. Please input courses first!")
        return
    if not students:
        print("No students available. Please input students first!")
        return

    list_courses()
    course_id = input("\nEnter Course ID to input marks: ")
    
    # Check if the entered course_id exists
    course_exists = any(course['id'] == course_id for course in courses)
    
    if course_exists:
        if course_id not in marks:
            marks[course_id] = {} 
            
        print("\n--- Input Marks ---")
        for student in students:
            mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
            marks[course_id][student['id']] = mark
        print("\n✅ Marks inputted successfully!")
    else:
        print("❌ Course ID not found!")

# ==================== LISTING FUNCTIONS ====================

def list_students():
    """List students[cite: 1]"""
    if not students:
        print("Student list is empty.")
        return
    print("\n--- LIST OF STUDENTS ---")
    for s in students:
        print(f"ID: {s['id']:<10} | Name: {s['name']:<20} | DoB: {s['dob']}")

def list_courses():
    """List courses[cite: 1]"""
    if not courses:
        print("Course list is empty.")
        return
    print("\n--- LIST OF COURSES ---")
    for c in courses:
        print(f"ID: {c['id']:<10} | Name: {c['name']}")

def show_marks():
    """Show student marks for a given course[cite: 1]"""
    if not marks:
        print("No marks data available.")
        return

    list_courses()
    course_id = input("\nEnter Course ID to show marks: ")
    
    if course_id in marks:
        print(f"\n--- MARKS FOR COURSE {course_id} ---")
        for student_id, mark in marks[course_id].items():
            # Find student name by ID
            student_name = next((s['name'] for s in students if s['id'] == student_id), "Unknown")
            print(f"ID: {student_id:<10} | Name: {student_name:<20} | Mark: {mark}")
    else:
        print("❌ No marks recorded for this course or course does not exist.")

# ==================== MAIN MENU ====================

def main():
    while True:
        print("\n" + "="*40)
        print("      STUDENT MARK MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a given course")
        print("0. Exit")
        print("="*40)
        
        choice = input("Enter your choice (0-6): ")
        
        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            list_students()
        elif choice == '6':
            show_marks()
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
