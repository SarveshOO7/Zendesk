# import requests module
import requests
from requests.auth import HTTPBasicAuth

print("Welcome to the Ticket Viewer!\n")

# Put your credintials here
subdomain = input()
email = input()
password = input()

baseURL = 'https://' + subdomain + '.zendesk.com/api/v2/tickets'


def printTicketDetails(ticket):
    print('Ticket with subject \'' +
          ticket['subject'] + '\' opened by', ticket['requester_id'], 'on', ticket['created_at'])
        
def handleError(response):
    if response.status_code == 404:
        print("Sorry! Could not find requested ticket(s)")
        return True
    if response.status_code == 401:
        print("Sorry! You have given incorrect credentials!")
        return True
    if 'error' in response.json():
        print(response.json().get('error'))
        return True
    return False



def getAllTickets():
    url = baseURL + ".json?page[size]=25"
    while 1:
        # Making a get request for all tickets
        response = requests.get(url, auth=HTTPBasicAuth(
            email, password))

        # handle error response
        if handleError(response):
            return
        tickets = response.json()

        # print request object
        for ticket in tickets['tickets']:
            printTicketDetails(ticket)

        if tickets.get('links').get('next'):
            url = tickets.get('links').get('next')
            print("Press enter to see next page!")
            temp = input()
        else:
            break


def getATicket():
    # get ticket ID from user
    print("Enter ticket ID:")
    ticketID = input()

    # Making a get request for the ticket
    response = requests.get(baseURL + "/" + ticketID + ".json", auth=HTTPBasicAuth(
        email, password))

    # handle error response
    if handleError(response):
        return

    ticket = response.json()
    printTicketDetails(ticket['ticket'])


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
        getATicket()
