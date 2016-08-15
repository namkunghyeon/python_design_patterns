from Command import Command

class FlipUpCommand(Command):
    """The Command class for turning off the light"""

    def __init__(self, light):
        super(Command, self).__init__()
        self._light = light

    def execute(self):
        self._light.turnOn()
