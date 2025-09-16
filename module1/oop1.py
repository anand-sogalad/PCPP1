"""
Learning:
class: A class is an idea or blueprint of an idea. it binds data and code
instance: An istance an instance of an class, its also called as object
object: A python's classes and methods are called as object in python
attribute: It's a class's traits. It can refere to variables and methods inside a class
methods: Methods are callable attributes
"""


class Duck(object):
    def __init__(self, height, weight, sex):
        self.__height = height
        self.__weight = weight
        self.__sex = sex

    def walk(self):
        return "duck can walk"

    def quack(self):
        return "quack quack"

    @property
    def height(self):
        return self.__height

    @property
    def weight(self):
        return self.__weight

    @property
    def sex(self):
        return self.__sex


"""
Scenario
create a class representing a mobile phone;
your class should implement the following methods:
__init__ expects a number to be passed as an argument; this method stores the number in an instance variable self.number
turn_on() should return the message 'mobile phone {number} is turned on'. Curly brackets are used to mark the place to insert the object's number variable;
turn_off() should return the message 'mobile phone is turned off';
call(number) should return the message 'calling {number}'. Curly brackets are used to mark the place to insert the object's number variable;
create two objects representing two different mobile phones; assign any random phone numbers to them;
implement a sequence of method calls on the objects to turn them on, call any number. Print the methods' outcomes;
turn off both mobiles.
Example output

mobile phone 01632-960004 is turned on
mobile phone 01632-960012 is turned on
calling 555-34343
mobile phone is turned off
mobile phone is turned off

"""


class Mobile(object):
    class_var = "I am class variable"

    def __init__(self, number):
        self.number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    def turn_on(self):
        return f"mobile phone {self.number} is turned on"

    def turn_off(self):
        return "mobile phone is turned off"

    def call(self, number):
        return f"calling {number}"


def main():
    # creating instances of the abovve class
    duckling = Duck(10, 3.4, "male")
    drake = Duck(25, 3.7, "male")
    hen = Duck(20, 3.4, "female")

    # class attributes
    # variables (currently they are encapsulated)
    print(
        f"Height: {duckling.height}",
        f"Weight: {duckling.weight}",
        f"Sex: {duckling.sex}",
    )
    print(f"Height: {drake.height}", f"Weight: {drake.weight}", f"Sex: {drake.sex}")
    print(f"Height: {hen.height}", f"Weight: {hen.weight}", f"Sex: {hen.sex}")

    # methods (callable attributes)
    print(duckling.walk(), duckling.quack())
    print(drake.walk(), drake.quack())
    print(hen.walk(), hen.quack())

    # types
    print(Duck.__class__)
    print(duckling.__class__)
    print(duckling.sex.__class__)
    print(duckling.quack.__class__)

    # mobile phone examples
    x_phone = Mobile("+91 99858 32548")
    y_phone = Mobile("+91 99858 32549")

    print(x_phone.turn_on())
    print(y_phone.turn_on())

    print(x_phone.call(y_phone.number))

    print(x_phone.turn_off())
    print(y_phone.turn_off())

    # if you would like to see the content of each attributes and their value use
    # __dict__ attribute (note that its not callable)
    print(x_phone.__dict__)
    print(y_phone.__dict__)
    print(Mobile.__dict__)  # use class name for all the class attributes


if __name__ == "__main__":
    main()
