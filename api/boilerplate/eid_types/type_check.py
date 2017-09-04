import re


def check(description, variable, type_name):
    if (variable is None) or (not isinstance(variable, type_name)):
        raise TypeError(description)
    
