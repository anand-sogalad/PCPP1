"""
Decorators
Decorator is one of the design patterns that describes the related objects.
"""

# decorator examples


# this simple decorator is bit problomatic
# this prints {func.__name__} getting decorated by simple_dcorator
# always, even if func1 was not called
# so, we should decorate always using wrappers
def simple_dcorator(func):
    print(f"{func.__name__} getting decorated by simple_dcorator")
    return func


# this decorator doesn't print anything unless func is called
# this decorator also takes all takes care of function arguments
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is being called")
        func(*args, **kwargs)
        print(f"{func.__name__} is completed")

    return wrapper


# implement a decorator that also takes arguments
def decorator_factory(name="decorator_factor"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"I am using decorator factory argument : {name}")
            print(f"{func.__name__} is getting called")
            result = func(*args, **kwargs)
            print(f"{func.__name__} execution finished")
            return result

        return wrapper

    return decorator


@simple_dcorator
def func1():
    print("Hello I am func1")


def func2():
    print("Hello I am func2")


@logger
def func3():
    print("I am function 3")


def main():
    func2()  # not decorated
    func3()


if __name__ == "__main__":
    main()
