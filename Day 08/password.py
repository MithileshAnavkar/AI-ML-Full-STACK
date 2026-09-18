password = input("Enter a password")

has_upper = False
has_lower = False
has_digit = False

for char in password:
     if char.isupper():
        has_upper = True
     if char.islower():
         has_lower= True
     if char.isdigit():
         has_digit= True

if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Your pass is strong")
else:
    print("Your pass is weak")

if not has_upper:
    print("no upper alphabets")

if not has_lower:
    print("no lower alphabets")

if not has_digit:
    print("no digits")

if len(password) < 8 :
    print("Your pass is less than 8 chars")

                  