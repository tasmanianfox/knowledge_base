# Resolving cirtular references

_Problem: parent class should be aware of child class and vice-versa_

_Use case: Hierarchy of widgets_

_Solution: "forward declaration" + include parent's header in child source file_

## Related errors
- invalid use of incomplete type class ...

## Solution

__parent.h__
```cpp
#include "child.h"

class Parent
{
public:
    int parentProperty;
protected:
    Child* child;

    void someParentFunction();
}
```
__parent.cpp__
```cpp
#include "parent.h"

void Parent::someParentFunction()
{
    this->child->childProperty = 1;
}

```
__child.h__
```cpp
class Child
{
public:
    int childProperty;
protected:
    Parent* parent;
    
    void someChildFunction();
}
```
__child.cpp__
```cpp
#include "child.h"
#include "parent.h" // !!!

void Parent::someChildFunction()
{
    this->parent->parentProperty = 2;
}

```