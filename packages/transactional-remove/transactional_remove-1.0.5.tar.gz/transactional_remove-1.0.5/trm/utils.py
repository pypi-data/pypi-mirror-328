from .const import *
from os import path, listdir

def state(item):
    if path.isfile(item):
        return FILE
    elif path.isdir(item):
        if listdir(item) != None:
            return DIRF
        else:
            return DIR
    elif path.islink(item):
        return LINK

def log(item: str, type: str, action: bool):
    pass