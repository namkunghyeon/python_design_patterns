import abc

class Command(object):
    __metaclass__ = abc.ABCMeta
    """The Command Abstract class"""
    def __init__(self):
        pass
        #Make Changes

    @abc.abstractmethod
    def execute(self):
        pass
        #OVERRIDE
