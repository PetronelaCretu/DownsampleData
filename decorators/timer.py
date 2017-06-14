# -*- coding: utf-8 -*-
# Python version: 3
'''
Created on Thu May 2 12:51:00 2017
@author: p.cretu

contains a decorator to estimate execution time of a function

'''
import time
from datetime import timedelta


def timer(some_function):
    """
    Outputs the time a function takes
    to execute
    """
    def tic_toc(*args):
        startTime = time.monotonic()
        
        data = some_function(*args)
        
        endTime = time.monotonic()
        print(some_function.__qualname__, timedelta(seconds=endTime - startTime))
        return data
    
    return tic_toc




