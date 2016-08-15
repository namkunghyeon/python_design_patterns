
from Reporter import Reporter
from DB import DB
from TestManager import TestManager
from TC import TC

if __name__ == '__main__':
    reporter = Reporter()
    db = DB()
    tm = TestManager()
    tm.setReporter(reporter)
    tm.setDB(db)

    reporter.setTM(tm)
    db.setTM(tm)


    #For simplification we are looping on the same test
    #Practially, it colud be about various unique test classes and ther objects

    while(1):
        tc = TC()
        tc.setTM(tm)
        tm.setTC(tc)
        tc.setup()
        tc.execute()
        tc.tearDown()
