# house.py, learning activity 30
# author: Louie Candelario
# 10.10.2022

import math

e_side = int(input('Enter the height of e.'))
f_side = int(input('Enter the length of f.'))
g_side = int(input('Enter the height of g.'))

triangle_area = f_side / 2 * g_side
rectangle_area = e_side * g_side
half_circle_area = (g_side / 2) ** 2 * math.pi / 2

area = triangle_area + rectangle_area + half_circle_area


print("The area of the shape is " + str(area))

# testing
"""
print("my assertions are:"
        "\n e_side = 2, f_side = 5, g_side = 4,  output = 24.283185307179586"
        "\n u_side = 3, m_side = 7, n_length = 5, output = 42.317477042468106")
"""