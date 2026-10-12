import logging

logging.basicConfig(
    filename="input.log",
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

try:
    number = int(input("Enter an integer: "))
    logging.info("Valid integer received")
    print("Your number:", number)

except ValueError:
    logging.error("User entered an invalid integer")
    print("Please enter a valid integer.")