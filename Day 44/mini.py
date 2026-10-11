import logging

logging.basicConfig(
    filename="student_results.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_result(name, marks):
    if marks < 0 or marks > 100:
        logging.error("Invalid marks received")
        return

    if marks >= 40:
        logging.info("%s passed with %s marks", name, marks)
    else:
        logging.warning("%s failed with %s marks", name, marks)

check_result("Aarav", 85)
check_result("Riya", 32)
check_result("Kabir", 120)

print("Results processed. Check student_results.log")