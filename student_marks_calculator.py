"""
Student Marks Calculator
A beginner-friendly Python practice project for learning Git.
"""

def calculate_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks) 
    average = total / len(marks)
    return total, percentage,average


def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def main():
    student_name = "Rahul"
    marks = [85, 92, 78, 88, 95]

    total, percentage, average = calculate_percentage(marks)
    grade = get_grade(percentage)

    print("Student:", student_name)
    print("Marks:", marks)
    print("Total:", total)
    print("Percentage:", round(percentage, 2), "%")
    print("average:", round(average, 2))

    print("Grade:", grade)


if __name__ == "__main__":
    main()
