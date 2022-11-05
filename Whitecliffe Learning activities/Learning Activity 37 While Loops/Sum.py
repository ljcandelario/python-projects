# Learning Activity - Sum.py
# by Louie Candelario
# 14/10/2022

given_number = int(input("Enter a positive number"))
num = 0
sum_of_all = 0

while num <= given_number:
    sum_of_all = sum_of_all + num
    num += 1

print("n =", num, "sum = ", sum_of_all)

