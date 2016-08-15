import abc

class Publisher:
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        #Make it uniniheritable
        pass

    def register(self):
        #OVERRIDE
        pass

    def unregister(self):
        #OVERRIDE
        pass

    def notifyAll(self):
        #OVERRIDE
        pass
