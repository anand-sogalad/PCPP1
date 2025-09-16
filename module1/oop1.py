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
