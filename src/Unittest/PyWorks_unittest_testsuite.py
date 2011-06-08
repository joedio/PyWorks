#--
#=============================================================================#
# File: PyWorks_unittest_testsuite.py
#
#  Copyright (c) 2008-2011, Joe DiMauro
#  All rights reserved.
#
#
# Description:  This script performs the following:
#                    a) Defines global variables shared among the tests in this testsuite.
#                    b) Starts a log file that's shared among the tests in this testsuite.
#                    c) Starting at the directory where this file resides it transverses the directory and
#                       its sub-directory tree collecting an alpha sorted list (a-z) of test files
#                       (files ending in *_unittest,py) and then executes each test file.
#
# Instructions: 1. Copy this file into the parent directory containing your test files
#               2. Edit the global variable definitions in this file as needed for the test run
#               3. Execute this file (see details below).
#
# Execution:   To run your Testsuite (e.g. Testsuite,py):
#                 a) From ScITE:
#                      1. Open your Testsuite.py in ScITE (Right click on the .py file & select Edit)
#                      2. From the ScITE tool select Tools > Go  or press F5
#                 b) From a DOS Command Console window:
#                      1. Change directory (cd) to the location of your Testsuite,py
#                      2. To run and re-direct stdout (1) & stderr (2) to a text file:
#                              jython -m Testsuite.py >> stdout.txt 2>&1
#                 c) From an Cygwin window:
#                      1. Change directory (cd) to the location of your Testsuite,py
#                      2. To run in the background and re-direct stdout ($1) & stderr ($2) to a text file:
#                               jython -m  Testsuite.py $1$2 >> stdout.txt &
#
# Analysis:       View the contents of the time-stamped logfile (that will be created in
#                 the ./results sub-directory), and the stdout for any failures.
#
#                 Note: If the Testsuite or individual Test files re-run the previous results directory will
#                       be renamed with an appended time-stamped.
#
#
# Restrictions:
#                Neither this file, the *_test,py nor  the *_lib,py files may reside at the top
#                level of the file system.
#
#                Only Testsuite files should end with _testuite,py
#                Only Test files should end with _test,py
#
#                Test files must reside in the same directory or a sub-directory of their testsuite file.
#                Test files must end with _test,py in order to be included for execution in the testsuite.
#
#                Individual test files should NOT open their Browser of Log file directly, but
#                should use the methods startBrowser() or startLogger(). This will ensure that the tests
#                can be run either collectively as a part of a testsuite, or individually apart of a testsuite,
#                and still have access to a log file, and a single results sub-directory.
#
#                Individual test files should NOT CLOSE the log file!
#
#                Individual test files should inherit the settings of any global variables
#                from the testsuite that launched them.
#
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by these methods
#=============================================================================#

import os                           # Adds ability to access OS
import re                           # Regular expressions
from datetime import datetime

#import logging                      # The Jython logger which is the basis for the PyWorksLogger

# PyWorks
#from PyWorks_Reflib import *       #  PyWorks Reference data module
from PyWorks_Utilities import print2, get_text_from_file, list_tree, prefix, suffix, calc_elapsed_time    # PyWorks General Utilities

#=============================================================================#


#=============================================================================#
# Global Variables section
# Set global variables that will be inherited by each of the test files
#=============================================================================#

# Java global variables
#======================
#

# PyWorks global variables
#============================
# Set the variable VERBOSE to True for help in debugging scripts
global VERBOSE
VERBOSE = False
#
# Set the variable $DEBUG to True for help in debugging scripts
global DEBUG
DEBUG = False

# Clear the PyWorks flag since no logger has been started yet
global bLoggerStarted
bLoggerStarted = False

# Set the PyWorks sRun_TestType variable to your choice of tests to launch
# for this test run . Define any types you like and add a local variable
# (sRun_TestType = "sMyType") in your individual tests.
# Only tests matching this setting will be run.
# ("" = ignore setting)
sRun_TestType = "ready"
#sRun_TestType = "wip"
#sRun_TestType = ""

# Set the PyWorks iRun_TestLevel variable to your choice of test level to launch
# for this test run. Set the level (1-5) as a local variable (iRun_TestLevel = iMyLevel)
# setting in your individual tests.
# Only tests with a level <= this setting will be run.
# (0 = ignore setting)(1=highest level, 5 = lowest level)
iRun_TestLevel = 0

# Application Under Test global variables
#

#=============================================================================#

#=============================================================================#
# Main code section
#=============================================================================#

# Not running a logger for the unit test


#=======================================
# Collect list of possible files to run
#=======================================

# Define the LIST to hold the list of test files
aMyTestList = []

# Define the search criteria
sFilesToFind = "_unittest.py"

# Loop through the directory and sub-directories using the find command to collect
# the list of files. Weeding out the numerous pathnames that don't end with a valid
# test file name (files ending  with _test,py).
#aPathlist = os.listdir(".")

# Get the Current Working Directory
sRootDir = os.getcwd()

if (VERBOSE == True):
    print2("PWD = " + sRootDir)
# end

# Get a Recursive listing of sub-directories
aPathlist = list_tree(sRootDir)


if(VERBOSE == True):
    #print2(aPathlist)
    pass
# end

# Parse the Recursive listing of sub-directories for files that match the search criteria

# Loop through the Recursive listing of sub-directories
for sPath in aPathlist:
    
    if(VERBOSE == True):
        print2(sPath)
    # end
    
    # Check for files matching the search criteria
    # Does the current pathname/filename contain a match
    if (re.match(r'.*' + sFilesToFind, os.path.basename(sPath))):
        # Append the list of matching files
        #aMyTestList = aMyTestList + hPossibleMatchingFiles
        aMyTestList.append( sPath)
    #end
# end Loop
    
if(VERBOSE == True):
    print2("_*")
    print2(aMyTestList)
    print2("*_")
# end

# Determine if file list needs to be pruned
if((sRun_TestType != "") | (iRun_TestLevel != 0)):
    
    # Display the number of test files
    print2("\nNumber of Test files found: " + str(len(aMyTestList)))
    
    # Display the alpha sorted list of all test files
    print2(aMyTestList)
    print2("")
    
else:
    print2("PyWorks ignoring settings for: sRun_TestType and iRun_TestLevel")
# end


#=============================================================#
# Prune the test file list based on the sRun_TestType setting
#=============================================================#
if(sRun_TestType != ""):
    
    # Define the LIST to hold the list of files to run
    aTestTypeListToRun =[]
    
    print2("Removing all tests without sRun_TestType = " + sRun_TestType)
    
    # Check each file in the list
    for sTestFile in aMyTestList:
        
        if(VERBOSE == True):
            print2("\nChecking file: " + sTestFile)
        # end
        
        # Find matches in the current file (only check the 1st 100 lines in the file)
        aMyMatches = get_text_from_file("sRun_TestType", sTestFile, 0, 100)
        
        if(VERBOSE == True):
            print2("Parsing file search results")
            print2(str(aMyMatches))
        # end
        aMatch = aMyMatches
        
        if(VERBOSE == True):
                print2("Match found: " + str(aMatch))
        # end
        
        # Loop through results LIST of the search
        if (aMatch[0] == False):
            
            if(VERBOSE == True):
                print2(" Skipping tests w/o matching variable string: " + sTestFile)
                sLine = "#"
            # end
            
        else:
            # Get the 1st match
            sLine = str(aMatch[2])
            
            if(VERBOSE == True):
                print2(" Line: " + sLine)
            # end
            
            
        # end # Loop through results of search
        
        # Remove any commented out lines
        sLine = prefix(sLine, "#")
        
        # Cleanup the line
        sLine = sLine.replace('"', '') # Remove double quotes
        sLine = sLine.replace("'", "'") # Remove single quotes
        sLine = sLine.replace(" ", "") # Remove whitespace
        
        # Save the setting portion of the line
        sSetting = suffix(sLine,"=")
        
        if(VERBOSE == True):
            print2(" Setting = '" + sSetting.lower() + "'")
        # end
        
        # Determine to keep or drop the test file
        if not(sSetting.lower() in sRun_TestType):
            if(VERBOSE == True):
                print2(" Dropping test file: " + sTestFile)
            # end
            
        else:
            
            if(VERBOSE == True):
                print2(" Keeping test file: " + sTestFile)
            # end
            
            # Add it to the list
            aTestTypeListToRun.append(sTestFile)
            
        # end # Determine to keep or drop the test file
        
    # end # Match found
    
    # Re-populate the LIST with the remaining files to run
    aMyTestList = aTestTypeListToRun
    
# end # Check each file in the list


# end # Prune the test file list based on the sRun_TestType settings

#=============================================================#
# Prune the test file list based on the iRun_TestLevel setting
#=============================================================#
if(iRun_TestLevel != 0):
    
    # Define the LIST to hold the list of files to run
    aTestLevelListToRun =[]
    
    print2("Removing all tests with iRun_TestLevel < " + str(iRun_TestLevel))
    
    # Check each file in the list
    for sTestFile in aMyTestList:
        
        if(VERBOSE == True):
            print2("\nChecking file: " + sTestFile)
        # end
        
        # Find matches in the current file (only check the 1st 100 lines in the file)
        aMyMatches = get_text_from_file("iRun_TestLevel", sTestFile, 0, 100)
        
        if(VERBOSE == True):
            print2("Parsing file search results")
        # end
        aMatch = aMyMatches
        
        if(VERBOSE == True):
            print2("Match found: " + str(aMatch[0]))
        # end
        
        # Check the results of the search
        if (aMatch[0] == False):
            
            
            # Match found
            #if(aMatch[0] != True):
            
            if(VERBOSE == True):
                print2(" Skipping tests w/o matching variable string: " + sTestFile)
                sLine = "#"
            # end
            
        else: # Search found a setting that needs to be checked
            
            # Get the 1st match
            sLine = str(aMatch[2])
            
            if(VERBOSE == True):
                print2(" Line: " + sLine)
            # end
            
            
            # end # Loop through results of search
            
            # Remove any commented out lines
            sLine = prefix(sLine, "#")
            
            if(VERBOSE == True):
                print2("Found line: " + sLine)
            # end
            
            # Cleanup the line
            sLine = sLine.replace('"', '') # Remove double quotes
            sLine = sLine.replace("'", "'") # Remove single quotes
            sLine = sLine.replace(" ", "") # Remove whitespace
            
            # Save the setting portion of the line
            sSetting = str(sLine).suffix("=")
            
            if(VERBOSE == True):
                print2(" Setting = '" + sSetting.lower() + "'")
            # end
            
            # Convert the string to an integer
            iSetting = int(sSetting)
            
            # Determine to keep or drop the test file
            if(iSetting > iRun_TestLevel):
                
                if(VERBOSE == True):
                    print2(" Dropping test file: " + sTestFile)
                # end
                
            else:
                
                if(VERBOSE == True):
                    print2(" Keeping test file: " + sTestFile)
                # end
                
                # Add it to the list
                aTestLevelListToRun.append(sTestFile)
                
            # end # Determine to keep or drop the test file
            
        # end # Match found
        
        # Re-populate the LIST with the remaining files to run
        aMyTestList = aTestLevelListToRun
        
    # end # Check each file in the list

#end # Prune the test file list based on the sRun_TestLevel settings

#=============================================================#

# Display the number of test files
print2("\nNumber of Test files to run: " + str(len(aMyTestList)))

# Display the alpha sorted list of test files that will be run
for sTestFile in aMyTestList:
    print2(sTestFile)
    # end

# Get the starting time of the unittest execution
tTestSuite_StartTime = datetime.now()
print2("Test suite start time = " + str(tTestSuite_StartTime))

# Execute each test file in the list (A-Z)
for sTestfile in aMyTestList:
    execfile(sTestfile)

#print2("Test Suite finished in " + calc_elapsed_time(tTestSuite_StartTime) + " (h:m:s.ms)")

# End File: PyWorks_unittest_testsuite.py