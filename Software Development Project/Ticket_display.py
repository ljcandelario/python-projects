# IT5016D_Assessment 2_20220956.py
# by Louie Candelario
# 25/10/2022
from Ticket_counter import TicketStats

class TicketDisplay:

    def __init__(self, user, problem, response):
        self.user = user
        self.problem = problem
        self.status = "Open"
        self.response = response

    def get_user(self):
        return self.user

    def display_ticket(self, ticket_number):  # prints the ticket in a formatted version
        print("\nHere is ticket number:", ticket_number)
        print("Staff ID:", self.user.staff_id)
        print("Employee name: ", self.user.name)
        print("Email: ", self.user.email)
        print("Employee issue: ", self.problem.problem)
        print("Response: ", self.response)
        print("Status: ", self.status, "\n")

    def reopen_ticket(self, ticket_number):  # prints the ticket in a formatted version
        print("\nHere is ticket number:", ticket_number)
        print("Staff ID:", self.user.staff_id)
        print("Employee name: ", self.user.name)
        print("Email: ", self.user.email)
        print("Employee issue: ", self.problem.problem)
        print("Response: ", self.response)
        self.status = "Reopened"
        print("Status: ", self.status, "\n")

    def ticket_response(self, ticket_number):  # changes the response from the default

        new_response = input("Enter your response")
        self.response = new_response

        if "password change" == str(self.problem.problem):
            # auto-generates new password, gives the new password to "response"
            confirm = input("Hit enter to auto-generate new password and close ticket")
            print(confirm)
            self.response = self.password_generator()
            print("\nHere is ticket number:", ticket_number)
            print("Staff ID:", self.user.staff_id)
            print("Employee name: ", self.user.name)
            print("Email: ", self.user.email)
            print("Employee issue: ", self.problem.problem)
            print("Response: ", self.response)
            self.status = "Closed"
            print("Status: ", self.status, "\n")
        else:
            print("\nHere is ticket number:", ticket_number)
            print("Staff ID:", self.user.staff_id)
            print("Employee name: ", self.user.name)
            print("Email: ", self.user.email)
            print("Employee issue: ", self.problem.problem)
            print("Response: ", self.response)
            self.status = "Closed"
            print("Status: ", self.status, "\n")

    def password_generator(self):  # 1st 2 characters of staff ID and 1st 3 characters of name
        first_part = self.user.staff_id[:2]
        second_part = self.user.name[0:3]
        new_password = str(first_part + second_part)
        self.response = new_password
        final_change = str("new password generated: " + new_password)
        return final_change

    '''def change_ticket_status(self, ticket_number):
        change_status = input("What would you like to do? "
                              " [1] Reopen Ticket \n"
                              " [2] Close Ticket \n")
        if change_status == "1":
            self.status = "reopened"
        elif change_status == "2":
            self.status = "closed"'''









