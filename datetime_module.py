from datetime import*
class Date_check:

    #staticmethod which does not take the instance or the class as it's first argument
    @staticmethod
    def is_workday(day):
        '''
        In python, dates have this weekday() method, where monday = 0 and sunday = 6
        and all the other days in between
        '''

        # if the day we are checking is equal to 'Saturday or Sunday' that means is not a work day
        # returns False
        if day.weekday() == 5 or day.weekday() == 6:
            return 'False: not work day'
        return 'True, is work day'

my_date = date(2020, 2, 10)

print(Date_check.is_workday(my_date))
