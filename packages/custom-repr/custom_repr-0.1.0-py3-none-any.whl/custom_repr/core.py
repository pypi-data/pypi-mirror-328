def add_repr(cls):
    def custom_repr(self):
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
    
    cls.__repr__ = custom_repr
    return cls
