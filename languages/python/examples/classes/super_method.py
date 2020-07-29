class SuperClass:
    def some_method(self, param):
        return param + " SuperClass::some_method"


class SubClass(SuperClass):
    def some_method(self, param):
        return super().some_method(param) + " SubClass::some_method"

sub = SubClass()
result = sub.some_method("Hello")

assert result == "Hello SuperClass::some_method SubClass::some_method"
print(result)
