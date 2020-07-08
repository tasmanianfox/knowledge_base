# Function arguments

### Number of arguments should be LOW

As for me, _"low"_ means 2-3 arguments. If there are more arguments need to be passed, they could be packed into an object.

__A workaround for cases when a large number of arguments is really needed__

Use structures / hashmaps / dictionaries / instances of class / objects / however it is called in your language

Instead of

```python
def my_function(first_name, last_name, age, height, weight)
    # code here

my_function("John", "Doe", 21, 178, 85)
# A question from another developer: what the heck do last number mean?
# Need to look up the function signature
```

use

```python
class Person:
  def __init__(self):
    self.first_name = self.last_name = self.age = \
        self.height = self.weight = None

def my_function(person):
  # code here

person = Person()
person.first_name = "John"
person.last_name = "Doe"
person.age = 21
person.height = 178
person.weight = 85

my_function(person)
```
More code? Yes. More readable? YES.

__Example of a function with many arguments__

_A WinAPI function which creates a window:_

Source: [Microsoft documentation](https://docs.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window#creating-the-window)

```c
HWND hwnd = CreateWindowEx(
    0,                              // Optional window styles.
    CLASS_NAME,                     // Window class
    L"Learn to Program Windows",    // Window text
    WS_OVERLAPPEDWINDOW,            // Window style

    // Size and position
    CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,

    NULL,       // Parent window    
    NULL,       // Menu
    hInstance,  // Instance handle
    NULL        // Additional application data
    );
```

12 arguments in total.

__Why functions with a large number of arguments are bad:__

- You will more likely mess up with order of arguments
- In case of changes in definition you will need to change function invocations as well