# Parking_meter.py
#
# Louie Candelario
# 13.10.2022

print("Kia Ora, this is a parking meter")
park_time = int(input("How many do you want to park?"))
print("park_time time is ", park_time, " hours.")

rate = 4
cost = 0
if park_time > 3:
    cost = rate * 3
    # drop the rate by $2
    rate -= 2
    # get the remainder of the parking time
    park_time -= 3
    # add to the current cost
    cost += rate * park_time
    print("The cost of the parking is $", cost)
else:
    cost = rate * park_time
    print("The cost of the parking is $", cost)

# test case assertion 1
'''
park_time = 7
total cost of parking = $20
'''

# test case assertion 2
'''
park_time = 2
total cost of parking = $8
'''