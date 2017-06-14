
'''
python version (3.5)

Created on 6.06.2017

@author: p.cretu
'''
import logging
from datetime import datetime

from io_handler.file_manager import SelfDocumenting


logger = logging.getLogger(__name__)


class Validator(SelfDocumenting):
    
    def __init__(self):
        pass
    
    def isInteger(self, value):
        try:
            isinstance(value, int)
        except Exception as e:
            logger.info(e)
            logger.info(self.isInteger.__qualname__, str(value))
            print(self.isInteger.__qualname__, value, e)
    
    def isFloat(self, value):
        ''' numpy.finfo(float)'''
        try:
            isinstance(value, float)
        except Exception as e:
            logger.info(e)
            logger.info(self.isFloat.__qualname__ + str( value)  )
            print(self.isFloat.__qualname__, value, e)
            

    def isString(self, value):
        try:
            isinstance(value, str)
        except Exception as e:
            logger.info(e)
            logger.info(self.isString.__qualname__ + value)
            print(self.isString.__qualname__, value, e)
            
    def isDate(self, value):
        try:
#             datetime.strptime(value, '%m/%d/%Y %I:%M %p')
            return datetime.strptime(value, '%d.%m.%Y')# day, month, year
        except Exception as e:
            logger.info(e)
            logger.info(self.isDate.__qualname__ + str(value))
            print(self.isDate.__qualname__, value, e)
            
    def isDateAfter(self, date, value):
        if self.isDate(date) > self.isDate(value):
            raise ValueError('{0!s} happened prior to {1!s}, which is not allowed in this data set, please check your data'.format(value, date))
        
        
    
                
            
            
