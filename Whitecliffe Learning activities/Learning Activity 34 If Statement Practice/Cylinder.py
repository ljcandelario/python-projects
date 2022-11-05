# Learning Activity- Cylinder.py
# by Louie Candelario
# 14/10/2022

import math

pi = math.pi

question = input("Here is a cylinder. Would you like to get the area or the volume? \n\n"
                 "[A] Area\n"
                 "[B] Volume")

answer = question.lower()

if answer == "a":
    print("Let's find the area of the cylinder")
    radius = int(input("Enter the radius of the cylinder"))
    length = int(input("Enter the length of the cylinder"))
    area = 2 * pi * radius * (radius + length)
    print(round(area, 2))

if answer == "b":
    print("Let's find the volume of the cylinder")
    radius = int(input("Enter the radius of the cylinder"))
    length = int(input("Enter the length of the cylinder"))
    volume = pi * (radius ** 2) * length
    print(round(volume, 2))

# Assertion 1
" Volume. radius = 3, length = 5, Volume = 141.37 "

# Assertion 2
" Area. radius = 5, length = 9, Area = 439.82 "
