from fetcher import getATicket


def testGetATicket():
    """Test getATicket function in fetcher.py assuming all the tickets in tickets.json have been uploaded."""
    for i in range(1, 101):
        assert getATicket(str(i))
