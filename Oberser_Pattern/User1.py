from Subscriber import Subscriber

class User1(Subscriber):
    def notify(self, postname):
        print 'User1 notified of a new post %s' % postname
