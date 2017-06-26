'''
Created on 26.06.2017

@author: p.cretu
'''
import logging
from logging.handlers import RotatingFileHandler
from os import path
import sys



class Logger():
    def __init__(self, logFile):
        self._logFile = path.realpath(path.dirname(sys.argv[0]) + '\\' + logFile),
        self.WEBAPP_CONSTANTS = { 'LOGFILE': self._logFile, }
        
    def getWebAppConstants(self, constant):
        self.WEBAPP_CONSTANTS.get(constant, False)

    def setLogger(self):
        LOGFILE = self.getWebAppConstants('LOGFILE')
        log_handler = RotatingFileHandler(LOGFILE, maxBytes=1048576, backupCount=5)
        log_handler.setFormatter(logging.Formatter( '%(asctime)s %(levelname)s: %(message)s ' '[in %(pathname)s:%(lineno)d]'))
        logger = logging.getLogger("GA")
        logger.setLevel(logging.INFO)
        logger.addHandler(log_handler)
        return logger
