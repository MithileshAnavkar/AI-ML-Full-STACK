import argparse

parser = argparse.ArgumentParser(
    description="Student Marks Checker"
)

parser.add_argument("name")
parser.add_argument("marks", type=float)

args = parser.parse_args()

if not 0 <= args.marks <= 100:
    parser.error("Marks must be between 0 and 100")

status = "PASS" if args.marks >= 40 else "FAIL"

print(f"Student: {args.name}")
print(f"Marks: {args.marks}")
print(f"Result: {status}")