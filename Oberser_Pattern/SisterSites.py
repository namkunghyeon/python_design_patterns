from Subscriber import Subscriber

class SisterSites(Subscriber):
    def __init__(self):
        self._sisterWebsites = ["Site1", "Site2", "Site3"]

    def notify(self, postname):
        for site in self._sisterWebsites:
            #Send updates by any means
            print "Sent nofication to site: %s" % site
