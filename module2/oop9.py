"""
Decorator prctice:

Decorator is one of the design patterns.
that is used describe the related objects

It actually hides the complex implementations and makes code looks simpler and cleaner
"""


# type1.
# universal decorator example with logger for each method
def logger(func):  # takes function as input
    def wrapper(*args, **kwargs):  # a clouser that remembers the args of out scope
        print(f"{func.__name__} method is being clalled")
        result = func(*args, **kwargs)
        print(result)
        print(f"{func.__name__} method execution completed")
        return result

    return wrapper  # clouser returned


# type2.
# universal decorator that always takes log_level as arg
def logger_with_level(log_level):  # this is called decorator factory
    def decorator(func):  # the real decorator
        def warapper(*args, **kwargs):  # the closure
            print(f"[{log_level}] {func.__name__} method is being clalled")
            result = func(*args, **kwargs)
            print(result)
            print(f"[{log_level}] {func.__name__} method execution completed")
            return result

        return warapper

    return decorator


# type3.
# universal decorator that can take arg or use default one
def logger_with_default_arg(_func=None, *, log_level="DEBUG"):
    def decorator(func):  # the real decorator
        def warapper(*args, **kwargs):  # the closure
            print(f"[{log_level}] {func.__name__} method is being clalled")
            result = func(*args, **kwargs)
            print(result)
            print(f"[{log_level}] {func.__name__} method execution completed")
            return result

        return warapper

    return decorator(_func) if _func else decorator


# this is universal decorator similer to decorator function type1
class Logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"I am calling {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(result)
        print(f"I am closing {self.func.__name__}")
        return result


# this is the universal decorator of type2
class Logger1(object):
    def __init__(self, value):
        self.value = value

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"I am calling {func.__name__}")
            result = func(*args, **kwargs)
            print(result)
            print(f"I am closing {func.__name__}")
            return result

        return wrapper


# this is universal decorator of type 3
class Logger2(object):
    def __init__(self, func=None, *, level="DEBUG"):
        self.func = func
        self.level = level

    def __call__(self, *args, **kwargs):
        # If func is not None, this is decorating a function
        if self.func:
            print(
                f"I am decorator class and this is printing from {self.__class__.__name__} with {self.level}"
            )
            result = self.func(*args, **kwargs)
            print(result)
            print(
                f"I am decorator class and this is printing from {self.__class__.__name__} with {self.level}"
            )
            return result
        else:
            # If no function yet, return a decorator factory
            def real_decorator(func):
                return Logger2(func, level=self.level)

            return real_decorator


@logger
def test1():
    return "I am test1"


@logger_with_level("INFO")
def test2():
    return "I am test2"


@logger_with_default_arg
def test3():
    return "I am test3"


@logger_with_default_arg(log_level="WARN")
def test4():
    return "I am test4"


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
