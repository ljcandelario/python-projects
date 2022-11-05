# Learning Activity - Phone_bill.py
# by Louie Candelario
# 14/10/2022
# """Cell Phone Bill A particular cell phone plan includes 50 minutes of air time and 50 text messages for $15.00 a
# month. Each additional minute of air time costs $0.25, while additional text messages cost $0.15 each. All cell phone
# bills include an additional flat charge of $0.44 to support 111 call centres, and the entire bill (including the 111
# charge) is subject to 5 percent sales tax. Write a program that reads the number of minutes and text messages used in
# a month from the user. Display the base charge, additional minutes charge (if any), additional text message charge
# (if any), the 111 fee, tax and total bill amount. Only display the additional minute and text message charges if the
# user incurred costs in these categories. Ensure that all the charges are displayed using 2 decimal places."""

minutes = int(input("Enter the number of minutes consumed"))
text_messages = int(input("Enter the number of text messages used"))

basic_charge = 1500
additional_minute = 25
additional_text = 15
flat_charge = 44
sales_tax = 0.05
extra_texts_charge = 0
extra_minutes_charge = 0

print("Your basic charge is $", str(basic_charge / 100))
if minutes > 50:
    extra_minutes_charge = int((minutes - 50) * additional_minute)
    print("The extra charges on your extra minutes are ", str(extra_minutes_charge/100))

if text_messages > 50:
    extra_texts_charge = int((text_messages - 50) * additional_text)
    print("The extra charges on your text messages are ", str(extra_texts_charge/100))

print("Flat charge for 111 calls is $", flat_charge/100)

sub_total = basic_charge + flat_charge + extra_texts_charge + extra_minutes_charge
print("The subtotal of your bill is: $", sub_total/100)

tax_charge = sub_total * sales_tax
print("Tax charges: $", round(tax_charge/100, 2))

total_bill = round((sub_total + tax_charge)/100, 2)
print("The total bill is: $", total_bill)

# Assertion 1.
"""
minutes = 60, texts = 60, extra_texts_charge = 1.5, extra_minutes_charge = 2.5, tax_charge = $0.97, 
total_ bill = $20.41
"""

# Assertion 2.
"""
minutes = 70, texts = 55, extra_texts_charge = 0.75, extra_minutes_charge = 5, tax_charge = $1.06, 
total_ bill = $22.25extra_minutes_charge
"""

# Assertion 3.
"""
minutes = 40, texts = 45, extra_texts_charge = 0, extra_minutes_charge = 0, tax_charge = $0.77, 
total_ bill = $16.21
"""