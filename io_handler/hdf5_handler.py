'''
Created on Thu June 8th 13:52:00 2017

@author: p.cretu

read and write hdf5 files
'''
import h5py
import logging
import datetime
from resources.decorators.timer import timer

logger = logging.getLogger(__name__)

class IOHDF5():
    
    def __init__(self):
        pass
    
    @staticmethod
    @timer
    def writeHDF5fromDict(self, dDict, fName, *options):
        try:
            h = h5py.File(fName)
            for k, v in dDict.items():
                h.create_dataset(k , data = v)
            h.close()
            self.generateScilab(dDict, fName)
            
        except RuntimeError as e:
            print(e)
            logger.error(e)
            print('Please check if a dataset already exists, it cannot be overwritten')
            
    @staticmethod
    @timer  
    def readHDF5(self, hdf5File):
        try:
            f = h5py.File(hdf5File, 'r')
#             for key in f.keys():
#                 print(key)
#                 print(f[key].value)
            return f
        except Exception as e:
            print(e)
            logging.error(e)
            
            
    def generateScilab(self, dDict, fName):
        scilabScript = '''//@author: p.cretu
        //Created on ''' + str(datetime.datetime.today()) + '''
        // Script to read ''' + fName +''' file content\n\n\nclear\nclc\n\n\n\n''' + \
        '''hdf5Data = h5open("''' + fName + '''.h5")\n\n\n'''
        
        for key in dDict.keys():
            key = key.strip()
            scilabScript += key.replace(' ', '') + ' = h5read(hdf5Data,\''+ fName + '/' + key +'\' )\n'
            
        scilabScript += '\nh5close(hdf5Data)'
        
        
        with open(fName + '.sce', 'w') as f:
            for line in scilabScript:
                f.write(line)
        f.closed
        
        
