# Learning Activity - Identify_triangle.py
# by Louie Candelario
# 14/10/2022
# """Name that Triangle
# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. All 3 sides of
# an equilateral triangle have the same length. An isosceles triangle has two sides that are the same length and a
# third side that is a different length. If all the sides have different lengths, then the triangle is scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user. Display a message indicating the type
# of the triangle. """

side_1 = input("Enter the length of the 1st side of the triangle.")
side_2 = input("Enter the length of the 2nd side of the triangle.")
side_3 = input("Enter the length of the 3rd side of the triangle.")

#
if side_1 == side_2 == side_3:
    print("The triangle is an equilateral triangle.")
elif side_1 == side_2 \
        or side_1 == side_3 \
        or side_2 == side_3:
    print("The triangle is an isosceles triangle")
else:
    print("The triangle is a scalene triangle")