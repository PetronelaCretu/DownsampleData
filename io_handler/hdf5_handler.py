'''
Created on Thu June 8th 13:52:00 2017

@author: p.cretu

read and write hdf5 files
'''
import h5py
import logging
from decorators.timer import timer

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
            
