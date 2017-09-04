import re


def check(description, variable, type_name):
    if (variable is None) or (not isinstance(variable, type_name)):
        raise TypeError(description)
        
def check_str(variable_name, variable, allow_empty=False):
    check(variable_name + " has to be a valid string", variable, str)

    if (not allow_empty) and (variable == ""):
        raise TypeError(variable_name + " has to be a non empty string")

def check_is_string_matching(description, variable_name, variable, pattern, flags=0):
    check_str(variable_name, variable, True)
    if not re.match(pattern, variable, flags=flags):
        raise TypeError(description)
        
