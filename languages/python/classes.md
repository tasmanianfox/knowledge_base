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