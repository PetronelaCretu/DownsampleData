'''
Created on 26.06.2017

@author: p.cretu
'''
import logging
from logging.handlers import RotatingFileHandler
from os import path
import sys, os



class Logger():

    def __init__(self, file = None):
        if file:
            self._logFile = path.realpath(path.dirname(sys.argv[0]) + '\\' + file)
        else:
            self._logFile = path.realpath(path.dirname(sys.argv[0]) + '\\' + 'log.log')
        
    
    @property
    def logFile(self ):
        return self._logFile
    
    @logFile.setter
    def logFile(self, logFile):
        self._logFile = path.realpath(path.dirname(sys.argv[0]) + '\\' + logFile)
       
       
    def setLogger(self):
        log_handler = RotatingFileHandler(self.logFile, maxBytes=1048576, backupCount=5)
        log_handler.setFormatter(logging.Formatter( '%(asctime)s %(levelname)s: %(message)s ' '[in %(pathname)s:%(lineno)d]'))
        logger = logging.getLogger("GA")
        logger.setLevel(logging.INFO)
        logger.addHandler(log_handler)
        logger.propagate = False
        self.log = logger
        return logger
    
    def getLogger(self):
        LOGFILE = str(os.path.realpath(os.path.dirname(sys.argv[0]) + '\\chipMain.log'))
        log_handler = RotatingFileHandler(LOGFILE, maxBytes=1048576, backupCount=5)
        log_handler.setFormatter(logging.Formatter( '%(asctime)s %(levelname)s: %(message)s ' '[in %(pathname)s:%(lineno)d]'))
        logger = logging.getLogger("GA")
        logger.setLevel(logging.INFO)
        logger.addHandler(log_handler)
        
        return self.log.getLogger()
        