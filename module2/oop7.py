"""
class as a decorator
"""


class Decorator(object):
    def __init__(self, func):
        self.func = func

    # __cal__ is used for calling class as a method
    def __call__(self, *args, **kwargs):
        print(f"I am decorator class and this is printing from {Decorator.__name__}")
        result = self.func(*args, **kwargs)
        print(result)
        print(f"I am decorator class and this is printing from {Decorator.__name__}")
        return result


@Decorator
def myfunc(a, b):
    return a + b


result = myfunc(1, 2)
print(result)
