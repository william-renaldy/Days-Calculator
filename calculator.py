from datetime import datetime
from dateutil.relativedelta import relativedelta


class Calculate(relativedelta):
    def __init__(self,date1,date2):

        date1 = tuple(map(int,date1))
        date2 = tuple(map(int,date2))

        date1 = datetime(*date1)
        date2 = datetime(*date2)

        if date2 > date1:
            date2,date1 = date1,date2

        super().__init__(date1,date2)