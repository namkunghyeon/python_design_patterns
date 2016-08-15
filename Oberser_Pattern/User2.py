from Subscriber import Subscriber

class User2(Subscriber):
    def notify(self, postname):
        print 'User2 notified of a new post %s' % postname
