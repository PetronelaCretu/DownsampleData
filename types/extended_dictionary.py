'''
Created on 22.06.2017

@author: p.cretu
'''
from decorators.try_function import tryFunction


class Dictionary():
    '''
    wrapper for dict that extends dict functionality
    the class can take an existing dict as object if one given at instantiation,
    otherwise a new empty dict is created
    '''
    
    def __init__(self, dicty = None):
        if dicty:
            self._dict = dicty 
        else:
            self._dict = dict()
    
    @tryFunction
    def convertValuesToFloat(self, data):
        '''
        input: dictionary to validate
        the dict object will be filled with the converted data
        '''
        for key in data.keys():
            try:
                # convert string values to float for a whole array
                self._dict.update({key:list(map(float, data[key])) })
            except Exception as e: 
                print(e, 'Error: key ', key , 'in file ', self.fileName, ', array will not be saved', self.fileName, ' has values not valid')
                continue

        