"""
Class methods:
class methods are bound to class and class variables

they can be used in case where we need to control the access of the class variables
or class variable state

also alternatively used for creating class instance as well
"""


# as @property meant to be only for instance properties
# I am going to build decorator for classproperty
class classproperty(property):
    def __get__(self, obj, cls):
        return self.fget(cls)


# class method is used to control the class variable
class ClassVariableExampple1(object):
    # protected class variables
    __class_var1 = "Example Class"
    __instance_counts = 0

    def __init__(self):
        # every time new object created the counter keeps the track of it
        ClassVariableExampple1.__instance_counts += 1

    @classproperty
    def instance_counts(cls):  # class method but decorated with classproperty
        return cls.__instance_counts

    # example for class method
    @classmethod
    def get_instance_count(cls):
        return cls.__instance_counts

    @classmethod
    def get_class_var1(cls):
        return cls.__class_var1

    # this is another use of class method.
    # can be used for creating instance of a class alternatively
    @classmethod
    def with_extra_arg(cls, arg):
        _cls = cls()
        _cls.arg = arg
        return _cls


def main():
    obj1 = ClassVariableExampple1()
    obj2 = ClassVariableExampple1()

    print(ClassVariableExampple1.instance_counts)
    print(obj1.instance_counts, obj2.instance_counts)

    print(ClassVariableExampple1.get_instance_count())
    print(obj1.get_instance_count(), obj2.get_instance_count())

    print(ClassVariableExampple1.get_class_var1())
    print(obj1.get_class_var1(), obj2.get_class_var1())


if __name__ == "__main__":
    main()
