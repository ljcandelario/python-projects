# Learning Activity- Performance_review.py
# by Louie Candelario
# 14/10/2022
# """Performance Reviews
# At a particular company, employees are rated at the end of each year. The rating scale begins at 0.0, with higher
# values indicating better performance and resulting in larger raises. The value awarded to an employee is either
# 0.0, 0.4, or 0.6 or more. Values between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
# with each rating is shown in the following table. The bonus awarded to an employee is $2400.00 multiplied by their
# rating.
#
# Rating Meaning
# 0.0 Unacceptable performance
# 0.4 Acceptable performance
# 0.6 or more Meritorious performance
#
# Write a program that reads a rating from the user and indicates whether the performance was unacceptable, acceptable
# or meritorious. The amount of the employee’s raise should also be reported. Your program should display an appropriate
# error message if an invalid number is entered."""

rating = float(input("Please rate your employee based on the three options below. \n\n"
                     "0.0 Unacceptable\n"
                     "0.4 acceptable performance\n"
                     "0.6 or more meritorious performance"))

if rating == 0.0:
    print("You rated the employee with unacceptable performance. They will not get a raise.")
elif rating == 0.4:
    employee_raise = rating * 2400
    print("You rated the employee with acceptable performance. Their raise is: $", employee_raise)
elif rating >= 0.6:
    employee_raise = rating * 2400
    print("You rated the employee with meritorious performance. Their raise is: $", employee_raise)
else:
    print("Please enter the one of the 3 rating numbers given. ")
    # using the else statement to make sure that the user does not enter value between 0.0-0.4 and 0.4-0.6

# Assertion 1
"rating = 0.0, unacceptable performance, raise = 0"
# Assertion 2
"rating = 0.4, Acceptable performance, raise = $960"
# Assertion 3
"rating = 0.8, Meritorious performance, raise = $1920"
# Assertion 4
"rating = 0.5, Please enter the one of the 3 rating numbers given. raise = 0"