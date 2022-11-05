# bouncer.py, learning activity 31
# author: Louie Candelario
# 12.10.2022

nz_resident = True
international_student = False

print("Check guest's name and age.")
guest_age = int(input("Please enter the student's age."))
guest_name = input("Please enter your name")

if guest_age < 21:
    print("Sorry. I can not allow you inside.")
elif guest_name == "Suzanne May":
    print("Sorry. I can not allow you inside.")
elif guest_name == "Wiremu Rangi":
    print("Sorry. I can not allow you inside.")
else:
    print("Welcome to the Bar!")

# Assertion 1. guest_age < 21, guest_name != "Suzanne May" or guest_name != "Wiremu Rangi". Outcome = False. I can not allow you inside
# print("Check guest's name and age.")
"""guest_age = int(input("Please enter the student's age."))
# guest_age = 20
guest_name = input("Please enter your name")  
# guest_name = Louie 

if guest_age < 21:
    print("Sorry. I can not allow you inside.")
elif guest_name == "Suzanne May":
    print("Sorry. I can not allow you inside.")
elif guest_name == "Wiremu Rangi":
    print("Sorry. I can not allow you inside.")
else:
    print("Welcome to the Bar!")
"""

# Assertion 2, guest_age > 21, guest_name != "Suzanne May" or guest_name != "Wiremu Rangi". Outcome = True. Welcome to the bar
# print("Check guest's name and age.")
"""guest_age = int(input("Please enter the student's age."))
# guest_age = 21
guest_name = input("Please enter your name")  
# guest_name = Louie 

if guest_age < 21:
    print("Sorry. I can not allow you inside.")
elif guest_name == "Suzanne May":
    print("Sorry. I can not allow you inside.")
elif guest_name == "Wiremu Rangi":
    print("Sorry. I can not allow you inside.")
else:
    print("Welcome to the Bar!")
"""

# Assertion 3, guest_age > 21, guest_name == "Suzanne May" or guest_name != "Wiremu Rangi". Outcome = False. I can not allow you inside.
# print("Check guest's name and age.")
"""guest_age = int(input("Please enter the student's age."))
# guest_age = 23
guest_name = input("Please enter your name")  
# guest_name = Suzanne May 

if guest_age < 21:
    print("Sorry. I can not allow you inside.")
elif guest_name == "Suzanne May":
    print("Sorry. I can not allow you inside.")
elif guest_name == "Wiremu Rangi":
    print("Sorry. I can not allow you inside.")
else:
    print("Welcome to the Bar!")
"""

# Assertion 3, guest_age > 21, guest_name != "Suzanne May" or guest_name == "Wiremu Rangi". Outcome = False. I can not allow you inside.
# print("Check guest's name and age.")
"""guest_age = int(input("Please enter the student's age."))
# guest_age = 25
guest_name = input("Please enter your name")  
# guest_name = Wiremu Rangi

if guest_age < 21:
    print("Sorry. I can not allow you inside.")
elif guest_name == "Suzanne May":
    print("Sorry. I can not allow you inside.")
elif guest_name == "Wiremu Rangi":
    print("Sorry. I can not allow you inside.")
else:
    print("Welcome to the Bar!")
"""