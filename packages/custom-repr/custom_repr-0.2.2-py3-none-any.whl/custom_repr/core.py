# def add_repr(cls):
#     """Decorator to add custom representation to a specific class."""
#     def custom_repr(self):
#         attribute_list = []
#         for key, value in self.__dict__.items():
#             if isinstance(value, str):
#                 formatted_value = f'"{value}"'
#             else:
#                 formatted_value = repr(value)
#             attribute_string = f"{key}: {formatted_value}"
#             attribute_list.append(attribute_string)
#         attributes_string = ", ".join(attribute_list)
#         result = f"{self.__class__.__name__}({attributes_string})"
#         return result
    
#     # Only set __repr__ if it hasn't been explicitly defined
#     if '__repr__' not in cls.__dict__:
#         cls.__repr__ = custom_repr
#     return cls
# main.py
import builtins

# Save the original __build_class__ function
original_build_class = builtins.__build_class__

# Define the custom repr function
def custom_repr(self):
    """Custom representation for all classes."""
    attribute_list = []
    for key, value in self.__dict__.items():
        if isinstance(value, str):
            formatted_value = f'"{value}"'
        else:
            formatted_value = repr(value)
        attribute_string = f"{key}: {formatted_value}"
        attribute_list.append(attribute_string)
    attributes_string = ", ".join(attribute_list)
    result = f"{self.__class__.__name__}({attributes_string})"
    return result

# Define a custom metaclass
class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        if '__repr__' not in dct:
            dct['__repr__'] = custom_repr
        return super().__new__(cls, name, bases, dct)

# Define a custom __build_class__ function
def custom_build_class(func, name, *args, **kwargs):
    return original_build_class(func, name, *args, metaclass=CustomMeta, **kwargs)

# Monkey-patch __build_class__
builtins.__build_class__ = custom_build_class