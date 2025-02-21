# Custom Repr

A simple decorator to add pretty representation to Python classes.

## Installation

```sh
pip install custom-repr
```

## Usage

```python
from custom_repr import add_repr

# Apply this decorator to automatically enhance your class with a custom __repr__ method, providing a better representation of object.
@add_repr  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

print(person)  # Person(name: "John", age: 30)