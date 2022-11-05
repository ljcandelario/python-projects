# Learning Activity- Chinese_zodiac.py
# by Louie Candelario
# 14/10/2022

year_born = int(input("Enter the year birth year to find out your chinese zodiac."))

# using modulo to determine each year's zodiac sign, without have to write every single year possible.
if year_born % 12 == 0:
    print("Your zodiac sign is the Monkey")
elif year_born % 12 == 1:
    print("Your zodiac sign is the Rooster")
elif year_born % 12 == 2:
    print("Your zodiac sign is the Dog")
elif year_born % 12 == 3:
    print("Your zodiac sign is the Pig")
elif year_born % 12 == 4:
    print("Your zodiac sign is the Rat")
elif year_born % 12 == 5:
    print("Your zodiac sign is the Ox")
elif year_born % 12 == 6:
    print("Your zodiac sign is the Tiger")
elif year_born % 12 == 7:
    print("Your zodiac sign is the Hare")
elif year_born % 12 == 8:
    print("Your zodiac sign is the Dragon")
elif year_born % 12 == 9:
    print("Your zodiac sign is the Snake")
elif year_born % 12 == 10:
    print("Your zodiac sign is the Horse")
elif year_born % 12 == 11:
    print("Your zodiac sign is the Sheep")

# Assertion 1
"year_born = 1993, zodiac = Rooster"

# Assertion 2
"year_born = 2978, zodiac = Dog"

# Assertion 3
"year_born = 1016, zodiac = Dragon"

