from Male import Male
from Female import Female

class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)

        if gender == 'F':
            return Female(name)
