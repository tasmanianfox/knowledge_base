# Classes

## Declaration of class

```python
class MyClass:
    def __init__(self, arg1): # Define properties in constructor!
        self.propery_a = "Value1"
        self.property_b = None
        self.property_c = arg1

    def my_function(self):
        return self.property_a

    def my_function2(self, arg):
        self.property_a = arg


my_instance = MyClass("test") # an instance of MyClass is created
```

## Static properties

```python
class AwesomeOtherClass:
    pass

class MyClass:
    static_property = AwesomeOtherClass()

    def __init__(self):
        self.propery_a = "Value1"

    def my_function(self):
        return "hello"

myobject = MyClass()
myobject.property_a # This belongs to an instance of MyClass object
MyClass.tatic_property # This is shared across all insances
```

## Invocation of super-class method

Use the __super()__ to invoke a method of super-class from sub-class

__NB!__ This code is incompatible with Python 2 and wil result with an error below:

```
super() takes at least 1 argument (0 given)
```

A working example in file: [super_method.py](examples/classes/super_method.py)

```python
class SuperClass:
    def some_method(self, param):
        return param + " SuperClass::some_method"


class SubClass(SuperClass):
    def some_method(self, param):
        return super().some_method(param) + " SubClass::some_method"

sub = SubClass()
result = sub.some_method("Hello")

print(result)
# Output:
# Hello SuperClass::some_method SubClass::some_method
```