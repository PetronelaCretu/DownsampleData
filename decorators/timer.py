# -*- coding: utf-8 -*-
# Python version: 3
'''
Created on Thu May 2 12:51:00 2017
@author: p.cretu

contains a decorator to estimate execution time of a function

'''
import time
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)


def timer(some_function):
    """
    Outputs the time a function takes
    to execute
    """

    def tic_toc(*args, **kwargs):
        startTime = time.monotonic()

        data = some_function(*args, **kwargs)

        endTime = time.monotonic()
        print(some_function.__qualname__, 'execution time: ', timedelta(seconds=endTime - startTime))
        logger.info(some_function.__qualname__ +
                    'execution time: ' +
                    str(timedelta(seconds=endTime - startTime)))
        return data

    return tic_toc




