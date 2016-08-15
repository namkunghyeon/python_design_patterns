import time
class Reporter:
    def __init__(self):
        self._tm = None

    def prepare(self):
        print "Reporter Class is preparing to report thr results"
        time.sleep(1)

    def report(self):
        print "Reporting the results of Test"
        time.sleep(1)

    def setTM(self, TM):
        self._tm = TM
