'''
Created on 08.09.2017

@author: p.cretu
'''

import pandas
import numpy
import logging

from dataDownsamplig.LTTB import LTTB

class DataDownsampler(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._dataFrame = None
        self._dict = None
        self._nArray = None
        self._resolution = 1980 # max width HD

    
    @property
    def dataFrame(self):
        return self._dataFrame
    
    @dataFrame.setter
    def dataFrame(self, dataFrame):
        self._dataFrame = dataFrame
        
        
    @property
    def dict(self):
        return self._dict
    
    @dict.setter
    def dict(self, dict):
        self._dict = dict
        
    
    @property
    def nArray(self):
        return self._nArray
    
    @nArray.setter
    def nArray(self, nArray):
        self._nArray =  numpy.asarray(nArray)
        pass
        
    @property
    def resolution(self):
        return self._resolution
    
    @resolution.setter
    def resolution(self, resolution):
        self._resolution = resolution
        pass
        
    def downsampleDataLTTB(self):
        '''
        '''
        if self._dataFrame is not None:
            a = self._downsampleDataFrame('_downsampleDataLTTBnarray')
            return a
        elif self._dict is not None:
            return self._downsampleDataDict('_downsampleDataLTTBnarray')
            
        elif self._nArray is not None:
            return self._downsampleDataLTTBnarray()
            
            
                        
    def _downsampleDataLTTBdf(self):
        '''
        '''
        pass
    
    def _downsampleDataLTTBdict(self):
        '''
        '''
        pass
    
    def _downsampleDataLTTBnarray(self):
        '''
        Apply the Steinarsson 
        Largest-Triangle-Three-Buckets algorithm.
        
        **return**: numpy array length 2 x resolution (class attribute)
        '''
        
        lttb = LTTB()
        out = lttb.downsample(self.nArray, self.resolution)
        
        return out[1]
    
    def downsampleDataLlTTB(self):
        '''
        '''
        if self._dataFrame is not None:
            return self._downsampleDataFrame('_downsampleDataLlTTBnarray')
            
        elif self._dict is not None:
            return self._downsampleDataDict('_downsampleDataLlTTBnarray')
            
        elif self._nArray is not None:
            return self._downsampleDataLlTTBnarray()
    
    
    def _downsampleDataLlTTBdf(self):
        '''
        '''
        pass
    
    def _downsampleDataLlTTBdict(self):
        '''
        '''
        pass
    
    def _downsampleDataLlTTBnarray(self):
        '''
        modified LTTB algorithm
        '''
        pass
    
    def downsampleMinAndMax(self):
        '''
        Method to downsample data in the _downsampleDataMMnarray
        method. Here the data to be downsampled is identified and
        passed further.
        
        '''
        if self._dataFrame is not None:
            return self._downsampleDataFrame('_downsampleDataMMnarray')
            
        elif self._dict is not None:
            return self._downsampleDataDict('_downsampleDataMMnarray')
            
        elif self._nArray is not None:
            return self._downsampleDataMMnarray()
        
        
    def _downsampleDataMMnarray(self):
        '''
        Apply downsampling on a numpy array - class attribute
        This method is based on dividing the array in as many sub-arrays 
        as the resolution value(class attribute). From each sub-array 
        the min and max values are extracted and returned in a duble sized
        resolution numpy array.
        
        **return**: numpy array of length 2x resolution (class attribute)
        
        '''
        nlen = int(len(self._nArray)/self._resolution  )    #number of bins
        container = self._nArray[0 : nlen * self._resolution]
        container= container.reshape(-1 , nlen)   #create the array of bins
     
        # find min and max for each bin
        
        minAndMax =  numpy.vstack((numpy.nanmax(container,axis=1), numpy.nanmin(container,axis=1)))
        data = list()
        for i in range(minAndMax[0].size):
            data.append( minAndMax[0][i])
            data.append( minAndMax[1][i])
        dataArray = numpy.asarray(data)
        
        return dataArray
    
    
    
    
    def _downsampleDataFrame(self, function):
        '''
        Apply the downsampling method in function argument
        on a pandas dataFrame
        
        **input**: function: the name of the method/function
                   to be called on the data
                   
        **return**: resized pandas dataframe; if the data to
                    be resized is the same length or smaller 
                    than the resolution value, the original data 
                    is returned
                    
        '''
        if self._dataFrame.shape[0] <= self._resolution:
            return self._dataFrame
        
        newDF = pandas.DataFrame()
        i = 0
        for c in self._dataFrame.columns:
            self.nArray = self._dataFrame[c]
            data = getattr(self, function)()
            newDF.insert(i, c, pandas.Series(data))
            i+=1
        
        return newDF
    
    def _downsampleDataDict(self, function):
        '''
        Apply the downsampling method in function argument
        on a dict data structure
        
        **input**: function: the name of the method/function
                   to be called on the data
                   
        **return**: resized dict data structure; if the data to
                    be resized is the same length or smaller 
                    than the resolution value, the original data 
                    is returned. This is applied for each key-value
                    pair in the dictionary.
                    
        '''
        newDict = dict()
        
        for key in self._dict.keys():
            self.nArray = self._dict[key]
            if self.nArray.size <= self._resolution:
                newDict.update({key: self.nArray})
            else:
                data = getattr(self, function)()
                newDict.update({key: data})
            
        return newDict
    
    
