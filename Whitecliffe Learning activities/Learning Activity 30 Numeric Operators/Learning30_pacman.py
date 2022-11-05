# pacman.py, learning activity 30
# author: Louie Candelario
# 10.10.2022

import math

radius = int(input('Enter the radius.'))

area = (radius ** 2) * math.pi

print("The area of the shape is " + str(area))

# testing
"""
print("my assertions are:"
        "\n radius = 2,  output = 12.566370614359172"
        "\n radius = 6, output = 113.09733552923255")
"""