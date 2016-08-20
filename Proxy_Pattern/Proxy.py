import time
from Manager import Manager
from SalesManager import SalesManager

class Proxy(Manager):
    def __init__(self):
        self.busy = 'Yes'
        self.sales = None

    def work(self):
        print "Proxy Checking For Sales Manger Availablility"

        if self.busy == 'Yes':
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()

        else:
            time.sleep(2)
            print "Sales Manager is Busy"
