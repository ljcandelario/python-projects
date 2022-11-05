# Learning Activity - While_loop_practice.py
# by Louie Candelario
# 21/10/2022

height = 8
width = 3
length = 10
area_of_rect = 2 * (width * length) + 2 * (length * height) + 2 * (height * width)
rectangle_volume = (height * length * width)
x_side_correct = False
y_side_correct = False
user_choice = False
x_side = int
y_side = int
answer = str

# program choice of the user, either to find volume, to find area or exit the program
while user_choice == False:
    choice = input("Hello, what would you like to do with this shape? \n"
                   "[A] Find the area of the shape \n"
                   "[B] Find the volume of the shape \n"
                   "[C] Exit the program \n")
    answer = choice.lower()
    if answer == "a":
        user_choice = True
        print("Let's find the area of the shape")
    elif answer == "b":
        user_choice = True
        print("Let's find the volume of the shape")
    elif answer == "c":
        print("You have exited the program")
        quit()
        #exits the program without going to the next while loops that check the validity of x_side and y_side
    else:
        print("Incorrect. Try again. \n\n")

# validating x_side value entered
while x_side_correct == False:
    x_side = int(input("Enter the value of x. It must be between 2 and 8"))
    # checks to see if x_side is a correct value
    if 2 <= x_side and x_side <= 8:
        x_side_correct = True
    else:
        print("Invalid value. Try again.")

# validating y_side value entered
while y_side_correct == False:
    y_side = int(input("Enter the value of y. It must be between 1 and 7"))
    # checks to see if y_side is a correct value
    if 1 <= y_side <= 7:
        y_side_correct = True
    else:
        print("Invalid value. Try again.")

# if user chose find area:
if answer == "a":
    print("Let's find the area of the shape")
    small_shape_area = 2 * (width * x_side) + 2 * (x_side * y_side) + 2 * (y_side * width)
    shape_area = area_of_rect - small_shape_area
    print("The area of the shape is: ", shape_area, "cm")
elif answer == "b":
    print("Let's find the volume of the shape")
    small_rect_volume = int((y_side * x_side * width))
    shape_volume = rectangle_volume - small_rect_volume
    print("The volume of the shape is:", shape_volume, "cm^3")

# test assertions
# assertion 1
# "Choice = a, find the area. x_side = 3, y_side = 4. result = 'The area of the shape is 202cm'"

# assertion 2
# "Choice = b, find the volume. x_side = 5, y_side = 4. result = 'The volume of the shape is 180cm^3'"