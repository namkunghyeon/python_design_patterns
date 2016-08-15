class Switch:
    """The INVOKER class"""

    def __init__(self, flipUpCmd, flipDownCmd):
        self._flipUpCommand = flipUpCmd
        self._flipDownCommand = flipDownCmd

    def flipUp(self):
        self._flipUpCommand.execute()

    def flipDown(self):
        self._flipDownCommand.execute()
