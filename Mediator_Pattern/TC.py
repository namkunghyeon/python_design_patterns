import time

class TC:
    def __init__(self):
        self._tm = None
        self._bProblem = 0

    def setup(self):
        print "Setting up the Test"
        time.sleep(1)
        self._tm.prepareReporting()

    def execute(self):
        if not self._bProblem:
            print "Executeing the test"
            time.sleep(1)
        else:
            print "Problem in setup. Test not executed"

    def tearDown(self):
        if not self._bProblem:
            print "Tearing down"
            time.sleep(1)
            self._tm.publishReport()
        else:
            print "Test not executed, NO tear don required"


    def setTM(self, TM):
        self._tm = TM

    def setProblem(self, value):
        self._bProblem = value
