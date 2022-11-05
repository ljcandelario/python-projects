from Ticket_display import TicketDisplay
from User import User
from Problem import Problem
from Ticket_counter import TicketStats


class Ticket:

    def opening_menu(self):
        self.counter_tickets = TicketStats()  # method for displaying and counting the ticket statistics
        self.ticket_container = {} # starts with an empty dictionary where the new tickets will be added
        print("Hello, welcome to IT tech support.")
        choice = 0
        while choice != "7":
            choice = str(input("What would you like to do? \n\n"
                               "[1] Create a new ticket \n" 
                               "[2] See existing tickets \n"
                               "[3] Display specific ticket \n"
                               "[4] Reopen specific ticket \n"
                               "[5] Respond to ticket \n"
                               "[6] Display ticket statistics \n"
                               "[7] Exit the program "))
            self.choices(choice)

    def choices(self, choice):
        if choice == "1":
            # gets information from input, then goes through User and Problem, to create the new ticket.
            new_ticket = self.get_ticket_information()

            # Ticket dictionary, creating a new key, and adding the new_ticket as value
            self.ticket_container[self.counter_tickets.ticket_id()] = new_ticket

            # new_ticket is formatted to show properly on the terminal, taking in the ticket_number as a parameter
            # from ticket_id as the Ticket number.
            new_ticket.display_ticket(self.counter_tickets.ticket_id())

            # the counter is then added to by increment_ticket_counter
            self.counter_tickets.increment_ticket_counter()
            self.counter_tickets.add_open_ticket()

            print(self.counter_tickets.display_stats())

        elif choice == "2":  # prints all tickets
            print(self.all_tickets())

        elif choice == "3":  # displays a specific ticket in the correct format
            ticket_number = input("Enter ticket number")
            reopened_ticket = self.ticket_container[ticket_number]
            reopened_ticket.display_ticket(ticket_number)

        elif choice == "4":  # reopen a closed ticket
            ticket_number = input("Enter ticket number")
            reopened_ticket = self.ticket_container[ticket_number]
            reopened_ticket.reopen_ticket(ticket_number)
            self.counter_tickets.add_open_ticket()  # adds to open tickets since te ticket was reopened
            self.counter_tickets.subtract_closed_ticket()  # subtracts from the closed tickets
            print(self.counter_tickets.display_stats())

        elif choice == "5":  # responds to a ticket
            ticket_number = input("please enter the ticket number")
            responded_ticket = self.ticket_container[ticket_number]  # calls the ticket number
            responded_ticket.ticket_response(ticket_number)  # updates and formats the edited ticket, closes the ticket
            self.counter_tickets.add_closed_tickets()  # adds to closed ticket counter
            self.counter_tickets.subtract_open_ticket() # subtracts from open tickets
            print(self.counter_tickets.display_stats())

        elif choice == "6":  # prints ticket statistics
            print(self.counter_tickets.display_stats())

        elif choice == "7":  # exits the program
            print("You have exited the program")
        else:
            print("Invalid choice. Please try again")

    def get_ticket_information(self):  # takes input from the user
        staff_id = input("Enter your staff ID")
        name = input("Enter your name")
        email = input("Enter your email")
        problem = input("Enter the issue you encountered")

        user = User(staff_id, name, email)  # creates a user object
        issue = Problem(problem)  # Problem object
        response = "Not yet provided"

        return TicketDisplay(user, issue, response)  # creates the ticket object

    def all_tickets(self):
        # prints all tickets in a formatted version
        print("\nHere are all the tickets")
        for key, value in self.ticket_container.items():
            print("\nTicket number: " + str(key))
            print("Name: ", value.user.name)
            print("Staff ID:", value.user.staff_id)
            print("Email: ", value.user.email)
            print("Customer Problem: ", value.problem.problem)
            print("Response: ", value.response)
            print("Ticket Status: ", value.status)





if __name__ == "__main__":
    ticket_system = Ticket()
    ticket_system.opening_menu()