# Automated Grading Engine v1.1
# Author: Lakshay Thore

def grade_student(marks):
    if marks >= 75:
        return 'DISTINCTION'
    return 'PASS' if marks >= 40 else 'FAIL'
