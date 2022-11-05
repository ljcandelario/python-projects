# Learning Activity - Password.py
# by Louie Candelario
# 15/10/2022

password_tries = 3

while True:
    answer = input("Please enter password")
    if answer == "1985":
        print("Welcome to your account.")
        break
    else:
        print("Password incorrect. Try again")
        password_tries -= 1

    if password_tries == 0:
        print("No more tries")
        break

exit_message = input("Hit enter to exit")

# Assertion 1
"input = '2000', print('Password incorrect. Try again') "
"input = '1346', print('Password incorrect. Try again') "
"input = '1985', print('Welcome to your account.') "

# Assertion 2
"input = '1985', print('Welcome to your account.')"