'''
Created on 08.09.2017

@author: p.cretu
'''
import unittest
from matplotlib import pyplot

from io_handler.hdf5_handler import IOHDF5
from dataDownsamplig.dataDownsampler import DataDownsampler

class Test(unittest.TestCase):


    def setUp(self):
        iohdf5 = IOHDF5()
        file = '\\\\mclserver3\\MCL Projekte\\nk153 (CHIP)\\05 (WP5 Prozessdatenanalyse und Korr)\\Arbeitsordner\\Sanity Checks_ HDF5\\Chip files\\SpikeData_V2_B002_011.h5'
        self.dDict = iohdf5.readHDF5ToDict(file)
        self.df = iohdf5.dictToDataFrame(self.dDict)
        self.dataDownsampler = DataDownsampler()
        self.dataDownsampler.dataFrame = self.df
        self.df.plot()
        

    def tearDown(self):
        pyplot.show()


    def testMinAndMAxDownsamplingOnDataFrame(self):
        self.downsampledMMDF = self.dataDownsampler.downsampleMinAndMax()
        self.downsampledMMDF.plot()
        self.assertIsNotNone(self.downsampledMMDF, 'check it')
        
    def testLTTBDownsamplingOnDataFrame(self):
        self.downsampledLTTBdf = self.dataDownsampler.downsampleDataLTTB()
        self.downsampledLTTBdf.plot()
        self.assertIsNotNone(self.downsampledLTTBdf, 'check it')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
