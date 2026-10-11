def calculate_percentage(marks, total):
    if total <= 0:
        raise ValueError("Total marks must be positive")

    if not 0 <= marks <= total:
        raise ValueError("Marks must be between 0 and total")

    return marks / total * 100


def get_grade(percentage):
    if not 0 <= percentage <= 100:
        raise ValueError("Invalid percentage")

    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 40:
        return "C"
    return "F"