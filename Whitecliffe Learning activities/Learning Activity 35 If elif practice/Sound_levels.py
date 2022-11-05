# Learning Activity- Sound_levels.py
# by Louie Candelario
# 14/10/2022
# """The following table lists the sound level in decibels for several common noises.
#
# Noise Decibel level (dB)
# Jackhammer 130
# Petrol lawnmower 106
# Alarm clock 70
# Quiet room 40
#
# Write a program that reads a sound level in decibels from the user. If the user enters a decibel level that matches
# one of the noises in the table, then your program should display a message containing only that noise. If the user
# enters a number of decibels between the noises listed, then your program should display a message indicating which
# noises the level is between. Ensure that your program also generates reasonable output for a value smaller than the
# quietest noise in the table, and for a value larger than the loudest noise in the table."""

sound_level = int(input("Enter the decibel levels of the sound"))

# ensures all sound levels above 130 decibels can be accepted as input.
if sound_level > 130:
    print("The sound is louder than a jackhammer")
elif sound_level == 130:
    print("The sound is as loud as a jackhammer")
# creates a range between 2 levels only using operators instead of using "and"
elif 106 < sound_level < 130:
    print("The sound's decibel level is between a lawnmower and a jackhammer.")
elif sound_level == 106:
    print("The sound is as loud as a lawnmower")
elif 70 < sound_level < 106:
    print("The sound's decibel level is between an alarm clock and a lawnmower.")
elif sound_level == 70:
    print("The sound is as loud as an alarm clock")
elif 40 < sound_level < 70:
    print("The sound's decibel level is between a quiet room and an alarm clock.")
elif sound_level == 40:
    print("The sound is as quiet as a quiet room")
else:
    print("It is more quiet than a quiet room.")
    # ensures that all other sounds less than 40 decibels can be considered as input

# Assertion 1
" sound_level = 135, result = print('The sound is louder than a jackhammer.')"

# Assertion 2
" sound_level = 75, result = print('The sound's decibel level is between a alarm clock and a lawnmower.')"

# Assertion 3
" sound_level = 35, result = print('It is more quiet than a quiet room.')"
