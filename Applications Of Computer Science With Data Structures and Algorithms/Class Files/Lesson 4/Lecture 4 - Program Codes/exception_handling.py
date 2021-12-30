# Without Try-Except
# top = int(input("Please enter the numerator:"))

# With Try-Except
try:
    top = int(input("Please enter the numerator:"))
except ValueError: # This try -except catches only ValueErrors
    print("You didn’t enter an integer.")
    exit(0)

try:
    bottom = int(input("Please enter the denominator:"))
except Exception: # This try -except catches any exception. Optional
    print("You didn’t enter an integer.")
    exit(0)

# try:
if top % bottom == 0:
    print("The numerator is evenly divided by the denominator.")
else:
    print("The fraction is not a whole number.")
# except ZeroDivisionError:
#     print("The denominator cannot be 0.")

print("Happy")