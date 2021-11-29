# import requests module
from fetcher import getATicket, getAllTickets

def CLI():
    """Creates a main menu in CLI to run the program"""
    print("Welcome to the Ticket Viewer!\n")


    while(1):
        print(" * Press 1 to view all tickets\n")
        print(" * Press 2 to view a ticket\n")
        print(" * Press q to quit\n")

        inp = input()
        if inp == 'q':
            print("\nThank you!\n")
            break

        if inp == '1':
            getAllTickets()
        elif inp == '2':
            # get ticket ID from user
            print("Enter ticket ID:")
            ticketID = input()
            getATicket(ticketID)
        else:
            print("Invalid Command!")

if __name__ == "__main__":
    CLI()

