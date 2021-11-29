
import requests
from requests.models import HTTPBasicAuth
import creds

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
    url = creds.baseURL + ".json?page[size]=25"
    while 1:
        # Making a get request for all tickets
        response = requests.get(url, auth=HTTPBasicAuth(
            creds.email, creds.password))

        # handle error response
        if handleError(response):
            return False
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
    return True


def getATicket(ticketID):
    # Making a get request for the ticket
    response = requests.get(creds.baseURL + "/" + ticketID + ".json", auth=HTTPBasicAuth(
        creds.email, creds.password))

    # handle error response
    if handleError(response):
        return False

    ticket = response.json()
    printTicketDetails(ticket['ticket'])
    return True
