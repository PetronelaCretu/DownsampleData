
'''
Created on Thu March 7 8:45:00 2019
@author: p.cretu

contains a decorator to estimate execution time of a function

'''
__version__ = '1.0'
__pythonVersion__ = '3.7'

import logging

logger = logging.getLogger(__name__)


def testIt(some_function):
    """
    Calls the function without executing it,
    reminds developer to test it first
    mocks output
    """

    def norun(*args, **kwargs):

        data = some_function(*args, **kwargs)

        logger.error(some_function.__qualname__ +
                    'Test the function!' )
        print(some_function.__qualname__ +
                    ' Test the function!' )
        return data

    return norun




