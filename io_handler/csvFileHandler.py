"""
"""
__python__ = "3.7"
__author__ = "pcretu"
__version__ = "1.0"

import numpy
import pandas

try:
    from ..logger.logger import Logger
    from .file_manager import FileManager
    from ..decorators.timer import timer
except ValueError as e:
    import sys
    sys.path.append("../")
    from logger.logger import Logger
    from file_manager import FileManager
    from decorators.timer import timer


log = Logger()
logger = log.logger

class CSVFileHandler(FileManager):

    def __init__(self):
        super(FileManager, self).__init__()

    @timer
    def readFile(self, inFile = None, *args,**kwargs):
        '''
        Reads a csv file with pandas

        :input: inFile - file to read, if none, the object'S set file will be used
                *args,**kwargs - arguments for the read_csv function
        :return: pandas dataframe

        '''
        try:
            if inFile is None:
                inFile = self.filePath
            if inFile.split('.')[-1] != 'csv':
                logger.critical(inFile + " file to read is not a csv file.")
                return
            data = pandas.read_csv(inFile,error_bad_lines=False, *args,**kwargs)
            if data.empty:
                logger.critical("Data read from " + inFile + " file is empty!")
                return
            return data
        except AttributeError as e:
            logger.info(self.readFile.__qualname__ + str(e) + '\n \t !!! No data read, return is null !!!')
            print(self.readFile.__qualname__ + str(e) +  '\n \t !!! No data read, return is null !!!')

    @timer
    def writeFile(self, outFile, data, *args,**kwargs):
        '''
        writes pandas dataframe to a csv file
        :input: outfile - file name/path
                data - pandas dataframe
        '''
        if type(data) is pandas.DataFrame:
            data.to_csv(outFile, *args,**kwargs)

    @timer
    def readMultipleFiles(self, folder = None, *args,**kwargs):
        '''
        Reads multiple csv file with pandas into a single dataframe

        :input: folder - folder with files to read, if none, the object's set folder will be used
                *args,**kwargs - arguments for the read_csv function

        :return: pandas dataframe

        '''
        if folder is None:
            logger.critical("Invalid folder name and/or path")
            return

        files = self.getDirectoryFiles(folder, "csv")
        if files is None or len(files) == 0:
            logger.critical("No csv files in the given folder")
            return
        dfs = list()
        for f in files:
            df = self.readFile(f)
            dfs.append(df)

        data = pandas.concat(dfs,  *args,**kwargs )

        if data.empty:
            logger.critical("Data read from " + folder + " file is empty!")
            return
        return data


