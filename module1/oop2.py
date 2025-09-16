"""
Implementing python operation on a specific objects
"""

# for example, int supports addition, subtraction...etc operations
n = 10
print(f"Addition operation - n + 10 == n.__add__(10) : {n + 10} == {n.__add__(10)}")


# So, same way we are going to implement operators on our custom Objects
class Person(object):
    def __init__(self, weight, height, age):
        self.__weight = weight
        self.__height = height
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    def __add__(self, other):
        """
        So, when two instances of same object are added it will add the weight
        attribute of the same objects
        """
        return self.weight + other.weight

    def __sub__(self, other):
        """
        same as addition, implementing subtraction
        """
        return self.weight - other.weight


def main():
    # create 2 object of a same class - Person
    person1 = Person(50, 5.5, 20)
    person2 = Person(56, 5.6, 22)

    # adding 2 objects should return the sum of (additon of) weight of the two objects
    total_weight = person1 + person2  # this should output as 106
    print(total_weight)

    total_weight = person1 - person2
    print(total_weight)


if __name__ == "__main__":
    main()
