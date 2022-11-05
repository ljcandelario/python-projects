class TicketStats:

    def __init__(self): # Tallies all the ticket statistics
        self.counter_tickets = 2000
        self.open_tickets = 0
        self.closed_tickets = 0
        self.total_tickets = 0

    def display_stats(self):
        print("Ticket Statistics: ")
        print("Total tickets: ", self.add_total_tickets())
        print("Open tickets: ", self.open_tickets)
        print("Closed tickets: ", self.closed_tickets)

    def ticket_id(self):  # creates the ticket ID that starts at 2000
        return str(self.counter_tickets)

    def increment_ticket_counter(self):
        self.counter_tickets += 1

    def add_open_ticket(self):
        self.open_tickets += 1

    def add_total_tickets(self):
        self.total_tickets = self.open_tickets + self.closed_tickets
        return self.total_tickets

    def add_closed_tickets(self):
        self.closed_tickets += 1

    def subtract_open_ticket(self):
        self.open_tickets -= 1

    def subtract_closed_ticket(self):
        self.closed_tickets -= 1