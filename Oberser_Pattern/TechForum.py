
from Publisher import Publisher

class TechForum(Publisher):

    def __init__(self):
        self._listOfUsers = []
        self.postname = None

    def register(self, userObj):
        if userObj not in self._listOfUsers:
            self._listOfUsers.append(userObj)

    def unregister(self, userObj):
        self._listOfUsers.remove(userObj)


    def notifyAll(self):
        for objects in self._listOfUsers:
            objects.notify(self.postname)

    def writeNewPost(self, postname):
        #User writes a post
        self.postname = postname
        #When submits the post is published and notification is sent to all
        self.notifyAll()
