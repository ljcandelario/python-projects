# rectangle.py, learning activity 30
# author: Louie Candelario
# 10.10.2022

g_side = int(input('Enter the height of g.'))
s_side = int(input('Enter the length of s.'))
q_side = int(input('Enter the height of q.'))
w_side = int(input('Enter the length of w.'))

area = (g_side * s_side) - (q_side * w_side)

print("The area of the shape is " + str(area))

# testing
"""
print("my assertions are:"
        "\n g = 3, s = 5, q = 2, w = 1, output = 13"
        "\n g = 5, s = 9, q = 4, w = 2, output = 37")
"""