# Learning31_student.py, learning activity 31
# author: Louie Candelario
# 11.10.2022

nz_resident = True
international_student = False

print("Check for student's eligibility.")
student_age = int(input("Please enter the student's age."))
distance_from_school = int(input("Please enter distance in kilometers."))

# Assertion 1, student_age = 17 and distance_from_school = 3 should equate to true.
print("The student's eligibility is..",
      distance_from_school < 4
      and 18 > student_age > 10
      and nz_resident
      or 18 > student_age > 10
      and international_student, "\n")

# Assertion 2, student_age = 19 and distance_from_school = 3 should equate to False.
