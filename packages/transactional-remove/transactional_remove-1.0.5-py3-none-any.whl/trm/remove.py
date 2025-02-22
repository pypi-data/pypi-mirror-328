import os
import shutil
from .utils import state, log
from .const import *

def rm(item):
    type = state(item)
    match type:
        case "file": log(item, type, RM); os.remove(item)
        case "link": log(item, type, RM); os.unlink(item)
        case "dir": log(item, type, RM); os.rmdir(item)
        case "dirf": log(item, type, RM); shutil.rmtree(item)
        case _: return
    
