"""
Abastract class and methods: If a class has abstract method. then it can be called as abstract class
An abstract class provides specific features to be implemented by the subclass
abstract class cannot be instantiated
abstract class also have common features implemented
Interface:
It act as a cotract
it only declares the fatures to be implemented by the sub class
"""

# example
from abc import ABC, abstractmethod


class BluePrint(ABC):

    @abstractmethod
    def print(self, paper, color): ...


class Printer(BluePrint):

    # python doesn't enforce method signature
    # as long as method is implemented, that's is sufficient
    def print(self, paper: str, color: str, is_special: bool):
        print(f"Prionting {paper} in {color} ink special ink? {is_special}")


def main():
    my_printer = Printer()
    my_printer.print("Praja Vaani", "red", True)


if __name__ == "__main__":
    main()
