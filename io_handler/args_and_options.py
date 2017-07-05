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


def getArgsOne(argv):
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


    
def ArgsOptions(script_version, program, description):
    current_date = datetime.now().strftime('%Y-%m-%d')
    parser = argparse.ArgumentParser(description = description,
                                     prog = program)
    activities_directory = './' + current_date

    # TODO: Implement verbose and/or quiet options.
    # parser.add_argument('-v', '--verbose', help="increase output verbosity", action="store_true")
    parser.add_argument('-v','--version', help="print version and exit", action="store_true")
    parser.add_argument('-h','--help', help="show information about teh program and list of program options", action="store_true")
#     parser.add_argument('--username', help="your Garmin Connect username (otherwise, you will be prompted)", nargs='?')
#     parser.add_argument('--password', help="your Garmin Connect password (otherwise, you will be prompted)", nargs='?')
    
#     parser.add_argument('-f', '--format', nargs='?', choices=['gpx', 'tcx', 'original'], default="gpx",
#         help="export format; can be 'gpx', 'tcx', or 'original' (default: 'gpx')")
    parser.add_argument('directory', nargs = '+')
    parser.add_argument('-d', '--directory', nargs='?', default=activities_directory,
        help="the data directory (default: './YYYY-MM-DD')")
    
    parser.add_argument('-u', '--unzip',
        help="if downloading ZIP files (format: 'original'), unzip the file and removes the ZIP file",
        action="store_true")
    
    return parser
    
def getArgs(parser):
    
    args = parser.parse_args()
    
    if args.version:
        print( argv[0] ) + ", version " + script_version
        exit(0)
        
    return args
   
