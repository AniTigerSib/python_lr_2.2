"""mmm = my_math_module
module for generating random values in a given range. Functions: gen_1, gen_2"""
from random import randint, randrange

def gen_1():
    """
    gen_1()
    generates a random integer between -97 and -21 and returns it
    """
    rand = randint(-97, -21)
    return rand

def gen_2():
    """
    gen_2()
    generates a random number between -95 and -31 with step 6 and returns it as float
    """
    rand = float(randrange(-95, -31, 6))
    return rand