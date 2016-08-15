import time

class DB:
    def __init__(self):
        self._tm = None

    def insert(self):
        print "Inserting the execution begin status in the Database"
        time.sleep(1)
        #Floowing code is to simulate a communication From DB to TC
        import random
        if random.randrange(1, 4) == 3:
            return -1

    def update(self):
        print "Udateing the test results in Database"

    def setTM(self, TM):
        self._tm = TM
