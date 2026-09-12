def student_result(marks):
    total = 0

    for mark in marks:
        total += mark

    percentage = total / len(marks)

    if percentage >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return total, percentage, result


total, percentage, result = student_result([80, 70, 90, 60, 75])

print("Total:", total)
print("Percentage:", percentage)
print("Result:", result)