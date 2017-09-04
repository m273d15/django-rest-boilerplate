import re
from datetime import date


def check(description, variable, type_name):
    if (variable is None) or (not isinstance(variable, type_name)):
        raise TypeError(description)
        
def check_str(variable_name, variable, allow_empty=False):
    check(variable_name + " has to be a valid string", variable, str)

    if (not allow_empty) and (variable == ""):
        raise TypeError(variable_name + " has to be a non empty string")
        
def check_int(variable_name, variable):
    check(variable_name + " has to be a valid int", variable, int)

def check_positive_int(variable_name, variable):
    check(variable_name + " has to be a valid int", variable, int)
    if(variable < 0):
        raise TypeError(variable_name + " has to be >= 0")

def check_is_string_matching(description, variable_name, variable, pattern, flags=0):
    check_str(variable_name, variable, True)
    if not re.match(pattern, variable, flags=flags):
        raise TypeError(description)
        
def check_pattern(description, variable, pattern):
    p = re.compile(pattern)
    if not p.match(variable):
        raise TypeError(description)
        
# TODO: the specifications for this type are highly confusing! Might need refactoring. See #51
def check_dateString(description, variable_name, variable):
    check_str(variable_name, variable)
    check_pattern(description, variable, '^[0-9\s]{8,}$')
    
def check_dateValue(description, variable_name, variable):
    check(description, variable, date)
    
def check_attributeSelection(description, variable):
    check_str(description, variable, False)
	
    if(not(variable == "ALLOWED" or variable == "PROHIBITED")):
        raise TypeError(description)
        
def check_attributeRequest(description, variable):
    check_str(description, variable)

    if(not(variable == "ALLOWED" or variable == "PROHIBITED" or variable == "REQUIRED")):
        raise TypeError(description)
        
def check_attributeResponse(description, variable_name, variable):
    check_str(variable_name, variable)

    if(not(variable == "ALLOWED" or variable == "PROHIBITED" or variable == "NOTONCHIP")):
        raise TypeError(description)
        
