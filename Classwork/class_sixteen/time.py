import datetime

class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

    def __init__(t, hour=0, minute=0, second=0):
        """
        Initializes a time object.
        hour: int
        minute: int
        second: int or float
        """
        t.hour = hour
        t.minute = minute
        t.second = second

    def __str__(t):
        """Returns a string representation of the time."""
        return '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)


    def print_time(t):
        """
        Prints a string representation of the time.
        """
        print(str(t))

    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

    def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    def is_after(t, other):
        """
        Returns True if t1 is after t2; fals eotherwise
        """
        return t.time_to_int() > other.time_to_int

#PROTOTYPING

    def add_time(t1, t2):
        """
        Adds two Time objects or a Time onject and a number
        """
        seconds = Time.time_to_int(t1) + Time.time_to_int(t2)
        return Time.int_to_time(seconds)

    def subtract_time(t1, t2):
        """
        Subtracts two time objects
        """
        seconds = Time.time_to_int(t1) - Time.time_to_int(t2)
        return Time.int_to_time(seconds)

    def mul_time(t1, factor):
        """
        takes a Time object and a number and returns a new Time 
        object that contains the product of the original Time and 
        the number
        """
        seconds = Time.time_to_int(t1)*factor 
        return Time.int_to_time(abs(seconds))

def race_speed(finish, distance):
    """
    Returns mile time as Time Object when given a finish time
    and number of miles to run
    """
    return finish.mul_time(1/distance)

def print_day():
    """
    Prints the current day of the week
    """
    my_date = datetime.datetime.now()
    print('The current day of the week is {0:%A}'.format(my_date, 'weekday'))

def birthday_printer(date):
    """
    Takes a birthdate as datetime and prints the user's age 
    as well as the time until their next birthday
    """
    now = datetime.datetime.today()
    age_delta = now - date
    age = age_delta.days // 365
    next_bday = datetime.datetime(now.year, date.month, date.day)
    time_til = next_bday - now
    if time_til.total_seconds() < 0:
        next_bday = datetime.datetime(now.year + 1, date.month, date.day)
        time_til = next_bday - now
    minutes, second = divmod(time_til.seconds, 60)
    hour, minute = divmod(minutes, 60)
    print('You are currently %d years old' %(age))
    print('There are %d days, %d hours, %d minutes, and %d seconds until your birthday' %(time_til.days, hour, minute, second))

def doubleday(d1, d2):
    """
    Takes two birthdates and prints the first person is 
    2 times older than the second person
    """
    dif = abs(d1 - d2)
    if d1 > d2:
        dd = d1 + dif
    elif d2 > d1:
        dd = d2 + dif
    else:
        print('These are the same date!')
        pass
    print('Your Double Day is %s' %(dd))

def main():
    start = Time()
    start.hour = 9
    start.minute = 45
    start.second =  0

    duration = Time()
    duration.hour = 1
    duration.minute = 35
    duration.second = 0

    print(Time.add_time(start, duration))
    print(Time.subtract_time(start, duration))

    print('After multiplied by 5: ', end=' ')
    print(Time.mul_time(start, 5))

    Time.print_time(race_speed(start, 8))

    print_day()
    my_birthday = datetime.datetime(1995, 1, 5)
    my_birthdate = datetime.date(1995, 1, 5)
    your_birthdate = datetime.date(2005, 1, 5)
    birthday_printer(my_birthday)
    doubleday(your_birthdate, my_birthdate)
    
if __name__ == '__main__':
    main()