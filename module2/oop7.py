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


class Decorator1:
    def __init__(self, func=None, *, decorator_arg="SomeValue"):
        self.func = func
        self.arg = decorator_arg

    def __call__(self, *args, **kwargs):
        # If func is not None, this is decorating a function
        if self.func:
            print(
                f"I am decorator class and this is printing from {self.__class__.__name__} with {self.arg}"
            )
            result = self.func(*args, **kwargs)
            print(result)
            print(
                f"I am decorator class and this is printing from {self.__class__.__name__} with {self.arg}"
            )
            return result
        else:
            # If no function yet, return a decorator factory
            def real_decorator(func):
                return Decorator1(func, decorator_arg=self.arg)

            return real_decorator


@Decorator1
def myfunc(a, b):
    return a + b


result = myfunc(1, 2)
print(result)
