
from Light import Light
from FlipDownCommand import FlipDownCommand
from FlipUpCommand import FlipUpCommand
from Switch import Switch

class LightSwitch:
    """The Client class"""

    def __init__(self):
        self._lamp = Light()
        self._switchUp = FlipUpCommand(self._lamp)
        self._switchDown = FlipDownCommand(self._lamp)
        self._switch = Switch(self._switchUp, self._switchDown)

    def switch(self, cmd):
        cmd = cmd.strip().upper()
        try:
            if cmd == "ON":
                self._switch.flipUp()
            elif cmd == "OFF":
                self._switch.flipDown()
            else:
                print "Argument \"ON\" OR \"OFF\" is required."

        except Exception, msg:
            print "Exception occured: %s" % msg
