# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:52:00 2017

@author: p.cretu
"""

import sys, getopt
import argparse
import logging
import datetime
from sys import argv


logger = logging.getLogger(__name__)
script_version = '1.0.0'


def getArgs(argv):
    '''
    function to parse the input arguments from the system and
    handle their utility 
    '''
    inputfile = list()
       
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi::o:v",["ifile=","ofile="])
    except getopt.GetoptError:
        print('*.py -i <inputfile>, ... ,<inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('*.py -i <inputfile>, ... ,<inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            for a in arg.split(','):
                inputfile.append(a)
             
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    logger.info('Input files is "', inputfile)
    logger.info( 'Output file is "', outputfile)
    return inputfile, outputfile

def getArgsFromDirectory(*args):
    inputFiles = ''
    
def ArgsOptions():
    current_date = datetime.now().strftime('%Y-%m-%d')
    parser = argparse.ArgumentParser()
    activities_directory = './' + current_date

    # TODO: Implement verbose and/or quiet options.
    # parser.add_argument('-v', '--verbose', help="increase output verbosity", action="store_true")
    parser.add_argument('--version', help="print version and exit", action="store_true")
#     parser.add_argument('--username', help="your Garmin Connect username (otherwise, you will be prompted)", nargs='?')
#     parser.add_argument('--password', help="your Garmin Connect password (otherwise, you will be prompted)", nargs='?')
    
    parser.add_argument('-c', '--count', nargs='?', default="1",
        help="number of recent activities to download, or 'all' (default: 1)")
    
    parser.add_argument('-f', '--format', nargs='?', choices=['gpx', 'tcx', 'original'], default="gpx",
        help="export format; can be 'gpx', 'tcx', or 'original' (default: 'gpx')")
    
    parser.add_argument('-d', '--directory', nargs='?', default=activities_directory,
        help="the directory to export to (default: './YYYY-MM-DD_garmin_connect_export')")
    
    parser.add_argument('-u', '--unzip',
        help="if downloading ZIP files (format: 'original'), unzip the file and removes the ZIP file",
        action="store_true")
    
    args = parser.parse_args(script_version = '1.0.0')
    
    if args.version:
        print( argv[0] ) + ", version " + script_version
        exit(0)
   
