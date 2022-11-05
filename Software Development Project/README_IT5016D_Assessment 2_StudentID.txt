Software project READ ME text file
By Louie Candelario, 20220956	

The IT Help desk ticketing system is a program that accepts input from the user and creates a new ticket. The ticket statistics are then displayed after each new ticket is created. There are options to display all tickets, a specific ticket, respond to a ticket and reopen a closed ticket. This project was created as a requirement for my Software development course at Whitecliffe school of Technology.

To initialize the project, first store all related files in a single folder.
All the files needed are:
Main.py
Ticket.py
Problem.py
User.py
Ticket_counter.py
Ticket_display.py

The Main.py file is where the whole program can be initialized. 

The Ticket class in Ticket.py is where most of the classes are connected to each other. The Ticket class is started with the opening_menu() method where all the choices are laid out and the choice of the user is taken to decide which functions to use. 

To start the use of the ticketing system, please choose option 1. Create a new Ticket.
Then give the required input such as staff ID, name, email and the description of the problem.
Example:
Staff ID: 20220956
Name: Louie 
email: louie_candelario@email.com
issue: Wifi not working

Once this has been done, the ticket information will then be stored, given a ticket number and printed to display the entered ticket information. The ticket statistics will also be displayed to acknowledge that the ticket was counted as an open ticket. The opening menu will then be presented again.

Next, create another ticket with different details but with the issue as "password change". Once the ticket is created and stored, the opening menu will pop up again. Please choose option 5, "Respond to ticket". Enter the ticket number of the ticket with the password change issue. This will prompt the user to hit enter to generate a new password for this specific ticket and issue. Once the user hits enter, the ticket will print with the response as new passowrd generated along with the new password. It will display the ticket statistics again and return to the opening menu.

Now that 2 tickets have been created, you can now choose option 2, "See existing tickets" to display the available tickets.

The program will continue to run until option 7, "Exit the program" has been chosen.