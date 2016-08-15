import abc

class Subscriber:
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        #Make it uniniheritable
        pass

    def notify(self):
        #OVERRIDE
        pass
