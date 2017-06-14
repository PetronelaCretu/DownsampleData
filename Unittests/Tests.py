'''
Created on 17.05.2017

@author: p.cretu
'''
import unittest
import h5py
import sys
sys.path.insert(0, '../../')



class TestHDF5FileFromPath(unittest.TestCase):
    '''
    tests that a HDF5 file is readable and has data
    Input:
        path to the file
    '''
    
    def setUp(self):
        
        self.f = h5py.File('\\\\mclserver3\\MCL Projekte\\nk021 (MIBA)\\11 (Abrollversuch)'
                  '\\Daten\\20170228\\01_Messungen an NVH-AWP\\01_FR - 20170124'
                  '\\BMWB37_SRS - FR - Ordercuts\\BMWB37_SRS - FR - Ordercuts.h5', 'r')


    def tearDown(self):
        self.f.close()
    
    def AssertReadsAllFile(self):
        for key in self.f.keys():
            self.assertIsNotNone(self.f[key].value, 'A value is None')
    
    def test_AssertAttributeValueError(self):
        with self.assertRaises(AttributeError):
            for key in self.f.keys():
                self.f[key].value
            

if __name__ == "__main__":
    unittest.main()


    
    