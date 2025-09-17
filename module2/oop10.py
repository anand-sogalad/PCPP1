"""
Static methods
they do not bind neither with class nor with instance
"""


class Something(object):

    # static method dont have any access to class or instance state and data/property
    @staticmethod
    def some_method():
        print("some method")


def main():
    # calling static methods
    Something.some_method()


if __name__ == "__main__":
    main()
