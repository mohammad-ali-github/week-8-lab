# 1. Storing first name in a variable
first_name = "Mohammad"

# 2. Storing last name in a variable
last_name = "Ali"

# 3. Printing hello firstname and lastname
print(f"Hello, {first_name.upper()} {last_name.lower()}")

# 4. Printing two line breaks
print()
print()

# 5. Creating a new variable with first name and last name with space
first_and_last_name = first_name + " " + last_name

# 6. Slicing the lastname from the joined name and printing it
print(first_and_last_name[9:])

# 7. Replacing lastname with specified string and printing it
print(first_and_last_name.replace(last_name, f"{last_name}, Walsh College Student"))

# 8. Printing quote
print("\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi\"")

# 9. Storing two decimal values
value1 = 20.0
value2 = 10.0

# 10. Storing reuslt of arithmetic operations
addition = value1 + value2
subtraction = value1 - value2
multiplication = value1 * value2
division = value1 / value2

# 11. Printing result of each arithmetic operation using different string formatting techniques
print(str(value1) + " plus " + str(value2) + " equals " + str(addition))
print("{0} minus {1} equals {2}".format(value1, value2, subtraction))
print("%.1f multiplied to %.1f equals %.1f" %	(value1, value2, multiplication))
print(f"{value1} divided by {value2} equals {division}")

# 12. Calculating square root and displaying
sq_root = round(multiplication ** 0.5, 2)
print("The square root of {0} equals {1}".format(multiplication, sq_root))

# 13. Storing current month and day
current_month = "November"
current_day = 12

# 14. Printing current month and day
print(f"\n\t\tToday is day {current_day} of the month of {current_month}.")