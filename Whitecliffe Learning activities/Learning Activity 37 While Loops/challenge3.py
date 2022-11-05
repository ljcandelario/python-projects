# Learning Activity - Sum.py
# by Louie Candelario
# 14/10/2022

p_value = int(input("Enter value of P"))
q_value = int(input("Enter value of Q"))
counter = 10

starting_number = (10 % p_value) + 10

while counter <= q_value:
    print(starting_number, end=", ")
    starting_number = starting_number + p_value
    counter += p_value
