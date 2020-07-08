# Blocks

## Empty blocks

Code blocks MUST contain non-empty lines of code. The code below will throw an error _"IndentationError: expected an indented block"_:

```python
if condition_a:

elif condition_b:
    print("TEST")
```

If any block really has to be empty, use the `pass` keyword:

```python
if condition_a:
    pass
elif condition_b:
    print("TEST")
```

It works with other kinds of blocks - classes, loops, etc:

```python
class EmptyClass(BaseClass):
    pass

for x in range(1, 10):
    pass
```