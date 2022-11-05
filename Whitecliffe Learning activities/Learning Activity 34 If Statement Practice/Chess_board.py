# Learning Activity- Chess_board.py
# by Louie Candelario
# 14/10/2022
# """ Positions on a chess board are identified by a letter and a number. The letter identifies the column,
# while the number identifies the row. Write a program that reads position coordinates from the user.
# Use an if statement to determine if the column begins with a black square or a white square.
# Then use modular arithmetic to report the colour of the square in that row. For example,
# if the user enters a, and then enters 1, your program should report that the square is black. If the user enters d,
# and then enters 5, your program should report that the square is white. Your program may assume that a valid position
# will always be entered. It does not need to perform any error checking. """


row_number = 0

enter_column_letter = input("Enter the column letter.")
enter_row_choice = int(input("Enter the row number"))


if enter_column_letter == ("a" or "c" or "e" or "g"):
    row_number = 1

player_choice = enter_row_choice + row_number

if player_choice % 2 == 0:
    print("Black square")
else:
    print("White square")

