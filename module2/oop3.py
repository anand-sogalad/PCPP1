"""
What is MRO
Method resolution order is the strategy to look for method in classes that is inherited from a class or more
it looks always from left right
"""


# lets try to solve diamond problem (multiple inheritance)
class A(object):
    def info(self):
        print("class A - info")


class B(A):
    def info(self):
        print("class B - info")


class C(A):
    def info(self):
        print("class C - info")


class D(B, C): ...


class D(A, C): ...  # this fails due to MRO cannot be solved


def main():
    d = D()
    d.info()  # expecting to print class B - info


if __name__ == "__main__":
    main()


"""
Method resolution order

It always starts from the class
then looks for the first base (left most)
then next, so on
it should be that child class should come first then parent class
"""
