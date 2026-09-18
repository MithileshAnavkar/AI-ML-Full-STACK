def get_number():
    try:
        number = int(input("Enter a number: "))
        return number

    except ValueError:
        print("Invalid input")
        return None

def analyze_number(number):

    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    print("Sign:", sign)
    print("Type:", parity)

number = get_number()

if number is not None:
    analyze_number(number)