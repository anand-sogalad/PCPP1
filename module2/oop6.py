"""
Scenario
Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
Apply your decorator to those functions to ensure that the time of the function executions can be monitored.
"""

from datetime import datetime


def timestampt(func):
    def wrapper(*args, **kwargs):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        result = func(*args, **kwargs)
        print(result)
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return result

    return wrapper


@timestampt
def addition(n1, n2):
    return n1 + n2


def main():
    addition(10, 15)


if __name__ == "__main__":
    main()
