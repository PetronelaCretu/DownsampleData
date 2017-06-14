# -*- coding: utf-8 -*-
# Python version: 3
'''
Created on Wed June 14th 17:07:00 2017
@author: p.cretu

contains a decorator that encloses the execution of a function in a try except block

'''
import logging


logger =  logging.getLogger(__name__)

def timer(some_function):
    """
    wraps a function in a try-except block
    """
    def check(*args):
        try:
        
            data = some_function(*args)
            return data
        except Exception as e:
            print(some_function.__qualname__, e)
            logger.info(some_function.__qualname__)
            logger.info(e)
    
    return check