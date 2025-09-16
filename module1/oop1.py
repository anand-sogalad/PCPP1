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


if __name__ == "__main__":
    main()
