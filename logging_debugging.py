import logging #built-in


#to change logging configuration

logging.basicConfig(level=logging.DEBUG)
def add(x,y):
    """Add Function"""
    return x+y
def subtract(x,y):
    """Subtraction Function"""
    return x-y

def multiply(x,y):
    """Multiplication Function"""
    return x*y

def division(x,y):
    """Division Function"""
    if y==0:
        raise ZeroDivisionError("Zero Division")
    else:
        return x/y

num1 = 10
num2 = 5

add_result = add(num1,num2)
logging.debug("Add: {} + {} = {}".format(num1,num2,add_result))

sub_result = subtract(num1,num2)
logging.debug("Subtract: {} - {} = {}".format(num1,num2,sub_result))

mult_result = multiply(num1,num2)
logging.debug("Multiply: {} x {} = {}".format(num1,num2,mult_result))

division_result = division(num1,num2)
logging.debug("Divide: {} / {} = {}".format(num1,num2,division_result))