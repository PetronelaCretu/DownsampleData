'''
Created on 22.06.2017

@author: p.cretu
'''
from decorators.try_function import tryFunction


class Dictionary(dict):
    '''
    wrapper for dict that extends dict functionality
    the class can take an existing dict as object if one given at instantiation,
    otherwise a new empty dict is created
    '''
    
    def __init__(self):
        super().__init__()
    
    @tryFunction
    def convertValuesToFloat(self):
        '''
        the dict object will be copied and refiled with the converted data
        '''
         
        for key in self.keys():
            try:
                # convert string values to float for a whole array
                self.update({key:list(map(float, self[key])) })
            except Exception as e: 
                print(e, 'Error: key ', key , 'in file ', self.fileName, ', array will not be saved', self.fileName, ' has values not valid')
                continue





        