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