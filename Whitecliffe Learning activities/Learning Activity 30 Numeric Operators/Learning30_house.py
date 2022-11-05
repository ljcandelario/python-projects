# house.py, learning activity 30
# author: Louie Candelario
# 10.10.2022

u_side = int(input('Enter the height of u.'))
m_side = int(input('Enter the length of m.'))
n_length = int(input('Enter the height of n.'))

triangle_area = (n_length ** 2) / 2
square_area = m_side * u_side

area = triangle_area + square_area


print("The area of the shape is " + str(area))

# testing
"""
print("my assertions are:"
        "\n u_side = 3, m_side = 2, n_length = 4,  output = 14"
        "\n u_side = 5, m_side = 3, n_length = 6, output = 18")
"""