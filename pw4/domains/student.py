import math
import numpy as np
from domains.course import Course


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def add_course(self, course_name, mark, credits):
        mark = math.floor(mark * 10) / 10

        course = Course(course_name, mark, credits)
        self.courses.append(course)

    def average_gpa(self):
        if not self.courses:
            return 0.0

        marks = np.array([c.mark for c in self.courses])
        credits = np.array([c.credits for c in self.courses])

        total_credits = np.sum(credits)

        if total_credits == 0:
            return 0.0

        return float(np.sum(marks * credits) / total_credits)