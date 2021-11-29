from fetcher import getATicket


def testGetATicket():
    for i in range(1, 101):
        assert getATicket(str(i))
