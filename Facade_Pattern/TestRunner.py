#Facade
from TC1 import TC1
from TC2 import TC2
from TC3 import TC3

class TestRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()

    def runAll(self):
        self.tc1.run()
        self.tc2.run()
        self.tc3.run()
