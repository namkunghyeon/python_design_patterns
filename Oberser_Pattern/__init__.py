
from User1 import User1
from User2 import User2
from SisterSites import SisterSites
from TechForum import TechForum

if __name__ == "__main__":
    techForum = TechForum()
    user1 = User1()
    user2 = User2()
    sites = SisterSites()

    techForum.register(user1)
    techForum.register(user2)
    techForum.register(sites)

    techForum.writeNewPost("Observer Pattern in Python")

    techForum.unregister(user2)

    techForum.writeNewPost("MVC Pattern in Python")
