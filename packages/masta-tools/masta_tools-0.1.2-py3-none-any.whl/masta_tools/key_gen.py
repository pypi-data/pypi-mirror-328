# -*- coding: utf-8 -*-
import string, random

def gen_alphanumeric_key(length:int=24, case_sensitive:bool=True):
    """Generate a randomized key using numbers and letters"""
    allowed = list(string.ascii_letters + string.digits)
    if not case_sensitive:
        allowed = list(set([str(x).upper() for x in allowed]))
    return ''.join(random.choice(allowed) for i in range(length))

def gen_alpha_key(length:int=24, case_sensitive:bool=True):
    """Generate a randomized key using only letters"""
    allowed = list(string.ascii_letters)
    if not case_sensitive:
        allowed = list(set([str(x).upper() for x in allowed]))
    return ''.join(random.choice(allowed) for i in range(length))

def gen_numeric_key(length:int=24):
    """Generate a randomized key using only numbers"""
    allowed = list(string.digits)
    return ''.join(random.choice(allowed) for i in range(length))


def gen_power_key(length, case_sensitive=True, include_chars="", exclude_chars=""):
    allowed = list(string.ascii_letters + string.digits)
    if not case_sensitive:
        allowed = [char.upper() for char in allowed]
    allowed = [char for char in allowed if char not in exclude_chars]
    allowed += [char for char in include_chars if char not in allowed]
    if isinstance(length, tuple):
        min_length, max_length = length
        length = random.randint(min_length, max_length)
    elif isinstance(length, int):
        length = length
    return ''.join(random.choice(allowed) for _ in range(length))