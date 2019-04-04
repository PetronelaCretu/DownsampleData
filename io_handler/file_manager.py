
__python__ = "3.7"
__author__ = "pcretu"
__version__ = "1.0"

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:52:00 2017

@author: p.cretu
"""

import os

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

try:
    from ..logger.logger import Logger
    from ..decorators.timer import timer
except ValueError as e:
    import sys

    sys.path.append("../")
    from logger.logger import Logger
    from decorators.timer import timer

log = Logger()
logger = log.logger


class FileManager(object):
    '''
    class to create an object that handles a file:
        check the files path
        read, write,
        find files of a certain type in a directory

    '''

    def __init__(self):
        self._filePath = None
        self._fileName = None
        self._folder = None

    @property
    def folder(self):
        return self._folder

    @folder.setter
    def folder(self, folder):
        '''
        check that the folder path exists
        '''
        if os.path.isdir(folder):
            self._folder = folder
        else:
            raise FileNotFoundError

    @property
    def filePath(self):
        return self._filePath

    @filePath.setter
    def filePath(self, filePath):
        '''
        check that the file path exists, as well as the file
        '''
        if os.path.isfile(filePath):
            self._filePath = filePath
        else:
            raise FileNotFoundError

    @property
    def fileName(self):
        if self._filePath:
            return self.getfNameFromPath()

    @fileName.setter
    def fileName(self, fileName):
        '''
        check that the file name exists
        '''
        if fileName and os.path.isfile(fileName):
            self._fileName = fileName
        elif self.getfNameFromPath() \
                and os.path.isfile(self.getfNameFromPath()):
            self._fileName = self.getfNameFromPath()

    def getfNameFromPath(self):
        '''
        retrirves file name from the path
        '''
        return self._filePath.split('\\')[-1]

    @timer
    def readFile(self, inFile):
        '''
        text file read
        '''
        with open(inFile, 'r') as f:
            data = f.read()
        f.closed()
        return data

    @timer
    def writeFile(self, outFile, data):
        '''
        text file write
        input: outfile - file name/path
               data - string to write in file
        '''
        with open(outFile, 'w') as f:
            for line in data:
                f.write(line)
        f.closed()

    def getDirectoryFiles(self, dir, extension=None):
        try:
            self.folder = dir
        except FileNotFoundError as e:
            logger.info(e)
            print(e, dir, '\tis not a valid folder path')
            return None

        listFiles = list()
        if extension is not None:
            for path, subdirs, files in os.walk(dir):
                for name in files:
                    if name.endswith(extension.lower()) or name.endswith(extension.upper()):
                        listFiles.append(os.path.join(path, name))
        else:
            for path, subdirs, files in os.walk(dir):
                for name in files:
                    listFiles.append(os.path.join(path, name))

        return listFiles

    def getFileName(self, file):
        fileName = file.split('\\')[-1]
        return fileName

    def printAndLog(self, msg):
        print(msg)
        logger.info(msg)

    def getFileSelector(self, title="Select file", fileType=None):
        Tk().withdraw()
        if fileType is not None:
            filetypes = ((fileType + " files",
                          "*." + fileType), ("all files", "*.*"))
        else:
            filetypes = filetypes = (("all files", "*.*"), ("all files", "*.*"))
        try:
            filename = askopenfilename(initialdir="/", filetypes=filetypes,
                                       title=title)  # show an "Open" dialog box and return the path to the selected file
            if filename:
                self.filePath = filename
                return self.filePath
        except FileNotFoundError as e:
            logger.warning("No file was selected")
            return


    def getFolderSelector(self):
        Tk().withdraw()
        folderPath = askdirectory()
        self.folder(folderPath)
        return self.folder
