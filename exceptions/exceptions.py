
'''
python version (3.5)

Created on 31.05.2017

@author: p.cretu
'''


class NotAnImageFileError(Exception):
    '''
    exception if a file is not an image file format of type .jpg, .png
    '''

    def __init__(self, msg=None):
        self.msg = msg
        super().__init__('NotAnImageFileError: '
                        'the file is not a valid image format type: %s' % msg)


class NotAXLSXFileError(Exception):
    '''
    exception if a file is not a xlsx file
    '''

    def __init__(self, msg=None):
        self.msg = msg
        super().__init__('NotAXLSXFileError: '
                        'the file is not a valid Excel 2007 or newer file type: %s' % msg)



class NotAXMLFileError(Exception):
    '''
    exception if a file is not a xml file
    '''

    def __init__(self, msg=None):
        self.msg = msg
        super().__init__('NotAXMLFileError: '
                        'the file is not a xml file type: %s' % msg)
        
        
class NotATXTFileError(Exception):
    '''
    exception if a file is not a txt file
    '''

    def __init__(self, msg=None):
        self.msg = msg
        super().__init__('NotATXTFileError: '
                        'the file is not a txt file type: %s' % msg)
        
        
class CriticalSamplingMissingError(Exception):
    
    '''
    exception if the number of samples in a file is lower than expected
    '''

    def __init__(self, msg=None):
        self.msg = msg
        super().__init__('CriticalSamplingMissingError: '
                        'samples missing in the dataset. %s' % msg)
        
        
        
