from fetcher import getATicket


def test():
    for i in range(1, 101):
        assert getATicket(str(i))
