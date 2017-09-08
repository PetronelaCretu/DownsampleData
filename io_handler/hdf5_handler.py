'''
Created on Thu June 8th 13:52:00 2017

@author: p.cretu

read and write hdf5 files
'''
import h5py
import logging
import datetime
import pandas

from decorators.timer import timer

logger = logging.getLogger(__name__)

class IOHDF5():
    
    def __init__(self):
        pass
    

    @timer
    def writeHDF5fromDict(self, dDict, fName, *options):
        h = h5py.File(fName)
        for k, v in dDict.items():
            try:
                h.create_dataset(k , data = v)
            except Exception as e:
                print(e)
                #logger.error(e)
        h.close()
        self.generateScilab(dDict, fName)

   
    @timer  
    def showFileDescription(self, hdf5File):
        try:
            print('The file contains: ')
            with h5py.File(hdf5File, 'r') as f:
                for key in f.keys():
                    print(key + 
                          ' Data Set containing \t' + 
                          str(len(f[key].value)) + 
                          ' values of type \t' + 
                          str(f[key].value.dtype) )
        except Exception as e:
            print(e)
            logging.error(e)

            
    def readHDF5ToDict(self, hdf5File):
        hdf5Dict = dict()
        try:
            with h5py.File(hdf5File, 'r') as f:
                for key in f.keys():
                    hdf5Dict.update({ key: f[key].value } )
                f.close()
            return hdf5Dict
        
        except Exception as e:
            print(e)
            #logging.error(e)
            
    def generateScilab(self,  dDict, fName):
        scilabScript = '''//@author: p.cretu
        //Created on ''' + str(datetime.datetime.today()) + '''
        // Script to read ''' + fName +''' file content\n\n\nclear\nclc\n\n\n\n''' + \
        '''//hdf5Data = h5open("''' + fName + '''")\n\n\n
        hdf5DataGet = uigetfile ("*.h5","Select 1  Data File(s)"); \n\n
        hdf5Data = h5open(hdf5DataGet)\n\n\n'''
        
        for key in dDict.keys():
            if dDict[key][0] is None:
                pass
            else:
                key = key.strip()
                scilabScript += key.replace(' ', '') + ' = h5read(hdf5Data,\''+  key +'\' )\n'
            
        scilabScript += '\nh5close(hdf5Data)'
        
        
        with open(fName.replace('.h5', '.sce'), 'w') as f:
            for line in scilabScript:
                f.write(line)
        f.closed
        
    
    def dictToDataFrame(self, dataDict):
        tracesdf = pandas.DataFrame.from_dict(dataDict)
        return tracesdf
    
    
        