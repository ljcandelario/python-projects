# Learning31_shopping.py, learning activity 31
# author: Louie Candelario
# 11.10.2022

print("This program checks if the customer can process a transaction")

registered_customer = True
purchased_gift_card = False
items_in_cart = int(input("How many items in the online cart?"))

print("The customer's check out status is... ",
      items_in_cart > 1
      and registered_customer
      or not registered_customer
      or purchased_gift_card, "\n")

# Assertion 1. registered_customer = True, items_in_cart = 4. Should print True
# Assertion 2. registered_customer = True, items_in_cart = 0, purchased_gift_card = True. Should print True
# Assertion 3. registered_customer = False, items_in_cart = 0, purchased_gift_card = True. Should print True
# Assertion 4. registered_customer = True, items_in_cart = 0, purchased_gift_card = False. Should print False
