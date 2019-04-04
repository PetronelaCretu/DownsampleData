
__python__ = "3.7"
__author__ = "pcretu"
__version__ = "1.0"

'''
Created on 26.06.2017

@author: p.cretu
'''
import logging
from logging.handlers import RotatingFileHandler
from os import path
import sys, os


class Logger():

    def __init__(self, file=None):
        if file and sys.argv[0] != '':
            self._logFile = path.realpath(path.dirname(os.getcwd()) + '\\' + file)
        else:
            self._logFile = path.realpath(path.dirname(os.getcwd()) + '\\' + 'log.log')

        self._logger = None
        self.setLogger()

    @property
    def logFile(self):
        return self._logFile

    @logFile.setter
    def logFile(self, logFile):
        self._logFile = path.realpath(path.dirname(os.getcwd()) + '\\' + logFile)

    @property
    def logger(self):
        return self._logger

    def setLogger(self):
        log_handler = RotatingFileHandler(self.logFile, maxBytes=1048576, backupCount=5)
        log_handler.setFormatter(
            logging.Formatter('%(asctime)s %(levelname)s: %(message)s ' '[in %(pathname)s:%(lineno)d]'))
        logger = logging.getLogger("GA")
        logger.setLevel(logging.INFO)
        logger.addHandler(log_handler)
        logger.propagate = False
        self._logger = logger


# decorator with logger object input parameter
def logIt(logger, level = logging.INFO):
    def loggerDecorator(function):
        def wrapper(*args, **kwargs):
            logger.setLevel(logging.INFO)
            result = function(*args, **kwargs)
            logger.info(function.__qualname__ + 'with output: ' +str(result))
            return result
        return wrapper
    return loggerDecorator