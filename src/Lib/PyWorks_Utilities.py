#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_Utilities.py
#
#  Copyright (c) 2008-2011, Joe DiMauro
#  All rights reserved.
#
# Description: Functions and methods for PyWorks
#    These functions and methods are application and platform independent,
#    and are NOT specific to Web based applications.
#
#    Some of these methods and functions have been collected from, or based upon
#    Open Source versions found on various sites in the Internet, and are noted.
#
#--
#
#++
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by these methods
#=============================================================================#

# Jython imports
import sys
import traceback
import os                           # Adds ability to set/get OS Variables
from datetime import date, datetime, timedelta # Add ability to get/format Dates
import time                         # Add ability to get/format Time
import random                       # Random number generator
import re                           # Regular expressions

# PyWorks imports
from PyWorks_Reflib import TIMESTAMP_STRING


#=============================================================================#
# PyWorks_Utilities
#=============================================================================#
#
# Description: Functions and methods for PyWorks
#    These functions and methods are application and platform independent.
#
#    Some of these methods and functions have been collected from, or based upon
#    Open Source versions found on various sites in the Internet, and are noted.
#
#
# Instructions: To use these methods in your scripts add these commands:
#                        from PyWorks_Utilities import *    # PyWorks General Utilities
#--
# Table of Contents
#
#  Please manually update this TOC with the alphabetically sorted names of the items in this module,
#  and continue to add new methods alphabetically into their proper location within the module.
#
#  Key:   () = No parameters,  (...) = parameters required
#
# Functions:
#    calc_datestrings()
#    calc_elapsed_time(...)
#    comma_delimit(...)
#    ### capture_results(...)
#    compare_files(...)
#    compare_strings_in_lists(...)
#    convert_date(...)
#    create_subdirectory(...)
#    display_java_env(...)
#    display_jython_env()
#    display_PyWorks_env(...)
#    find_folder_in_tree(...)
#    find_tmp_dir()
#    format_dateString_mdyy(...)
#    format_dateString_mmddyyyy(...)
#    format_from_currency(...)
#    format_to_currency(...)
#    get_env(...)
#    get_PyWorks_install_path()
#    get_text_from_file(...)
#    getMatchingKeyValue(...)
#    invertDict()
#    is_blank(...)
#    is_linux()
#    is_osx()
#    is_mac()
#    is_SOATest()
#    isValid_EmailAddress()
#    isValid_Password()
#    isValid_TopLevelDomain()
#    isValid_ZipCode()
#    is_win()
#    is_win32()
#    is_win64()
#    list_subdirs(...)
#    list_tree(...)
#    ordinal()
#    parse_ascii_file(...)
#    ##parse_csv_file(...)
#    parse_dictionary()
#    prefix(...)
#    printenv(...)
#    print2(...)
#    random_alphanumeric(...)
#    random_boolean()
#    random_char(...)
#    random_chars(...)
#    random_number(...)
#    random_paragraph(...)
#    random_pseudowords(...)
#    random_sentence(...)
#    random_word(...)
#    remove_prefix(...)
#    remove_suffix(...)
#    reverse_string()
#    set_env(...)
#    ##start_logger(...)
#    string_to_date(...)
#    subdirs(...)
#    suffix(...)
#    to_sentance(...)
#    word_count()     # alias  wc()
#
# Pre-requisites:
# ++
#=============================================================================#

# Version of this module
PW_UTILITIES_VERSION = "1.0.3"

# Format to use when appending a timestamp to file names
#DATETIME_FILEFORMAT = "%Y_%m_%d_%H%M%S"

# Name of PyWorks default data directory
DATA_DIR = "data"

# Name of PyWorks default results directory
RESULTS_DIR = "results"

# Define values for True/False since they were not defined in Jython2.2.1
True = 1
False = 0

#  Define the PyWorks Global logger variable to suppress messages when VERBOSE is True
global bLoggerStarted
bLoggerStarted = False

global oLogger
#oLogger = False

#  Define the PyWorks Global dictionary variable to suppress messages when VERBOSE is True
global DICTIONARY
DICTIONARY = None

# Clear the Verbose flag
global VERBOSE
VERBOSE = False


#=============================================================================#
#--
# Function: calc_datestrings()
#++
#
# Description: Calculates various date strings (past, present and future)
#              based on the current date in the format mm/dd/yyyy.
#              The calculated date strings are put into a DICT LIST, which is returned.
#
# Returns: DICT - Containing STRING representations of the various dates.
#                 To access a STRING in the DICT use any of the following keys:
#                     TODAY
#                     TOMORROW
#                     YESTERDAY
#                     DAYS_FUTURE_7
#                     DAYS_PAST_7
#                     DAYS_FUTURE_30
#                     DAYS_PAST_30
#                     DAYS_FUTURE_60
#                     DAYS_PAST_60
#                     DAYS_FUTURE_90
#                     DAYS_PAST_90
#                     DAYS_FUTURE_365
#                     DAYS_PAST_365
#                     WEEKS_FUTURE_1
#                     WEEKS_FUTURE_2
#                     WEEKS_FUTURE_4
#                     WEEKS_FUTURE_8
#                     WEEKS_FUTURE_12
#                     WEEKS_FUTURE_365
#                     WEEKS_PAST_1
#                     WEEKS_PAST_2
#                     WEEKS_PAST_4
#                     WEEKS_PAST_8
#                     WEEKS_PAST_12
#                     WEEKS_PAST_365
#
# Usage Examples:
#                aMyWorkingDates = calc_datestrings()
#                sYESTERDAY = aMyWorkingDates["YESTERDAY"]
#                s60_DAYS_PAST = aMyWorkingDates["DAYS_PAST_60"]
#
#                 or:
#
#                sYESTERDAY = calc_datestrings["YESTERDAY"]
#                s60_DAYS_PAST = calc_datestrings["DAYS_PAST_60"]
#
#=============================================================================#
def calc_datestrings():

    '''
    Calculates various date strings (past, present and future)
    based on the current date in the format mm/dd/yyyy.
    The calculated date strings are returned in a Dictionary.
    '''

    # Grab the current date time
    #tNow = Time.now
    dToday = date.today()

    # Define the time format to be used in file names: e.g. 01/02/2007
    sDateformat = "%m/%d/%Y"

    sTODAY = dToday.strftime(sDateformat)
    sTOMORROW = (dToday + (timedelta(days=1))).strftime(sDateformat)
    sYESTERDAY = (dToday - (timedelta(days=1))).strftime(sDateformat)
    sDAYS_FUTURE_7 = (dToday + (timedelta(days=7))).strftime(sDateformat)
    sDAYS_PAST_7 = (dToday - (timedelta(days=7))).strftime(sDateformat)
    sDAYS_FUTURE_30 = (dToday + (timedelta(days=30))).strftime(sDateformat)
    sDAYS_PAST_30 = (dToday - (timedelta(days=30))).strftime(sDateformat)
    sDAYS_FUTURE_60 = (dToday + (timedelta(days=60))).strftime(sDateformat)
    sDAYS_PAST_60 = (dToday - (timedelta(days=60))).strftime(sDateformat)
    sDAYS_FUTURE_90 = (dToday + (timedelta(days=90))).strftime(sDateformat)
    sDAYS_PAST_90 = (dToday - (timedelta(days=90))).strftime(sDateformat)
    sDAYS_FUTURE_365 = (dToday + (timedelta(days=365))).strftime(sDateformat)
    sDAYS_PAST_365 = (dToday - (timedelta(days=365))).strftime(sDateformat)
    WEEKS_FUTURE_1 = (dToday + (timedelta(weeks=1))).strftime(sDateformat)
    WEEKS_FUTURE_2 = (dToday + (timedelta(weeks=2))).strftime(sDateformat)
    WEEKS_FUTURE_4 = (dToday + (timedelta(weeks=4))).strftime(sDateformat)
    WEEKS_FUTURE_8 = (dToday + (timedelta(weeks=8))).strftime(sDateformat)
    WEEKS_FUTURE_12 = (dToday + (timedelta(weeks=12))).strftime(sDateformat)
    WEEKS_FUTURE_52 = (dToday + (timedelta(weeks=52))).strftime(sDateformat)
    WEEKS_PAST_1 = (dToday - (timedelta(weeks=1))).strftime(sDateformat)
    WEEKS_PAST_2 = (dToday - (timedelta(weeks=2))).strftime(sDateformat)
    WEEKS_PAST_4 = (dToday - (timedelta(weeks=4))).strftime(sDateformat)
    WEEKS_PAST_8 = (dToday - (timedelta(weeks=8))).strftime(sDateformat)
    WEEKS_PAST_12 = (dToday - (timedelta(weeks=12))).strftime(sDateformat)
    WEEKS_PAST_52 = (dToday - (timedelta(weeks=52))).strftime(sDateformat)

    hDateStringDict = {
      "TODAY" : sTODAY,
      "TOMORROW" : sTOMORROW,
      "YESTERDAY" : sYESTERDAY,
      "DAYS_FUTURE_7" : sDAYS_FUTURE_7,
      "DAYS_PAST_7" : sDAYS_PAST_7,
      "DAYS_FUTURE_30" : sDAYS_FUTURE_30,
      "DAYS_PAST_30" : sDAYS_PAST_30,
      "DAYS_FUTURE_60" : sDAYS_FUTURE_60,
      "DAYS_PAST_60" : sDAYS_PAST_60,
      "DAYS_FUTURE_90" : sDAYS_FUTURE_90,
      "DAYS_PAST_90" : sDAYS_PAST_90,
      "DAYS_FUTURE_365" : sDAYS_FUTURE_365,
      "DAYS_PAST_365" : sDAYS_PAST_365,
      "WEEKS_FUTURE_1" : WEEKS_FUTURE_1,
      "WEEKS_FUTURE_2" : WEEKS_FUTURE_2,
      "WEEKS_FUTURE_4" : WEEKS_FUTURE_4,
      "WEEKS_FUTURE_8" : WEEKS_FUTURE_8,
      "WEEKS_FUTURE_12" : WEEKS_FUTURE_12,
      "WEEKS_FUTURE_52" : WEEKS_FUTURE_52,
      "WEEKS_PAST_1" : WEEKS_PAST_1,
      "WEEKS_PAST_2" : WEEKS_PAST_2,
      "WEEKS_PAST_4" : WEEKS_PAST_4,
      "WEEKS_PAST_8" : WEEKS_PAST_8,
      "WEEKS_PAST_12" : WEEKS_PAST_12,
      "WEEKS_PAST_52" : WEEKS_PAST_52,
    }

    return hDateStringDict

# Function - calc_datestrings


#=============================================================================#
#--
# Function: calc_elapsed_time(...)
#++
#
# Description: Calculates the duration of an event based on the specified start time.
#
# Returns: STRING - Elapsed time as a string
#
# Syntax: tStartTime = TIME object - The starting time of the event to be timed
#
# Usage Example: tTestCase_StartTime = datetime.now()
#                    print2("Start time = " + str(tTestCase_StartTime))
#                    # Do some stuff, run a test,  time.sleep(2)  or whatever
#                    print2("Testcase finished in " + calc_elapsed_time(tTestCase_StartTime) + " (h:m:s.ms)")
#
#=============================================================================#
def calc_elapsed_time(tStartTime):

    '''
    Calculates the duration of an event based on the specified start time.
    Returns: STRING - Elapsed time as a string
    '''

    #VERBOSE = True

    # Get the end time for this test case
    tEndTime = datetime.now()

    # Calculate the run time
    #sElapsedTime = str((tEndTime - tStartTime).seconds)
    sElapsedTime = str((tEndTime - tStartTime))

    if(VERBOSE == True):
        print2(tEndTime - tStartTime)
    # end

    return sElapsedTime

# End Function - calc_elapsed_time(...)


#=============================================================================#
#--
# Function: capture_results(...)
#
#++
#
# Description: Creates a specified sub-directory in either the Operating systems's
#              temporary directory or the Current Working Directory in order to
#              hold the results of this test run, and start a logger,
#              which in turn opens a timestamped log file within that directory.
#
#              Any pre-existing results sub-directory is renamed by appending a time stamp
#              to the sub-directories name. Thus allowing the current test run's results to always be saved
#              to the same specified sub-directory name, without overwriting any previous results.
#
# Returns: LOGGER object
#
# Syntax: bTmpDir = BOOLEAN - true = Create the  directory "PyWorks/results/" in the Operating systems's temporary directory
#                                               false = Create the  directory "results/" in the Current Working Directory
#
#         sResultsDirName = STRING - Name of the results directory ( Default value is RESULTS_DIR)
#
#         sLogfilePrefix = STRING - Prefix of the name of the log directory.
#                                   A timestamp (e.g. "%Y_%m_%d_%H%M%S") and a ".log" suffix will be
#                                   appended to this value to make up the log files name.
#                                   (default value is "logfile")
#
#         iLogsToKeep = INTEGER -  The total number of log files that can be saved.
#                                  When the current log file reaches the maxLogSize a new file is opened.
#                                  (e.g. 10 = keep up to 10 log files)
#                                  (default value is 50)
#
#          iMaxLogSize = INTEGER - The file size in bytes for any individual log file. Once this
#                                  value is reached a new log file is opened.
#                                  (e.g. 1000000 = 1Mb)
#                                  (default value is 5000000)
#
#          sLogLevel = STRING - The message level. One of the following (Per the Ruby Core API):
#                                Messages have varying levels (info, error, etc), reflecting their varying importance.
#                                The levels, and their meanings, are:
#                                   FATAL: An unhandleable error that results in a program crash
#                                   ERROR: A handleable error condition
#                                   WARN: A warning
#                                   INFO: generic (useful) information about system operation
#                                   DEBUG: low-level information for developers
#
#                                (default value is "INFO")
#
# Calls: create_subdirectory()
#          LoggerFactory.start_default_logger()
#
#=============================================================================#
def capture_results(bTmpDir=True, sResultsDirName=RESULTS_DIR, sLogfilePrefix="logfile", iLogsToKeep=50, iMaxLogSize= 5000000, sLogLevel="INFO"):

    '''
    Creates a specified sub-directory in either the Operating systems's
    temporary directory or the Current Working Directory
    '''
    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - capture_results:")
        print2("  bTmpDir: " + str(bTmpDir))
        print2("  sResultsDirName: " + sResultsDirName)
        print2("  sLogfilePrefix: " + sLogfilePrefix)
        print2("  iLogsToKeep: " + str(iLogsToKeep))
        print2("  iMaxLogSize: " + str(iMaxLogSize))
        print2("  sLogLevel: " + sLogLevel)
    # end

    # Don't allow a blank values
    if((sResultsDirName == "") | (sResultsDirName == None)):
        sResultsDirName = "results"
    # end

    if((sLogfilePrefix == "") |  (sLogfilePrefix == None)):
        sLogfilePrefix="logfile"
    # end

    if((iLogsToKeep < 1) |  (iLogsToKeep > 1000)):
        iLogsToKeep=50
    # end

    if((iMaxLogSize < 1) |  (iMaxLogSize > 100000000)):
        iMaxLogSize=5000000
    # #end

    if((sLogLevel == "") | (sLogLevel == None)):
        sLogLevel = "INFO"
    #end

    # Presume that no global logger has been started
    #bLoggerStarted = False

    # Only one Global logger object can exist
    # If a Global Logger is NOT open proceed
    for value in get_env("PW_LOGGER_STARTED"):
        #print2(get_env("PW_LOGGER_STARTED"))
        if(value != "True"):
            bLoggerStarted = False
        else:
            bLoggerStarted = True
        # end
    # end

    if(bLoggerStarted == False):

        # Save the current working directory
        sStartingDir = os.getcwd()

        # Find the proper temporary directory for the current OS
        sTmpDirPath = find_tmp_dir()

        # Define the name of Global WatirWorks directory
        # to be created in the OS's Temporary directory to hold any test results
        global sTmpWatirWorks_Dir
        sTmpPyWorks_Dir = "PyWorks"

        # Change directories to the temporary directory for the current OS
        if(bTmpDir == True):
            os.chdir(sTmpDirPath)

            if(os.path.exists(sTmpPyWorks_Dir) == False):
                # Creates a subdirectory to hold the results
                create_subdirectory(sTmpPyWorks_Dir)
            # end

            # Change directories to the PyWorks directory within the temporary directory for the current OS
            os.chdir(sTmpPyWorks_Dir)

        #end # Change directories to the temporary directory for the current OS

        print2("\nCreating results sub-directory: " + sResultsDirName)

        # Creates a subdirectory to hold the results
        create_subdirectory(sResultsDirName)

        # Define variables for the log file
        sTimeStamp = TIMESTAMP_STRING
        #sTimeStamp = time.strftime("%Y_%m_%d_%H%M%S")

        sLogfileName = sLogfilePrefix + "_" + sTimeStamp + ".log"

        # Combine the elements of the full pathname to the log file
        sLogfilePartialPathname = os.path.join(sResultsDirName, sLogfileName)

        sFullPathToFile = os.path.join(os.getcwd(), sLogfilePartialPathname)

        # Restore the original the working directory
        if(bTmpDir == True):
            os.chdir(sStartingDir)
        # end

        print2(" Starting new logger object for Log file: " + sFullPathToFile) # Write string to stdout (console)

        # Create the LOGGER object, which in turn creates the log file
        oNewLogger = start_logger(sFullPathToFile, iMaxLogSize, iMaxLogSize, sLogLevel)

        # Set an OS variable (to use as a Global var) indicating that the logger started
        set_env("PW_LOGGER_STARTED", "True")

        if(VERBOSE == True):
            for value in get_env("PW_LOGGER_STARTED"):
                print2(get_env("PW_LOGGER_STARTED"))
                if(value == "True"):
                    bLoggerStarted = True
                # end
            # end
        # end
        return oNewLogger

    else:
        print2(" Global logger object already started.")
        return oLogger
    # end # Only one Global logger object can exist

# END Function - capture_results()


#=============================================================================#
#--
# Function: comma_delimit(...)
#++
#
# Description:  Converts Float to STRING with the thousands separators inserted.
#               User can specify the separator character. Typically a comma for US or period for European numbers.
#               Any decimal places in the original number are truncated at two places, at the penny/cent.
#
# Returns: STRING = The string representation of the number with the thousands separator inserted.
#
# Syntax: sDelimiter =  STRING - Character to use as the thousand's delimiter,
#
# Usage Examples:
#                 To delimit with a comma:
#                    comma_delimit(1234567890.0123)  #=>  "1,234,567,890.01"
#                 To delimit with a period
#                    comma_delimit(1234567890.0123, ".")  # =>  "1.234.567.890.01"
#
#=============================================================================#
def comma_delimit(self, sDelimiter = ','):

    '''
    Converts Float to STRING with the thousands separators inserted
    '''

    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - comma_delimit:")
        print2("  sDelimiter: " + sDelimiter)
    # end

    #sDecimalPoint = '.'

    # Convert float to a string. # First convert Float to Integer, then Integer to string
    sFloat = str(self)
    if (VERBOSE == True):
        print2("\tFloat as a String: '" + sFloat + "'")
    # End

    # Split the string into its INTEGER and Decimal components
    aFloatComponents = sFloat.split(".")
    sIntegerComponent = aFloatComponents[0]
    sDecimalComponent = aFloatComponents[1]

    if (VERBOSE == True):
        print2("\tInteger component = '" + sIntegerComponent + "'")
        print2("\tDecimal component = '" + sDecimalComponent + "'")
    # end

    # Reverse the Integer component
    sReversedIntegerComponent =reverse_string(sIntegerComponent)

    if (VERBOSE == True):
        print2("\tReversed Integer component = '" + sReversedIntegerComponent + "'")
    # end


    # Determine the length of the INteger component
    iLen = len(sReversedIntegerComponent)

    # Need to comma delimit when the length is greater than 3 digits
    if (iLen > 3):

        # Cast the string to a list object
        aReversed = list(sReversedIntegerComponent)

        # Insert the delimiter character every third character
        for iIndex in range(len(aReversed)):

            # Use the modulo (%) function to see if the current index cast as a float
            # is evenly divisible by three, and its not the first or last character
            #  If it passes those three checks then insert the delimiter before the
            # current character (Remember that the string is reversed at this point).
            if (((float(iIndex)%3)== 0) & (iIndex != len(aReversed)) & (iIndex != 0)):
                aReversed[iIndex] = sDelimiter + aReversed[iIndex]
            # end
        # end

        # Reassemble the list components into a string
        sReversedIntegerComponent = ''.join(aReversed)

    # end # Need to comma delimit

    # Re-Reverse the Integer component
    sIntegerComponent = reverse_string(sReversedIntegerComponent)

    if (VERBOSE == True):
        print2("\tRe-reversed Integer component = '" + sIntegerComponent + "'")
    # end


    # Re-assemble the Integer and Decimal components
    sFloat = sIntegerComponent + "." + sDecimalComponent


    return sFloat

# End Function - comma_delimit()



#=============================================================================#
#--
# Function: compare_files(...)
#++
#
# Description: Compares two ASCII Text files to see if they are identical.
#
#              If two files differ, their size or other file attributes may
#              also differ, so compare the file attributes first. If they
#              pass and both are regular files then compare their contents.
#
#              Based on code ported from the Ruby Cookbook, Section 6.10, page 209
#                 http://oreilly.com/catalog/9780596523695
#
# Returns: BOOLEAN - True if they match, otherwise False
#
# Syntax: sFile1 = STRING - Full pathname/filename of the first file to compare
#         sFile2 = STRING - Full pathname/filename of the second file to compare
#
# Example:
#                if(compare_files(sFile_1, sFile_2) == True):
#                    print2("Files match")
#                else:
#                    print2("Files DIFFER")
#                # end
#
#=============================================================================#
def compare_files(sFile1, sFile2):

    '''
    Compares two ASCII text files to see if they are identical.
    '''

    if(VERBOSE == True):
        print2("Parameters - compare_files:")
        print2("  sFile1: " + sFile1)
        print2("  sFile2: " + sFile2)
    # end

    # Start by comparing their file attributes: existence, file size, file type
    if ((os.path.exists(sFile1) != True)  | (os.path.exists(sFile2) != True)): # Fail if either file's existence does not match
        return False
    if (os.path.getsize(sFile1) != os.path.getsize(sFile2)): # Fail if they have different file sizes
        return False

    # This test is not supported in current Jython version, so its commented out
    #if((os.path.samefile(sFile1, sFile2)) == True):   # Pass if they are the same file in the same location
    #    return True


    # Their file attributes match so compare their file contents
    # Open and read the first file
    # Access the file (read-only) and populate an LIST with its contents, line by line
    fFile = open(sFile1, 'r')
    aFileOneContents = fFile.readlines()
    # Close the file
    fFile.close()



    # Open and read the second file
    # Access the file (read-only) and populate an LIST with its contents, line by line
    fFile = open(sFile2, 'r')
    aFiletTwoContents = fFile.readlines()
    # Close the file
    fFile.close()

    # Verify that the two file's contents are the same
    if (aFileOneContents == aFiletTwoContents):
        return True
    else:
        return False

# End Function - compare_files(...)


#=============================================================================#
#--
# Function: compare_strings_in_lists(...)
#++
#
# Description: Compares the String elements in one LIST with those in a second LIST
#              and returns an LIST with Integer value of the number of exact matches,
#              along with the matching strings.
#
#              If a String in one LIST matches two or more strings in the other LIST
#              both matches will be counted. Any leading or trailing whitespace is ignored.
#
# Returns: LIST - Two element LIST,
#              LIST[0] = INTEGER - Count of the matches found between the two LISTs.
#              LIST[1] = LIST  - Each matching STRING
#
# Syntax:
#         aList_1 = First LIST of strings to compare
#         aList_2 = Second LIST of strings to compare
#         bIgnoreCase = BOOLEAN - True = Ignore case, False = Case sensitive
#         bExactMatch  = BOOLEAN - True = Row contents are an exact match for string (Compare as strings)
#                                  False = Row contains the string. (Compare as Regular Expression) (Default)
#
# Usage Examples:
#
#              aFirstList = ["the", "end", "the end", "stop"]
#              aSecondList = ["The end", "end", "start", "the", "Stop"]
#
#              print2("Compare as strings")
#              aFound = compare_strings_in_lists(aFirstList, aSecondList)
#              print2(str(aFound))
#
#              print2("Compare as strings - Ignore case")
#              aFound = compare_strings_in_lists(aFirstList, aSecondList, True)
#              print2(str(aFound))
#
#              print2("Compare as Regexp - Ignore case")
#              aFound = compare_strings_in_lists(aFirstList, aSecondList, True, True)
#              print2(str(aFound))
#
#=============================================================================#
def compare_strings_in_lists(aList_1 = None, aList_2 = None, bIgnoreCase = False, bExactMatch = False):

    '''
    Compares the String elements in one LIST with those in a second LIST
    and returns an LIST with Integer value of the number of exact matches,
    along with the matching strings.
    '''

    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - compare_strings_in_lists:")
        print2("  aList_1: " + str(aList_1))
        print2("  aList_2: " + str(aList_2))
        print2("  bIgnoreCase: " + str(bIgnoreCase))
        print2("  bExactMatch: " + str(bExactMatch))

    # Clear the match counter
    iMatchesFound = 0

    # Clear the matching text
    aMatchingText = []

    # Loop through the Strings in the first LIST
    for aText_1 in aList_1:

        # Convert element in LIST to a string and remove an leading or training spaces
        sText_1 = str(aText_1).strip()

        # Case sensitive or ignore case ?
        if(bIgnoreCase == True):
            sText_1 = sText_1.upper()
        # end

        # Loop through the Strings in the second LIST
        for aText_2 in aList_2:

            # Convert element in LIST to a string and remove an leading or training spaces
            sText_2 = str(aText_2).strip()

            # Case sensitive or ignore case ?
            if(bIgnoreCase == True):
                sText_2 = sText_2.upper()
            # end

            # Perform a compare between Regular Expressions?
            if(bExactMatch == True):

                # Compare the two strings
                if((str(sText_1.strip())) == (str(sText_2.strip()))):

                    # Increment the match counter
                    iMatchesFound = iMatchesFound + 1

                    # Record the matching text
                    aMatchingText += sText_1

                # End Compare the two strings
            else: # Perform a compare between Regular Expressions?

                # Compare the two strings as Regular Expressions
                #if((re.search(r'sText_2', sText_1)) or (re.search(r'sText_1', sText_2))):
                if((re.search(sText_2, sText_1)) or (re.search(sText_1, sText_2))):

                    # Increment the match counter
                    iMatchesFound = iMatchesFound + 1

                    # Record the matching text
                    aMatchingText += ''.join(sText_1)
                    #aMatchingText += sText_1

                # End Compare the two strings

            # End Perform a compare between Regular Expressions?

        # End Loop through the strings in the second LIST

    # End Loop through the strings in the first LIST

    # Reassemble the list components into strings
    aMatchingText = ''.join(aMatchingText)

    return iMatchesFound, aMatchingText

# End Function - compare_strings_in_lists(...)


#=============================================================================#
#--
# Function: convert_date(...)
#++
#
# Description: Converts the specified date to a STRING format based upon the timespan from today.
#              For a specified DATETIME object, or a STRING representation of a date (e.g. 7/6/05)
#
#              Based upon code at:   http://snippets.dzone.com/posts/show/487
#
# Returns: STRING - The converted date based on the elapsed time from today, formatted like one of the following:
#                    'yesterday', 'today', 'tomorrow',       # If within 1 day of today
#                    '12 days ago', 'in 4 days',           # If within 60 days of today
#                    'Monday, January 5'                   # If within 180 days of today
#                    'Tuesday, December 15, 2004'          # If beyond 1080 days of today
#
# Syntax: dMyDate = DATE, or STRING - The date to be converted
#                   Dates expressed as STRINGs must be format like:   mm/dd/yy    m/d/yyyy   m/d/yy   mm/d/yyyy
#
# Usage Examples: Please refer to: PyWorks_convert_datestrings_unittest.py
#
#=============================================================================#
def convert_date(dMyDate):

    '''
    Converts the specified date to a STRING format based upon the timespan from today.
    '''

    #VERBOSE == True

    if(VERBOSE == True):
        print2("Parameters - convert_date:")
        print2("  dMyDate: " + str(dMyDate))
    # end

    # Get the current date
    dToday = date.today()
    if(VERBOSE == True):
        print2(dToday)
    # end

    try:
        # Determine if value is a String or a Date
        if(dMyDate.__class__.__name__ == "str"):
            # Convert the string to a date

            # Split the date using the separator character into
            # and LIST populated with separate MM, DD, YY string values
            aDate = dMyDate.split("/")

            # Convert the string values into integers
            iMonth = int(aDate[0])
            iDay = int(aDate[1])
            iYear = int(aDate[2])

            if(VERBOSE == True):
                print2(" Month(MM) = " + str(iMonth) + ", Day(DD) = " + str(iDay) + ", Year(YY) = " + str(iYear))
                print2("Create a date object from the YY, MM, DD values")
            # end
            # Convert 2 digit years into 4-digit years
            if(iYear <= 99):
                iYear = (2000 + iYear)
                if(VERBOSE == True):
                    print2("Adjusted 4-digit year: " + str(iYear))
                # end
            # end

            dMyDate = date.replace(dToday, iYear, iMonth, iDay)
            if(VERBOSE == True):
                print2(" New created date = " + str(dMyDate))
            # end

        # end
    except: # If its a date us it as is
        pass
    # end - Determine if value is a String or a Date


    try: # If this fails then presume an invalid date
        if(dMyDate != dToday):
            dOffset = (dMyDate - dToday)
            #print2("dOffset: " + str(dOffset))
            sDayString = prefix(str(dOffset), ",")

            sNumberOfDays = prefix(sDayString, " ")
            #print2("sNumberOfDays: " + sNumberOfDays)
            iNumberOfDays = int(sNumberOfDays)

        else:
            #print2("sNumberOfDays: 0")
            iNumberOfDays = 0
        # end


        if(iNumberOfDays >= 0 and iNumberOfDays < 1):
            return 'today'
        if iNumberOfDays >= 1 and iNumberOfDays < 2:
            return 'tomorrow'

        if iNumberOfDays >= -1 and iNumberOfDays < 0:
            return 'yesterday'

        if abs(iNumberOfDays) < 60 and iNumberOfDays > 0:
            return "in " + str(abs(iNumberOfDays)) + " days"

        if abs(iNumberOfDays) < 60 and iNumberOfDays < 0:
            return " " + str(abs(iNumberOfDays)) + " days ago"

        if abs(iNumberOfDays) < 182:
            return dMyDate.strftime('%A, %B %d')

        #  No match with any of the previous  syntax so return reformatted like - Thursday, April  1, 2010
        return dMyDate.strftime('%A, %B %d, %Y')

    except:
        return "Invalid date"

    # end

# end  Function - convert_date()


#=============================================================================#
#--
# Function: create_subdirectory(...)
#
#++
#
# Description: Creates a specified sub-directory in the Current Working Directory.
#
#              If the specified sub-directory pre-exists, that sub-directory is renamed
#              by appending a time-stamp to its name, before the new sub-directory is created.
#
#              For example the directory can then be used as a results directory
#              to hold artifacts of a test run, such as: log files, screen captures, output files, etc.
#
# Prerequisite: Since a pre-existing sub-directory will be re-named NO files within it
#               can be open or in use.
#
# Returns: BOOLEAN - True on success, otherwise False
#
# Syntax: sSubDir = STRING -  The name of the new sub-directory to be created.
#
#=============================================================================#
def create_subdirectory(sSubDir="new_directory"):

    '''
    Creates the specified sub-directory in the Current Working Directory
    '''


    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - create_subdirectory:")
        print2("  sSubDir: " + str(sSubDir))
    # end

    # Don't allow a blank values
    if((sSubDir == "") | (sSubDir == None)):
        sSubDir = "my_new_directory"
    # end

    sFullPathToFile = os.path.join(os.getcwd(), sSubDir)

    # Generate a timestamp to append to the file name
    # The timestamp of 14 characters can be appended to a file name (e.g. mylogfile_2007_Dec_30_235959.log)
    # Example: sMyPrefix = "mylogfile"
    #          sMyExtension = ".log"
    #          sMyFilename = sMyPrefix + TIMESTAMP_STRING + sMyExtension
    sTimeStamp = time.strftime("%Y_%m_%d_%H%M%S")

    if os.path.isdir(sFullPathToFile):
        print2(" Pre-existing sub-directory being renamed")

        # Rename the old directory by appending a timestamp to its name
        os.rename(sSubDir, sSubDir + "_" + sTimeStamp)

    # end

    print2(" Creating sub-directory: " + sFullPathToFile)

    # Create a new directory
    os.mkdir(sFullPathToFile)

    return True

# end Function - create_subdirectory(...)


#=============================================================================#
#--
# Function: display_java_env()
#
#++
#
# Description: Displays information about the Java environment.
#              Information on the Java version, and platform.
#
#
# HINT: Save to a log file along with the results of the test.
#
# Returns: N/A
# Syntax:  N/A
#
#=============================================================================#
def display_java_env():

    '''
    Displays information about the Java environment
    '''

    # Record the settings
    print2("")

    # Jython 2.2.1 does not include the module "platform"
    # The platform module was added in Jython 2.3.0.
    # So wrap this block of code in a try/except to trap and ignore
    # any errors if run under Jython 2.2.1
    try:
        import platform                     # Adds ability to access Java/Jython/Python info

        sValue = ["?", "?", "?", "?", "?","?"]
        sValue = platform.uname() # SUNOS etc.
        #print2 "uname = " + str(sValue)
        print2 ("Java System = " + sValue[0])       # e.g. Java
        print2 ("Node = " + sValue[1])              # e.g. CO0700GJDIMAURO
        print2 ("Java Version  = " + sValue[2])     # e.g. 1.6.0_20
        print2 ("Java Vendor = " + sValue[3])       # e.g. Java HotSpot(TM) Client VM, 16.3-b01, Sun Microsystems Inc.
        print2 ("Java  Machine = " + sValue[4])     # e.g.
        print2 ("Java  Processor = " + sValue[5])   # e.g.
        print2 ("Java Platform = " + platform.platform())      # Includes processor arch at the end
        print2 ("Compiler = " + platform.python_compiler())             # e.g. Java HotSpot(TM) Client VM (Sun Microsystems Inc.)
    except:
        pass
    # end

    print2 ("JAVA_HOME = " + str(get_env("JAVA_HOME")['JAVA_HOME']))

# end # Function display_java_env(...)


#=============================================================================#
#--
# Function: display_jython_env()
#
#++
#
# Description: Displays information about the Jython environment.
#              Information on versions.
#
# HINT: Save to a log file along with the results of the test.
#
# Returns: N/A
# Syntax: N/A
#
#
#=============================================================================#
def display_jython_env():

    '''
    Displays information about the Jython environment
    '''

    # os.version will fail on older versions of Jython 
    try:
        # Jython Version
        print2("Jython Version: " + os.version)
    except:
        pass
    
    # Jython 2.2.1 does not include the module "platform"
    # The platform module was added in Jython 2.3.0.
    # So wrap this block of code in a try/except to trap and ignore
    # any errors if run under Jython 2.2.1
    try:
        import platform                     # Adds ability to access Java/Jython/Python info

        print2 ("Jython Version: " + platform.python_version()) # 2.5.2rc3 etc.

        ''' # This block runs but doesn't return any useful data
        if(is_win() == True): # Windows specific
            sValue = platform.win32_ver()
            #print2 ("win32 win32_ver = " + str(sValue))
            print2 ("win32 Release = " + sValue[0])
            print2 ("win32 Version = " + sValue[0])
            print2 ("win32 CSD = " + sValue[0])
            print2 ("win32 PType = " + sValue[0])
        '''
        # end # Windows specific

        if(is_linux() == True): # Mac OSx specific
            sValue = platform.linux_distribution() # SUNOS etc.
            #print2 ("Linux linux_distribution = " + str(sValue))
            print2 ("Linux Distribution Name = " + sValue[0])
            print2 ("Linux Version = " + sValue[1])
            print2 ("Linux ID = " + sValue[2])
            print2 ("Linux Supported Distributions = " + str(sValue[3]))
            print2 ("Linux Full Distribution Name = " + sValue[4])
                # end
            # end # Linux specific

        if(is_osx() == True): # Mac OSx specific
            sValue = platform.mac_ver()
            #print2 ("Mac mac_ver = " + str(sValue))
            print2 ("Mac Release = " + str(sValue[0]))
            print2 ("Mac Version  = " + str(sValue[1]))
            print2 ("Mac Machine = " + sValue[2])

            # end
        # end # Mac OSx specific
    except:
        print2("Jython Version: UNKNOWN")
    # end
    
    if(get_env('JYTHON_HOME')['JYTHON_HOME'] != None):
        print2 ("JYTHON_HOME = " + get_env('JYTHON_HOME')['JYTHON_HOME'])
    else:
        print2 ("JYTHON_HOME = ")
    # end

# End Function - display_jython_env(...)



#=============================================================================#
#--
# Function: display_PyWorks_env()
#
#++
#
# Description: Displays information about the PyWorks environment.
#              Information on which modules are loaded, and their respective versions.
#
# HINT: Save to a log file along with the results of the test.
#
# Returns: N/A
# Syntax: N/A
#
#=============================================================================#
def display_PyWorks_env():

    '''
    Displays information about the PyWorks environment
    '''

    sPW_Install_Path = get_PyWorks_install_path()
    print2("\nPyWorks Install Path: " + sPW_Install_Path)


    try: # If it doesn't error its loaded, if it errors its not loaded.
        #print2("PyWorks Libraries")
        print2(" PyWorks_Reflib: " + PW_REFLIB_VERSION)
    except: # It erred, thus its NOT loaded
        print2(" PyWorks_Reflib: Not loaded")
    # end

    try: # If it doesn't error its loaded, if it errors its not loaded.
        print2(" PyWorks_Utilities: " + PW_UTILITIES_VERSION)
    except: # It erred, thus its NOT loaded
        print2(" PyWorks_Utilities: Not loaded")
    # end

    try: # If it doesn't error its loaded, if it errors its not loaded.
        print2(" PyWorks_WebUtilities: " + PW_WEB_UTILITIES_VERSION)
    except: # It erred, thus its NOT loaded
        print2(" PyWorks_WebUtilities: Not loaded")
    # end

# End Function - display_PyWorks_env(...)


#=============================================================================#
#--
# Function: find_folder_in_tree(...)
#
#++
#
# Description: Searches for the specified folder and returns the full pathname of its location in the directory tree.
#
#               1) Starts searching in the current working directory.
#               2) If still not found, recursively searches in the directories
#                  beneath the current working directory.
#
# Returns: STRING - The full pathname to the matching folder
#
# Syntax: sFolderName = STRING - The name of the folder to find (default = DATA_DIR )
#
#=============================================================================#
def find_folder_in_tree(sFolderName):

    '''
    Searches for the specified folder and returns the full pathname of its location
    '''

    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - find_folder_in_tree:")
        print2("  sFolderName: " + str(sFolderName))
    # end


    sFullPathToDir = "" # Set a default value

    # Save the current working directory
    sStartingDir = os.getcwd()

    if(VERBOSE == True):
        print2(" Starting directory: " + sStartingDir)
        print2("Recursively searching all sub-directories for folder: " + sFolderName)

    # end

    aSubDirListing = list_subdirs(sStartingDir)

    if (VERBOSE == True):
        print2("Sub-directories....")
        for sSubDir in aSubDirListing:
            print2("\t" + sSubDir)
        # end
    # end

    # Search the directory and sub-directories using the find command to collect
    # the list of directories. Need to weed out the numerous
    # pathnames that don't end with the sub-directory.
    for sSubDir in aSubDirListing:

        # Does path end with the folder matching the search criteria
        # Verify that it really ends with, not just contains the folder
        if(re.match(r'.*' + sFolderName + r'$', sSubDir)):
            sFullPathToDir = sSubDir
            break
        # end
    # end


    if(VERBOSE == True):
        print2("Full path to sub folder: " + sFullPathToDir)
    # end

    # Return the full path to the sub-directory
    return sFullPathToDir


# Function - find_folder_in_tree()



#=============================================================================#
#--
# Function: find_tmp_dir()
#
#++
#
# Description: Returns the full path of a temporary directory on the current Operating System
#            That directory should allow write permissions for the user account
#
# Returns: STRING = The full path to the temporary directory
#
# Syntax: N/A
#
# Usage Examples:
#
#                           sTempDir = find_tmp_dir()
#
#=============================================================================#
def find_tmp_dir():

    '''
    Returns the full path of a temporary directory on the current Operating System
    '''

    if is_win() == True:
        sTmp_Dir = get_env("TMP")["TMP"]
    elif(is_linux() == True):
        sTmp_Dir = "/tmp"
    elif(is_mac() == True):
        sTmp_Dir = "/tmp"
    # end
    return sTmp_Dir

# End Function - find_tmp_dir


#=============================================================================#
#--
# Function: format_dateString_mdyy(...)
#
#++
#
# Description: Converts a string representation of a date (i.e. "01/02/2007", or "12/22/2007")
#              into the form m/d/yy, (e.g. 1/2/07).
#
# Returns: sConvertedDateString = STRING
#
# Syntax: sDelimiter = STRING - The delimiter character (defaults to "/")
#
# Usage Examples: To convert the date string "08/04/2007" to "8/4/07"
#                    sMyDateString = "08/04/2007"
#                    sAdjustedDate = format_dateString_mdyy(sMyDateString, "/")
#
# Pre-requisites: Month and day must be one or two characters long
#                 Year must be two or four characters long
#
#=============================================================================#
def format_dateString_mdyy(self, sDelimiter = "/"):

    '''
    Converts a string representation of a date (i.e. "01/02/2007", or "12/22/2007")
    into the form m/d/yy, (e.g. 1/2/07).
    '''

    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - format_dateString_mdyy:")
        print2("  sDelimiter: " + sDelimiter)
    # end

    try: ### BEGIN - Convert the date string ###

        # Define empty string to return
        sConvertedDateString = ""

        if(VERBOSE == True):
            print2("Original Date string: " + str(self))
        # end

        # BEGIN - SETP 1 - Value is not a string
        if(self.__class__.__name__ == "str"):

            # Remove any Leading or Training whitespace
            self = self.strip()

            # BEGIN - STEP 2 - Split the string into separate month, day and year strings
            #
            # Split the date into Month, Day and Year strings  based on the delimiter character
            iMySeperator = self.find(sDelimiter)
            iMyEndOfLine = self.find(r'$')

            if(VERBOSE == True):
                print2("iMySeperator " + str(iMySeperator))
                print2("iMyEndOfLine " + str(iMyEndOfLine))
            # end

            sMonthToConvert = self[0: iMySeperator]
            sDayYearToConvert = self[(iMySeperator + 1): iMyEndOfLine]


            if(VERBOSE == True):
                print2(" Original Month: " + sMonthToConvert)
                #print2(" sDayYearToConvert: " + sDayYearToConvert)
            # end

            iMySeperator = sDayYearToConvert.find(sDelimiter)
            iMyEndOfLine = sDayYearToConvert.find(r'$')
            sDayToConvert = sDayYearToConvert[0: iMySeperator]
            #sYearToConvert = sDayYearToConvert[(iMySeperator + 1):]
            sYearToConvert = suffix(self, sDelimiter)

            if(VERBOSE == True):
                print2(" Original Day: " + sDayToConvert)
                print2(" Original Year: " + sYearToConvert)
            # end
            # END - STEP 2 - Split the string into separate month, day and year strings

            # BEGIN - STEP 3 - Remove leading zeros from the month
            #
            if(VERBOSE == True):
                print2(" sMonthToConvert[0]: " + sMonthToConvert[0])
            # end

            if(sMonthToConvert[0] == "0"):
                # Starting with the first character, keep one characters
                sConvertedMonth = str(sMonthToConvert[1:])
            else:
                sConvertedMonth = sMonthToConvert
            # end

            if(VERBOSE == True):
                print2(" sConvertedMonth: " + sConvertedMonth)
            # end
            # END - STEP 3 - Remove leading zeros from the month

            # BEGIN - STEP 4 - Remove leading zeros from the day
            #
            if(VERBOSE == True):
                print2(" sDayToConvert[0]: " + sDayToConvert[0])
            # end

            if(sDayToConvert[0] == "0"):
                # Starting with the first character, keep one characters
                sConvertedDay = str(sDayToConvert[1:])
            else:
                sConvertedDay = sDayToConvert
            # end

            if(VERBOSE == True):
                print2(" sConvertedDay: " + sConvertedDay)
            # end
            # END - STEP 4 - Remove leading zeros from the day

            # BEGIN - STEP 5 - Remove first two characters from a 4-character year
            #
            if(VERBOSE == True):
                print2(" len(sYearToConvert): " + str(len(sYearToConvert)))
            # end
            if len(sYearToConvert) > 2:
                # Keep the last two characters
                sConvertedYear = sYearToConvert[2:]
            else:
                sConvertedYear = sYearToConvert
            # end

            if(VERBOSE == True):
                print2(" sConvertedYear: " + sConvertedYear)
            # end
            # END - STEP 5 - Remove first two characters from a 4-character year

            # BEGIN - STEP 6 - Assemble the corrected date string
            #
            sConvertedDateString = sConvertedMonth + "/" + sConvertedDay + "/" + sConvertedYear

            if(VERBOSE == True):
                print2("New Date string: " + sConvertedDateString)
            # end
            # END - STEP 6 - Assemble the corrected date string

        else: # SETP 1 - Value is not string

            if(VERBOSE == True):
                print2("   ## sDateToConvert not a string, its a " + self.__class__.__name__)
            # end

        # END - SETP 1 - Value is not a string

    except:
        print2("*** WARNING - Converting the date string", "WARN")
        print2("*** WARNING and trace:")
        print2('-'*60)
        traceback.print_exc(file=sys.stdout)
        print2('-'*60)

        # Raise the error with a custom message after the rest of the exception actions
        raise("*** METHOD - format_dateString_mdyy(...)")

    else:

        return sConvertedDateString

    # End Convert the date string
# End Function - format_dateString_mdyy


#=============================================================================#
#--
# Function: format_dateString_mmddyyyy(...)
#
#++
#
# Description: Convert a string representation of a date (i.e. "1/2/07", or "12/22/55")
#              into the form mm/dd/yyyy, (e.g. 01/02/2007).
#
# Returns: sConvertedDateString = STRING
#
# Syntax: sDelimiter = STRING - The delimiter character (defaults to "/")
#
#         sMSB = STRING - The two Most Significant Bits of the year (e.g. "19" for 1900-1999)
#
# Usage Examples: To convert the date string "8/4/55" to "08/04/1955"
#                    sMyDateString = "8/4/55"
#                    sAdjustedDateString = format_dateString_mmddyyyy(sMyDateString, "/", "19")
#
# Pre-requisites: Month and day may only be one or two characters long
#                 Year may only be two or four characters long
#=============================================================================#
def format_dateString_mmddyyyy(self, sDelimiter = "/", sMSB = "20"):

    '''
    Convert a string representation of a date (i.e. "1/2/07", or "12/22/55")
    into the form mm/dd/yyyy, (e.g. 01/02/2007)
    '''

    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - format_dateString_mmddyyyy:")
        print2("  sDelimiter: " + sDelimiter)
        print2("  sMSB: " + sMSB)
    # end

    try: ### BEGIN - Convert the date string ###

        # Define empty string to return
        sConvertedDateString = ""

        if(VERBOSE == True):
            print2("Original Date string: " + str(self))
        # end

        # BEGIN - SETP 1 - Value is not a string
        if(self.__class__.__name__ == "str"):

            # Remove any Leading or Training whitespace
            self = self.strip()

            # BEGIN - STEP 2 - Split the string into separate month, day and year strings
            #
            # Split the date into Month, Day and Year strings  based on the Delimiter character
            iMySeperator = self.find(sDelimiter)
            iMyEndOfLine = self.find(r'$')

            sMonthToConvert = self[0: iMySeperator]
            sDayYearToConvert = self[(iMySeperator + 1): iMyEndOfLine]

            if(VERBOSE == True):
                print2(" Original Month: " + sMonthToConvert)
                print2(" sDayYearToConvert: " + sDayYearToConvert)
            # end


            iMySeperator = sDayYearToConvert.find(sDelimiter)
            iMyEndOfLine = sDayYearToConvert.find(r'$')
            sDayToConvert = sDayYearToConvert[0: iMySeperator]
            #sYearToConvert = sDayYearToConvert[(iMySeperator + 1) : iMyEndOfLine]
            sYearToConvert = suffix(self, sDelimiter)

            if(VERBOSE == True):
                print2(" Origional Day: " + sDayToConvert)
                print2(" Origional Year: " + sYearToConvert)
            # end
        # END - STEP 2 - Split the string into separate month, day and year strings

        # BEGIN - STEP 3 - Add leading zeros from the month
        #
        if(VERBOSE == True):
            print2(" len(sMonthToConvert): " + str(len(sMonthToConvert)))
        # end

        if(len(sMonthToConvert) == 1):
            # Pre-pend a zero to the day
            sConvertedMonth = "0" + sMonthToConvert
        else:
            sConvertedMonth = sMonthToConvert
        # end

        if(VERBOSE == True):
            print2(" sConvertedMonth: " + sConvertedMonth)
        # end
        # END - STEP 3 - Add leading zeros from the month

        # BEGIN - STEP 4 - Add leading zeros from the day

        if(VERBOSE == True):
            print2(" len(sDayToConvert): " + str(len(sDayToConvert)))
        # end

        if(len(sDayToConvert) == 1):
            # Pre-pend a zero to the day
            sConvertedDay = "0" + sDayToConvert
        else:
            sConvertedDay = sDayToConvert
        # end

        if(VERBOSE == True):
            print2(" sConvertedDay: " + sConvertedDay)
        # end
        # END - STEP 4 - Add leading zeros from the day

        # BEGIN - STEP 5 - Add first two characters to a 2-character year
        #
        if(VERBOSE == True):
            print2(" len(sYearToConvert): " + str(len(sYearToConvert)))
        # end
        if(len(sYearToConvert) == 2):
            # Pre-pend two characters to the year
            sConvertedYear = sMSB + sYearToConvert
        else:
            sConvertedYear = sYearToConvert
        # end

        if(VERBOSE == True):
            print2(" sConvertedYear: " + sConvertedYear)
        # end
        # END - STEP 5 - Add first two characters to a 2-character year

        # BEGIN - STEP 6 - Assemble the corrected date string
        #
        sConvertedDateString = sConvertedMonth + "/" + sConvertedDay + "/" + sConvertedYear

        if(VERBOSE == True):
            print2("New Date string: " + sConvertedDateString)
        # end
        # END - STEP 6 - Assemble the corrected date string

        else: # SETP 1 - Value is not string

            if(VERBOSE == True):
                print2("   ## sDateToConvert not a string, its a " + self.__class__.__name__)
            # end

        # End END - SETP 1 - Value is not a string


    except:

        print2("*** WARNING - Converting the date string", "WARN")
        print2("*** WARNING and trace:")
        print2('-'*60)
        traceback.print_exc(file=sys.stdout)
        print2('-'*60)
        # Raise the error with a custom message after the rest of the exception actions
        raise("*** METHOD - format_dateString_mdyy(...)")

    else:

        return sConvertedDateString

    # End Convert the date string

# End Function - format_dateString_mmddyyyy


#=============================================================================#
#--
# Function: format_from_currency(...)
#
#++
#
# Description: Converts a string representation of a currency formatted number
#              into a string representation of a number.
#              Such as converting the string "$1,000.52"  into the string "1000.52"
#              Note that strings with more than 2 decimal places are rounded off.
#
# Returns: sStringRepresentationOfNumber = STRING
#
# Syntax:
#         bStripDecimalPlaces = BOOLEAN - True = Strip string of decimal places (assumes 2 decimal places)
#                                         False = Do NOT strip
#         sDelimiter = STRING - Character used to separate the converted amount every 3 places to
#                               left of the decimal's location
#         sSymbol = STRING - Character used to identify the amount which will be truncated by the conversion process.
#                            For example: Dollars ($), Euros (E), Pounds Sterling (L), Yen (Y),
#                            or other non-multi-byte currency symbols.
#                            If set to "" no symbol is truncated
#
# Usage Examples:
#                To convert the string "E1.000.00" to "1000"
#                       format_from_currency("E1.000.00", "E", ".", True)
#
#                To convert the string "$1,000.50" to "1000"
#                       format_from_currency("$1,000.50","$", ",", True)
#
#                To convert the string "$1.000.50" to "$1000.50"
#                       format_from_currency("$1.000.50","", ".", False)
#
#=============================================================================#
def format_from_currency(self, sSymbol = "$", sDelimiter = ",", bStripDecimalPlaces = False):

    '''
    Converts a string representation of a currency formatted number (e.g. "$1,000.00"
    into a string representation of a number (e.g. "1000").
    '''

    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - format_from_currency:")
        print2("  bStripDecimalPlaces: " + str(bStripDecimalPlaces))
        print2("  sDelimiter: " + sDelimiter)
        print2("  sSymbol: " + sSymbol)
    # end


    if(VERBOSE == True):
        print2(" Amount To Convert:  " + str(self))
        print2(" Strip Decimal Places: " + str(bStripDecimalPlaces))
        print2(" Delimiter: " + str(sDelimiter))
        print2(" Symbol: " + str(sSymbol))
    # end

    # Define decimal point character
    sDecimalPoint = "."

    # Remove any leading or trailing spaces
    self.strip()

    # Determine the length of the string
    iEndOfString = len(self)

    if(VERBOSE == True):
        print2(" String length: " + str(iEndOfString))
    # end

    # Determine if the Numeric String has a decimal and where's its located
    # Count backward from the end of the string through only the last 4 character
    # which will catch formats ( *, *., *.0, *.00)
    #
    if (self[iEndOfString - 1] == sDecimalPoint):
            iSplit = iEndOfString - 1
    elif (self[iEndOfString - 2] == sDecimalPoint):
            iSplit = iEndOfString - 2
    elif (self[iEndOfString - 3] == sDecimalPoint):
            iSplit = iEndOfString - 3
    elif (self[iEndOfString - 4] == sDecimalPoint):
            iSplit = iEndOfString - 4
    else:
        iSplit = iEndOfString
    # End Determine if the Numeric String has a decimal and where's its located

    # Split string at the decimal place's location
    sPrefix = self[0: iSplit]
    sSuffix = self[(iSplit) : iEndOfString]

    if(VERBOSE == True):
        print2(" Prefix string: " + sPrefix)
        print2(" Suffix string: " + sSuffix)
    # end

    # Remove the delimiter character from the prefix
    sPrefix = sPrefix.replace(sDelimiter, "")

    if(VERBOSE == True):
        print2(" Delimited prefix string: " + sPrefix)
    # end

    # Does the first character in the string match the symbol that is to be removed?
    if(str(sSymbol) != ""):
        # Strip off the symbol character
        sPrefix = sPrefix.replace(sSymbol, "")
    # end

    # Pad the prefix as necessary
    if(sPrefix == ""):
        sPrefix = "0" + sPrefix

        if(VERBOSE == True):
            print2(" Padded prefix string: " + sPrefix)
        # end

    # End Pad the prefix as necessary

    # Pad the suffix to 2-decimal places as necessary
    if (sSuffix == "."):
        sSuffix = sSuffix + "00"
    elif (re.match(r'\.$', sSuffix)):
        sSuffix = sSuffix + "00"
    elif (re.match(r'\.\d$', sSuffix)):
        sSuffix = sSuffix + "0"
    # End Pad the suffix to 2-decimal places as necessary

    if(VERBOSE == True):
        print2(" Padded suffix string: " + sSuffix)
    # end

    # Re-attach the suffix
    if(bStripDecimalPlaces == False):
        # Create string by adding the prefix and the suffix
        sStringRepresentationOfNumber = sPrefix + sSuffix
    else:
        # Create string by adding only the prefix
        sStringRepresentationOfNumber = sPrefix
    # End Re-attach the suffix

    return sStringRepresentationOfNumber

# End Function - format_from_currency()



#=============================================================================#
#--
# Function: format_to_currency(...)
#
#++
#
# Description: Converts a string representation of a number into a string representation
#              of a currency formatted amount, with a thousands separator, and 2-decimal places.
#              Such as converting "1000000"  to "$1,000,000.00".
#              Values are padded to two decimal places as necessary.
#
# Returns: sStringRepresentationOfAmount = STRING
#
# Syntax:
#          sDelimiter = STRING - Character used to separate the converted amount every 3 places to
#                                  left of the decimal's location (the thousands separator)
#          sSymbol = STRING - Monetary symbol prepended onto the converted amount,
#                              For example: Dollars ($), Euros (E), Pounds Sterling (L), Yen (Y),
#                              or other non-multi-byte currency symbols.
#                              If set to "" no symbol is prepended.
#
# Usage Examples:
#                To convert the string "1000" to Pounds Sterling, using a period as a delimiter,
#                     format_to_currency("1000", "L", ".")  #=>  "L1.000.00"
#
#                To convert the string "1000.50" to Dollars, using a comma as a delimiter,
#                     format_to_currency("1000.50")   #=>  "$1,000.50"
#
#                To convert the string "1000.5" without a $, using a comma as a delimiter,
#                     format_to_currency("1000000.50", "", ",")   #=> "1,000,000.50"
#
#                To convert the string "1" to Euros, using a period as a delimiter,
#                     format_to_currency("1", "E", ".")  #=>  "E1.00"
#
#                To convert the string ".5" to Dollars, using a comma as a delimiter,
#                    format_to_currency(".5", "$", ",") #=> "$0.50"
#=============================================================================#
def format_to_currency(self, sSymbol = "$", sDelimiter = ","):

    '''
    Converts a string representation of a number (e.g. "1000") into a string representation
    of a currency formatted amount, with a thousands separator, and 2-decimal places ($1,000.00).
    '''

    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - format_to_currency:")
        print2("  self: " + self)
        print2("  sSymbol: " + sSymbol)
        print2("  sDelimiter: " + sDelimiter)

    # end

    # Remove any leading or trailing spaces
    sString = self.strip()

    # Determine the last character of the string
    iStringLength = len(sString)
    sLastCharacter = sString[iStringLength - 1]  # Adjust for 0 vs 1 indexed
    if (VERBOSE == True):
        print2 (" iStringLength: " + str(iStringLength))
        print2 (" sLastCharacter: " + sLastCharacter)
    # end

    # If string ends in a decimal, pad it with zeros
    if(sLastCharacter == "."):
        sString = sString + "00"
    # end

    # Convert String into a float
    #fAmount = float(sStringRepresentationOfAmount)
    fAmount = float(sString)

    fAmount = "%.2f" % fAmount

    # Add the separator character to the Float before every third digit to the left of the decimal place
    fAmount = comma_delimit(float(fAmount), sDelimiter)

    if(VERBOSE == True):
        print2(" Partly converted number: " + str(fAmount))
    # end

    # Convert the Float back into a String and prepend the Monetary symbol character
    sStringRepresentationOfAmount = sSymbol + str(fAmount)

    # Determine the length of the string
    iEndOfString = len(sStringRepresentationOfAmount) #.index(r'/ $ /') # Length of the string (count from 0)

    if(VERBOSE == True):
        print2("Length of string: " + str(iEndOfString))
    # end

    # Pad to 2-decimal places if necessary
    if(sStringRepresentationOfAmount[iEndOfString - 3] != "."):

        sStringRepresentationOfAmount = sStringRepresentationOfAmount + "0"

    # end

    return sStringRepresentationOfAmount

# End Function - format_to_currency()



#=============================================================================#
#--
# Function: get_env(...)
#++
#
# Description: Collects information of the specified O/S Environment Variables
#
#              In effect it reads all or part of the ENV object into a DICT.
#
#              The ENV object is populated with the O/S variables
#              that were set when the process that launched Java started.
#
# Note: This method may not be any more useful that accessing the O/S variable values directly
#       from the ENV object, (i.e. ENV["Path"] will return the setting of that O/S variable).
#
#       Since a printenv() method was also coded, this getenv() method is supplied
#       to complete the set.
#
# Returns: DICT - A DICT containing STRINGS of:
#                     key = O/S Environment variable name
#                     value = O/S Environment variable setting
#
# Syntax: sEnvVar = STRING - The case sensitive name of the O/S Environment variable to collect.
#                            If no variable name is specified all the variables and corresponding values are collected
#
# Usage Examples:
#                 hMyEnvVars = get_env("COMPUTERNAME")
#                 hMyEnvVars = get_env()
#=============================================================================#
def get_env(sEnvVar = None):

    '''
    Collects information of the specified O/S Environment Variables

    NOTE: Unlike calling the UNIX getenv command with no parameters,
    the os.getenv() method does not return the list of all variables.
    But this method will!
    '''

    #sValue = os.getenv(sEnvVar)


    # Get all the variables if a specific variable was NOT specified
    if(sEnvVar == None) | (sEnvVar == ""):
        #
        # Create a blank 'dict' object
        hEnvVars = {}

        # Insert each key/value pair into the dict
        for param in os.environ.keys():
            hEnvVars[param] = os.environ[param]

        if (hEnvVars.__class__.__name__ != 'dict'):
            print2(hEnvVars.__class__.__name__)
        # end

    else: # Get only the specified variable

        sValue = os.environ.get(str(sEnvVar))

        # Populate the DICT if no matching env variable was found
        if sValue.__class__.__name__ == "None":
            hEnvVars = {sEnvVar:""}
        else:
            hEnvVars = {sEnvVar:sValue}

    return hEnvVars

# End Function - get_env()


#=============================================================================#
#--
# Function: get_PyWorks_install_path()
#
#++
#
# Description: Identifies the location of the PyWorks folder
#
# HINT:  Use the path returned from this method along with the dictionary file's name
#        to access that dictionary that is supplied with PyWorks
#
# Returns: STRING - The full path name of the root PyWorks folder
#
# Syntax: N/A
#
# Usage Examples: sPath = get_PyWorks_install_path()
#
#=============================================================================#
def get_PyWorks_install_path():

    '''
    Identifies the location of the PyWorks folder
    '''
    #VERBOSE = True

    # Set default return value
    sPW_Install_Path = None

    # Get the full set of paths
    hRaw_PYTHONPATH = get_env('PYTHONPATH')
    sRaw_PYTHONPATH = hRaw_PYTHONPATH['PYTHONPATH']
    if(VERBOSE == True):
        print2(sRaw_PYTHONPATH)
    # end

    # Get the Path separator character
    if(is_win() == True):
        sPathSeperator = ";"
    else:
        sPathSeperator = ":"
    # end
    #print2 sPathSeperator

    if(sRaw_PYTHONPATH != None):
        aSplit_PYTHONPATH = sRaw_PYTHONPATH.split(sPathSeperator)
    else:

        sPyWorksInstallPath = ""

        # Determine if running from within SOATest
        if((is_SOATest() == True) & (is_win() == True)):

            sPyWorksPath = "parasoft\workspace\PyWorks"

            hRaw_PATH = get_env('USERPROFILE')
            sRaw_PATH = hRaw_PATH['USERPROFILE']

            sPyWorksInstallPath = os.path.join(sRaw_PATH, sPyWorksPath)
        # end

        return sPyWorksInstallPath
    # end
    if(VERBOSE == True):
        print2(aSplit_PYTHONPATH)
    # end

    # Loop through Jython Load path LIST
    for sPath in aSplit_PYTHONPATH:
        #print2 sPath
        if(re.search('PyWorks', sPath)):
        #if(re.search(r'/PyWorks\/src\/', sPath)):

            #print2 "FOUND IT"
            # Save the match
            sPW_Install_Path = sPath
            break
        # end

    # End Loop through path LIST

    #print2 "Found: " + sPW_Install_Path

    # Remove "/src" from the end of path to get the root PyWorks folder
    # Escape the backslash
    sPW_Install_Path = remove_suffix(sPW_Install_Path, r"\\")

    return sPW_Install_Path

# End Function - get_PyWorks_install_path()


#=============================================================================#
#--
# Function: get_text_from_file(...)
#
#++
#
# Description: Checks the specified ASCII text file to see if it contains an exact match for the specified string.
#              All lines within the specified range are searched
#
# Returns: LIST - aResults = Three dimensional LIST containing a record for each match within the specified range:
#                                   aResults[0,0] = BOOLEAN - True if match found, otherwise False
#                                   aResults[0,1] = INTEGER - Line number of the matching line
#                                   aResults[0,2] = STRING - The line of text containing the matching string
#
# Syntax: sSearchString = STRING- The text to find in the ASCII Text file
#         sFileToSearch = STRING - The full pathname to the ASCII Text file to be searched
#         iStartLine = INTEGER -  The line number from the file to start searching at (Default = First line in the file)
#                                0 = The first line in the file
#                                Negative number = Last line of file
#                                Values greater than the actual length of the file default to the last line of the file
#         iRangeOfLines = INTEGER -  The number of lines to search (default = 0, All lines in file from the iStartLine)
#                                   0 = Search the entire length of the file
#                                   Positive number = Search down from iStartLine toward the BOTTOM of the file for the specified number of lines
#                                   Negative number = Search up from iStartLine toward the TOP of the file for the specified number of lines
#                                   Absolute values greater than the length of the file default to the length of the file
#
# Usage Example: To find the string "OK" in the file MyTextFile.txt which is in the current directory:
#                   aMatched = get_text_from_file("OK", "/MyFile.txt" ,0 ,0)
#                   if(aMatched[0] == True):
#                        print2("Line: " + str(aMatched[1])
#                        print2("Text: " + aMatched[2])
#                   # end
#
#=============================================================================#
def get_text_from_file(sSearchString="", sFileToSearch="", iStartLine = 0, iRangeOfLines = 0):

    '''
    Checks the specified ASCII text file to see if it contains an exact match for the specified string
    '''

    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - get_text_from_file:")
        print2("  sSearchString: " + sSearchString)
        print2("  sFileToSearch: " + sFileToSearch)
        print2("  iStartLine: " + str(iStartLine))
        print2("  iRangeOfLines: " + str(iRangeOfLines))
        #print2("  bExactMatch: " + str(bExactMatch))
    # end


    # Disallow negative numbers for the index
    if(iStartLine < 0):
        iStartLine = 0
    # end

    # Disallow negative numbers for the index
    if(iRangeOfLines < 0):
        iRangeOfLines = 0
    # end

    # Set default values
    bFoundMatch = False
    iMatchingLineNumber = 0
    sMatchingLineText = ""
    aMatch = [bFoundMatch, iMatchingLineNumber, sMatchingLineText] # Set default search results
    aResults = [aMatch]
    # Set control parameters
    bSearchFromBottomUp = False
    aMatches = []

    # Cut and run if either parameter is blank
    if((sSearchString == "") | (sFileToSearch == "")):
        if(VERBOSE == True):
            print2("Blank Search String or File")
        # end
        return aResults
    # end

    try:

        # Perform some basic checks on the file. Any error will return the default value
        #
        if(os.path.exists(sFileToSearch) == False):
            if(VERBOSE == True):
                print2("File does not exist")
            # end
            return aResults

        else:  # It exists so perform additional test on the file

            # Verify the file is an ASCII Text file NOT a directory, characterSpecial, blockSpecial, fifo, link, socket, or unknown file type
            if(os.path.isfile(sFileToSearch) == False):
                if(VERBOSE == True):
                    print2("File is not a file")
                # end
                return aResults  # Default search results
            # end
            '''
            # TODO: Find how to check file permission in jython 2.2.1
            # Verify the file is readable  (F_OK = exists, R_OK = Readable, W_OK = Writable, X_OK = Executable)
            if(os.access(sFileToSearch, os.R_OK) == False):
                if(VERBOSE == True):
                    print2("File is not readable")
                # end
                return aResults  # Default search results
            # end
            '''

            # Verify the file is not a zero length file
            if(os.path.getsize(sFileToSearch) < 0):
                if(VERBOSE == True):
                    print2("File is of zero length")
                # end
                return aResults  # Default search results
            # end

        # end # Perform some basic checks on the file


        if(VERBOSE == True):
            print2("Opening File read-only: " + sFileToSearch)
        #end

        # Open the file
        oFileObject = open(sFileToSearch, 'r')

        # Read the lines of the file into an LIST
        aFileContents = oFileObject.readlines()

        # Close the file
        oFileObject.close()

        if(VERBOSE == True):
            print2("Closing file")
        # end

        # Determine direction of search
        if(iRangeOfLines < 0):
            bSearchFromBottomUp = True
            if(VERBOSE == True):
                print2(" Search File from Bottom to Top: " + str(bSearchFromBottomUp))
            #end
        #end

        # Get the number of lines in the file
        iNumberOfLinesInFile = len(aFileContents)
        if(VERBOSE == True):
            print2(" File contains " + str(iNumberOfLinesInFile) + " lines")
        #end


        # Default adjustment for line number (one indexed) to loop counter (zero indexed)
        iStart = iStartLine -1

        # Adjust the start line  (0, line-1, or last_line-1)
        if (iStartLine < 0):
            iStart = (iNumberOfLinesInFile - 1)
            if(VERBOSE == True):
                print2("Adjust Negative Start Line")
            # end
        # end

        if (iStartLine == 0):
            iStart = iStartLine
            if(VERBOSE == True):
                print2("Adjust Zero Start Line")
            # end
        # end

        if (iStartLine > iNumberOfLinesInFile):
            iStart = (iNumberOfLinesInFile - 1)
            if(VERBOSE == True):
                print2("Adjust Out-Of-Range Start Line")
            # end
        # end

        if(VERBOSE == True):
            print2("Adjusted Start line: " + str(iStart))
        # end


        # Adjust the range value is within the actual number of lines in the file
        if((abs(iRangeOfLines) > iNumberOfLinesInFile) | (iRangeOfLines == 0)):
            iRangeOfLines = iNumberOfLinesInFile

            if(VERBOSE == True):
                print2("Adjusted range: " + str(iRangeOfLines))
            # end

        # end


        # Determine end line based on search direction
        if(bSearchFromBottomUp == False):

            # Start values (0, line-1, or last_line-1)
            if(iStart + iRangeOfLines >= iNumberOfLinesInFile):
                iEnd = iNumberOfLinesInFile -1
            else:
                iEnd = iStart + iRangeOfLines -1
            # end

            if(VERBOSE == True):
                print2("Calculated end line: " + str(iEnd))
            # end


            if(VERBOSE == True):
                print2(" Search from line " + str(iStart) + " to line " + str(iEnd))
            # end

            #=============================================================
        else: # Search from the Bottom UP

            iEnd = 0

            if(iStart  - abs(iRangeOfLines) <= 0):

                iEnd = 0

                if(VERBOSE == True):
                    print2("Adjusted end line to 0")
                # end
            # end

            if(abs(iRangeOfLines) <= iStart ):
                iEnd =  iStart + iRangeOfLines +1
                if(VERBOSE == True):
                    print2("Adjusted end line  ***")
                # end

            # end

            if(VERBOSE == True):
                print2("Calculated end line: " + str(iEnd))
            # end

            if(VERBOSE == True):
                print2(" Search from line " + str(iStart) + " to line " + str(iEnd))
            # end

        # end # Determine end line based on search direction


        # Loop through the file contents LIST to find a match
        while iStart <= iRangeOfLines:

            if(VERBOSE == True):
                print2(" Searching Line Number: " + str(iStart))
            # end

            sCurrentLineContents = aFileContents[iStart].strip()

            if(VERBOSE == True):
                print2("Current Line Contents: '" + sCurrentLineContents + "'")
            # end

            # Record info if a match is found
            if(sSearchString in sCurrentLineContents):
            #if(sCurrentLineContents == sSearchString):
            #if(re.search(sCurrentLineContents, sSearchString) == True):

                # Record line number
                #iLineNumberWithMatch = aFileContents.lineno

                # Record text in the  line

                if (VERBOSE == True):
                    print2("Found matching text: '" + sCurrentLineContents + "' on line " + str(iStart))
                # end

                # Add the current line number and line contents to the LIST
                aMatches =  aMatches + [True, iStart, sCurrentLineContents]

            # end

            # Which way to count?
            if(bSearchFromBottomUp == False):

                # increment line
                iStart = iStart +1

                if(iStart > iEnd):
                    break
                # end

            else:

                # decrement line
                iStart = iStart -1

                if(iStart < iEnd):
                    break
                # end

            # end # Which way to count?

        # end # Loop through the file contents LIST to find a match
        #
    except:
        print2("*** WARNING and trace:")
        print2('-'*60)
        traceback.print_exc(file=sys.stdout)
        print2('-'*60)

        # Close the file if it is open
        if(oFileObject != None):
            oFileObject.close()
        # end

        return aResults # Default search results

    # end

    if(VERBOSE == True):
        print2(str(aMatches))
    # end
    # If the LIST is still blank, pad it with a default set of values to indicate no match was found
    if (aMatches == []):
        aMatches = [False, 0,""]
    # end

    return aMatches # Completed search results

# end # Function - get_text_from_file()



#=============================================================================#
#--
# Function: getMatchingKeyValue()
#
#++
#
# Description: Checks the specified DICT for the first Key matching the one specified, and returns the matching Key and it's Value.
#              Note in Jython2.2.1 sorting of DICT's is not supported, so the order of the Keys in the DICT will NOT be alphabetical
#
# Returns: LIST    - LIST[0] = STRING - The matching Key
#                    LIST[1] = STRING - The matching Key's Value
#
# Syntax: hDictToSearch = DICT - The DIctionary of STRING to search
#         sKeyToMatch = STRING - The Key name to search for (May be a partial match)
#         bCaseSensitive = BOLEAN - True to perform a case sensitive search for the Key, False to ignore case
#
# Usage examples: Please see the unit tests in: PyWorks_dict_unititest.py
#
#=============================================================================#
def getMatchingKeyValue(hDictToSearch, sKeyToMatch, bCaseSensitive=False):
    '''
    Checks the specified DICT for the first Key matching the one specified, and returns the matching Key and it's Value.
    Note in Jython2.2.1 sorting of DICT's is not supported, so the order of the Keys in the DICT will NOT be alphabetical
    '''
    
    #VERBOSE = True
    
    if(VERBOSE == True):
        print2("Parameters - getMatchingKeyValue:")
        print2("  hDictToSearch: " + str(hDictToSearch))
        print2("  sKeyToMatch: " + sKeyToMatch)
        print2("  bCaseSensitive: " + str(bCaseSensitive))
    # end
    
    # Set default values
    aFound = ["", ""]
    
    
    # Loop through the DICT
    for key, value in hDictToSearch.iteritems():
        
        if (bCaseSensitive == True):
            
            if(VERBOSE == True):
                print2("Case sensitive search of key: " + key)
            # end
            
            # Does current Key match the one specified
            if (re.search(sKeyToMatch, key)):
                
                # Update the values to return
                aFound = [key, value]
            # end
            
        else:
            
            if(VERBOSE == True):
                print2("Case insensitive search of key: " + key.upper())
            # end
            
            # Does current Uppercase Key match the one specified
            if (re.search(sKeyToMatch.upper(), key.upper())):
                
                # Update the values to return
                aFound = [key, value]
            # end
            
            
        # end 
    # end
    if(VERBOSE == True):
        print2(aFound)
    # end
    
    return aFound

# End - Function getMatchingKeyValue


#=============================================================================#
# Function: invertDict()
#
# Description: Returns a dictionary with the vale:key pairs switched, so that
#              what were the keys are now the values, and what were the values
#              are now the keys.
#
# Returns: dict - With Key:value pairs inverted
#
# Syntax: dDict_orig - dict - The Dictionary to be inverted
#
# Usage examples: CANADIAN_PROVINCES["MB"]#=>  "Manitoba"
#                 CANADIAN_PROVINCE_ABBREVIATION = invertDict(CANADIAN_PROVINCES)
#                 CANADIAN_PROVINCE_ABBREVIATION["Alberta"]#=>  "AB"
#=============================================================================#
def invertDict(dDict_orig):
    '''
    Returns a dictionary with the value:key pairs switched
    '''

    dFlipped_dict = {}  # Define a new dictionary

    for key, value in dDict_orig.iteritems():
        dFlipped_dict[value] = key
    # End

    return dFlipped_dict

# End Function - invertDict()


#=============================================================================#
#--
# Function: is_blank()
#++
#
# Description: Determines if the specified string contains only whitespace
#
# Returns: BOOLEAN - True if string is all white space., otherwise False
#
# Syntax: N/A
#
# Usage Examples:
#                 print2(is_blank("    "))  #=>  True
#                 print2(is_blank(""))      #=>  False
#                 print2(is_blank("A"))     #=>  False
#
#=============================================================================#
def is_blank(self):

    '''
    Determines if the specified string contains only whitespace
    '''

    if (re.search(r'\S', self)):
        return True
    else:
        return False

# End Function - is_blank

#=============================================================================#
#--
# Function: is_linux()
#
# TODO: Determine how to identify other Linux platforms i.e. OpenSolaris
#
#++
#
# Description: Identifies if running on a Linux platform
#
# Returns: BOOLEAN - True if platform is Linux, otherwise False
#
# Syntax: N/A
#
# Usage Examples:  if(is_linux() == True)
#                      # Execute your Linux specific code
#                  # end
#
#=============================================================================#
def is_linux():

    '''
    Identifies if running on a Linux platform
    '''

    # Get the value of the OS Variable
    #sOS_Value_Debain = os.getenv("OS")

    # Get the value of the OS Variable
    #sOS_Value_Linux_Gnu = os.getenv("OSTYPE")
    sOS_Value_Linux_Gnu = os.getenv("SHELL")


    #if ((sOS_Value_Linux_Gnu == "linux-gnu")):
    if ((sOS_Value_Linux_Gnu == "/bin/bash") & (is_osx() == False)):
        return True
    else:
        return False
# end  Function - is_linux)


#=============================================================================#
#--
# Function: is_osx()
#
#++
#
# Description: Identifies if running on a OS/X platform
#
# Returns: BOOLEAN - True if platform is OS/X, otherwise False
#
# Syntax: N/A
#
# Usage Examples:  if(is_osx() == True)
#                      # Execute your OS/X specific code
#                  # end
#
#=============================================================================#
def is_osx():

    '''
    Identifies if running on a OS/X platform
    '''

    # Get the value of the OS Variable
    #sOS_Value = os.getenv("OSTYPE")
    sOS_Value = os.getenv("PYTHONIOENCODING")

    #if (sOS_Value == "darwin10.0" ):
    if (sOS_Value == "MacRoman" ):
        return True
    else:
        return False
# end # Function - is_osx()

is_mac = is_osx


#=============================================================================#
#--
# Function: is_SOATest()
#
#++
#
# Description: Identifies if running from within SOATest
#
# Returns: BOOLEAN - True if running from within SOAtest, otherwise False
#
# Syntax: N/A
#
# Usage Examples:  if(is_SOATest() == True)
#                      # Execute your OS/X specific code
#                  # end
#
#=============================================================================#
def is_SOATest():

    '''
    Identifies if running from within SOAtest
    '''

    # Attempt to import a SOATest module from within a try/except to catch any error.
    # If it errors then not running from within SOATest
    # If it doesn't error the it is running from within SOATest.
    try:
        from com.parasoft.api import Application

    except:
        return False
    else:
        return True
    # end

# end # Function - is_SOATest()


#=============================================================================#
#--
# Function: isValid_EmailAddress()
#++
#
# Description: Checks the specified string against Email Address rules defined herein.
#
#              If the string is None the validation is skipped. Please check this condition outside
#              of this function, as your application may not require an email address, but needs
#              to validate it only if one exists.
#
#              Email Address rules are:
#                 1. It is a STRING
#                 2. String's syntax is valid  (e.g. <account>@<local-domain>.<top-level-domain>)
#                 3. String is at least 6 characters long
#                 4. String contains a valid Top Level Domain
#                 5. String contains only valid characters:  A-Z  a-z  0-9  .  +  -  _
#
# Returns: BOOLEAN - True if all verifications pass, otherwise False
#
# Syntax: N/A
#
# Usage Examples: sMyString = "qa@test.com"
#                 assert(isValid_EmailAddress(sMyString))
#
# Limitations: Does not check the following:
#                     1. IP Address instead of <local-domain>.<top-level-domain> :
#                             me@[192.168.1.1]
#
#                     2. Account is specified by an Alias which is between double quotes " thus allowing otherwise invalid characters:
#                            "J. P.'s-Big Boy, The Best Burger in Town!"@server.com
#
#                     3. Local domain name may not begin with a number:
#                           elvis.presley@123.com            # Sorry but Elvis has left the building
#
#                     4. Email account, or local-domain exist and is currently active:
#                           queen-of-england@whitehouse.gov
#
#                    5. The validation is skipped if email address is None
#=============================================================================#
def isValid_EmailAddress(self):

    '''
    Checks the specified string against Email Address rules defined herein
    '''

    #VERBOSE = True

    #Set flag to True by default, if any check fails it will be set to False
    # Innocent until proven guilty
    bValidEmailAddress = True

    try: ### BEGIN - Check the Email Address  ###


        # BEGIN - SETP 1 - Value is not a string
        if(self.__class__.__name__ == "str"):

            if(VERBOSE == True):
                print2("  Checking Email Address: " + str(self))
            # end

            # Upcase the Email address as by definition they should be case insensitive
            self = self.upper()

            # BEGIN - STEP 2 - Top Level domain  (e.g. com, org, gov, etc.)

            # Separate the TLD from the address.
            #  The TLD is always the characters following the last period to the end of the string
            #
            # Flip the string so that the TLD is at the beginning of the strings
            sTLD2Check = suffix(self, ".")

            # Check the validity of the TLD
            bValidEmailAddress = isValid_TopLevelDomain(sTLD2Check)

            if((bValidEmailAddress == False) & (VERBOSE == True)):
                print2("   ## Invalid Email Address Top Level domain " + str(self))
            # end

            ## End Check validity

            # END OF - STEP 2 - Top Level domain is valid

            # BEGIN - STEP 3 - String length

            # The account, and local-domain could conceivable be only 1 character
            # The global-domain must be at least 2 characters
            #  Add the @ and a period and it all adds up to 6 characters
            #  For example:  a@b.de
            #
            if (len(self) <= 5):

                bValidEmailAddress = False

                if(VERBOSE == True):
                    print2("   ## Email Address must be at least 6 characters, only counted " + str(len(self)))
                # end

            # END - STEP 3 - String length

            # BEGIN - STEP 4 - Syntax is valid  (e.g. <account>@<local-domain>.<top-level-domain>)

            #
            # Note that x@localhost will fail as its missing a period separating the <local-domain> and <top-level-domain>
            #

            # Define set of valid characters. The + after the square bracket means multiples occurrences are OK
            # Need to check if other characters are valid (e.g. double quote "  bang !  etc.)
            # The shortest TLD is 2 characters in length
            # The longest TLD is 6 charactere in length
            if (re.search(r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}$', self) == None):

                bValidEmailAddress = False

                if(VERBOSE == True):
                    print2("   ## Invalid Email Address syntax " + str(self))
                # end

            # END - STEP 4 - Syntax is valid




        else: # SETP 1 - Value is not string

            bValidEmailAddress = False

            if(VERBOSE == True):
                print2("   ## Email Address not a string, its a " + self.__class__.__name__)
            # end

        # End END - SETP 1 - Value is not a string

    except:
        print2("*** WARNING - Checking Email Address Top Level domain", "WARNING")
        print2("*** WARNING and trace:")
        print2('-'*60)
        traceback.print_exc(file=sys.stdout)
        print2('-'*60)
    else:

        return bValidEmailAddress

### END - Check the Email Address  ###

# End Function - isValid_EmailAddress



#=============================================================================#
#--
# Function: isValid_Password()
#
#++
#
# Description: Checks the specified STRING against the Password rules as defined herein.
#
#              If the string is None the validation is skipped. Please check this condition outside
#              of this function, as your application may not require a password, but needs
#              to validate it only if one exists.
#
#              Password rules are:
#                 1. It is a STRING
#                 2. String is at least 8 characters long
#                 3. String contains at least 1 alpha character
#                 4. String contains at least 1 uppercase alpha character
#                 5. String contains at least 1 lowercase alpha character
#                 6. String contains at least 1 non-alpha character
#                 7. String DOES NOT contain a whitespace character
#                 8. String DOES NOT contain an invalid character (? @ &)
#
# Returns: BOOLEAN - True if all verifications pass, otherwise False
#
# Syntax: N/A
#
# Usage examples: sMyString = "MyPa55w0rd"
#                 assert(isValid_Password(sMyString))
#
#=============================================================================#
def isValid_Password(self):

    '''
    Checks the specified STRING against the Password rules as defined herein
    '''

    #VERBOSE = True

    #Set flag to True by default, if any check fails it will be set to False
    # Innocent until proven guilty
    bValidPassword = True

    if(VERBOSE == True):
        print2("Parameters - isValid_Password:")
        print2("  self: " + str(self))
    # End

    try: ### BEGIN - Check the password  ###

        # BEGIN - SETP 1 - Value is not a string
        if(self.__class__.__name__ == "str"):

            # BEGIN - STEP 2 - String is at least 8 characters long
            if(len(self) <= 7):

                bValidPassword = False

                if(VERBOSE == True):
                    print2("   ## Password has less than 8 characters, only counted " + str(len(self)))
                # end

            # END - STEP 2 - String is at least 8 characters long

            ''' # BEGIN - STEP 3 - String contains at least 1 alpha character
            if ((re.search(r'([a-z] | [A-Z].?)',self)) != True):

                bValidPassword = False

                if(VERBOSE == True):
                    print2("   ## Password has less than 1 alpha character")
                # end

            # END - STEP 3 - String contains at least 1 alpha character
            '''

            # BEGIN - STEP 4 - String contains at least 1 uppercase alpha character
            if ((re.search(r'[A-Z]', self)) == None):

                bValidPassword = False

                if(VERBOSE == True):
                    print2("   ## Password has less than 1 uppercase alpha character")
                # end

            # END - STEP 4 - String contains at least 1 uppercase alpha character

            # BEGIN - STEP 5 - String contains at least 1 lowercase alpha character
            if ((re.search(r'[a-z]',self)) == None):

                bValidPassword = False

                if(VERBOSE == True):
                    print2("   ## Password has less than 1 lowercase alpha character")
                # end

            # END - STEP 5 - String contains at least 1 lowercase alpha character

            # BEGIN - STEP 6 - String contains at least 1 non-alpha character
            if ((re.search(r'[0-9\!\$\#\%\.]', self)) == None):

                bValidPassword = False

                if(VERBOSE == True):
                    print2("   ## Password has less than 1 non-alpha character")
                # end

            # END - STEP 6 - String contains at least 1 non-alpha character

            # BEGIN - STEP 7 - String contains a whitespace character
            if ((re.search(r'\s', self)) != None):

                bValidPassword = False

                if(VERBOSE == True):
                    print2("   ## Password contains a whitespace character")
                # end

            # END - STEP 7 - String contains a whitespace character

            # BEGIN - STEP 8 - String contains at least invalid character
            # NEED to find a complete list of what are considered invalid characters
            if ((re.search(r'[\?\@\&].?', self)) != None):

                bValidPassword = False

                if(VERBOSE == True):
                    print2("   ## Password contains an invalid character @ & ?")
                # end

            # END - STEP 8 - String contains at least 1 invalid character

        else: # SETP 1 - Value is not string

            bValidPassword = False

            if(VERBOSE == True):
                print2("   ## Password not a string, its a " + self.__class__.__name__)
            # end

        # End END - SETP 1 - Value is not a string


    except:
        pass

        print2("*** WARNING - Checking Password", "WARN")
        print2("*** WARNING and trace:")
        print2('-'*60)
        traceback.print_exc(file=sys.stdout)
        print2('-'*60)


    else:

        return bValidPassword

    # end ### END - Check the password  ###

# End Function - isValid_Password



#=============================================================================#
#--
# Function: isValid_TopLevelDomain()
#++
#
# Description: Checks the specified string against the list of valid Top Level Domain abbreviations.
#
#
# Returns: BOOLEAN - True if all verifications pass, otherwise False
#
# Syntax: N/A
#
# Usage Examples:  sMyString = "com"
#                  assert(isValid_TopLevelDomain(sMyString))
#
#=============================================================================#
def isValid_TopLevelDomain(self):

    '''
    Checks the specified string against the list of valid Top Level Domain abbreviations
    '''

    from PyWorks_Reflib import TOP_LEVEL_DOMAINS

    try: ### BEGIN - Check the TLD  ###

        #Set flag to False by default, if a match is found it will be set to True
        # Innocent until proven guilty
        bValidDomain = False

        # BEGIN - SETP 1 - Value is not a string
        if(self.__class__.__name__ == "str"):

            # BEGIN - STEP 2 - Top Level domain  (e.g. com, org, gov, etc.)

            #
            # Set of Top Level domain names was found at: http://www.icann.org/registries/top-level-domains.htm
            #
            aTopLevelDomains = TOP_LEVEL_DOMAINS # Constant LIST defined in PyWorks_Reflib

            # Loop
            for sTLD in aTopLevelDomains:
                if(self.upper() == sTLD.upper()):

                    bValidDomain = True
                # end
            # End Loop

            if((bValidDomain == False) & (VERBOSE == True)):
                print2("   ## Invalid Top Level domain: " + str(self))
            # end

            ## END - STEP 2 - Top Level domain is valid

        else: # SETP 1 - Value is not string

            bValidDomain = False

            if(VERBOSE == True):
                print2("   ## Value is not a string, its a " + self.__class__.__name__)
            # end

        # End END - SETP 1 - Value is not a string

    except:
        print2("*** WARNING -  Top Level domain: ", "WARN")
        print2("*** WARNING and trace:")
        print2('-'*60)
        traceback.print_exc(file=sys.stdout)
        print2('-'*60)

    else:

        return bValidDomain

    # ### END - Check the TLD  ###

# End Function - isValid_TopLevelDomain


#=============================================================================#
#--
# Function: isValid_ZipCode()
#
#++
#
# Description: Checks the specified STRING against Zip Code rules defined herein
#              Covers both Zip and Zip+4 syntax.
#
#              If the string is None the validation is skipped. Please check this condition outside
#              of this function, as your application may not require a Zip Code, but needs
#              to validate it only if one exists.
#
#              Zip Code rules are:
#                 1. It is a STRING
#                 2. String's syntax is:  <5 digits>  or  <5-digits>-<4-digits>
#
# Returns: BOOLEAN - True if all verifications pass, otherwise False
#
# Syntax: N/A
#
# Usage examples: sMyString = "80303-4000"
#                 assert(isValid_ZipCode(sMyString))
#
# Limitations: Does not check the following:
#                 1. The Zip Code is listed by the US Postal Service as currently supported
#                 2. Does not lie outside of the range of valid numbers
#
#=============================================================================#
def isValid_ZipCode(self):

    '''
    Checks the specified STRING against Zip Code rules defined herein
    Covers both Zip and Zip+4 syntax
    '''

    try: ### BEGIN - Check the Zip Code  ###

        #Set flag to True by default, if any check fails it will be set to False
        # Innocent until proven guilty
        bValidZipCode = True

        # Skip check if value is None
        if ((self != None) & (self != "None")):

            # BEGIN - SETP 1 - Value is not a string
            if(self.__class__.__name__ == "str"):

                # BEGIN - STEP 2a - Syntax of <5 digits> or <5-digits>-<4-digits>
                #if (self != r'/ (^ \d{5}$) | (^ \d{5} - \d{4}$) /'):
                if (((re.search(r'^\d{5}$', self)) == None) and (re.search(r'^\d{5}-\d{4}$', self)) == None):

                    bValidZipCode = False

                    if(VERBOSE == True):
                        print2("   ## Invalid Zip Code syntax " + str(self))
                    # end



            else: # SETP 1 - Value is not string

                bValidZipCode = False

                if(VERBOSE == True):
                    print2("   ## Zip Code not a string, its a " + self.__class__.__name__)
                # end

            # End END - SETP 1 - Value is not a string
        # End Skip check if value is None

    except:
        print2("*** WARNING - Checking Zip Code", "WARN")
        print2("*** WARNING and trace:")
        print2('-'*60)
        traceback.print_exc(file=sys.stdout)
        print2('-'*60)

    else:

        return bValidZipCode

    # ### END - Check the Zip Code  ###

# End Function - isValid_ZipCode


#=============================================================================#
#--
# Function: is_win()
#
#++
#
# Description: Identifies if running on a Windows platform
#
# Returns: BOOLEAN - True if platform is Windows, otherwise False
#
# Syntax: N/A
#
# Usage Examples:  if(is_win() == True)
#                      # Execute your Windows specific code
#                  # end
#
#=============================================================================#
def is_win():

    '''
    Identifies if running on a Windows platform
    '''

    # Get the value of the OS Variable
    sOS_Value = os.getenv("OS")

    if sOS_Value == "Windows_NT":
        return True
    else:
        return False
# Function - is_win()


#=============================================================================#
#--
# Function: is_win32()
#
#++
#
# Description: Identifies if running on a Windows 32 bit platform
#
# Returns: BOOLEAN - True if platform is Windows 32 bit, otherwise False
#
# Syntax: N/A
#
# Usage Examples:  if(is_win32() == True)
#                      # Execute your Windows 32-bit specific code
#                  # end
#
#=============================================================================#
def is_win32():

    '''
    Identifies if running on a Windows 32 bit platform
    '''

    # Get the value of the OS Variable
    sOS_EnvValue = os.getenv("PROCESSOR_ARCHITECTURE")

    if ((is_win() == True) & (sOS_EnvValue == "x86") & (is_win64() == False)):
        return True
    else:
        return False
# Function - is_win32


#=============================================================================#
#--
# Function: is_win64()
#
#++
#
# Description: Identifies if running on a Windows 64 bit platform
#
# Returns: BOOLEAN - True if platform is Windows 64 bit, otherwise False
#
# Syntax: N/A
#
# Usage Examples:  if(is_win64() == True)
#                      # Execute your Windows 64-bit specific code
#                  # end
#
#=============================================================================#
def is_win64():

    '''
    Identifies if running on a Windows 64 bit platform
    '''

    # Get the value of the OS Variable
    sOS_EnvValue = os.getenv("PROCESSOR_ARCHITEW6432")

    if ((is_win() == True) & (sOS_EnvValue == "AMD64")):
        return True
    else:
        return False
# Function - is_win64


#=============================================================================#
#--
# Function: list_subdirs(...)
#++
#
# Description: Returns a alpha sorted recursively directory listing of a filesystem search
#
#
# Returns: LIST = An LIST of STRINGS - Each item in the LIST is a fullpathname to a sub-directory
#
# Syntax: sStartingDir = STRING - The fullpath to use as the root directory of the search
#
# Pre-requisites:
#                 import os
#
# Usage Examples: To get a recursive listing of the sub-directories in the path C:\My_Path\subpath\folder:
#
#                    sRootDir =  "C:\My_Path\subpath\folder"
#                    aListing = list_subdirs(sRootDir)
#                    for sPath in aListing:
#                        print2(sPath)
#                    # end
#
#                 To get a list of files matching a specific search criteria:
#
#                    sRootDir = os.getcwd()
#                    sFileToFind = "*.py"        # The search criteria (i.e. *.txt, My*.csv, etc.)
#                    hMatchingFiles = []
#                    aListing = list_subdirs(sRootDir)
#                    for sPath in aListing:
#                        hPossibleMatchingFiles = (glob.glob(os.path.join(sPath, sFileToFind)))
#                        if hPossibleMatchingFiles != []:
#                            hMatchingFiles = hMatchingFiles + hPossibleMatchingFiles
#                        #end
#                    #end
#                    print2("Found matching files: ...")
#                    for sFile in hMatchingFiles:
#                        print2( "\t" + sFile)
#                    # end
#=============================================================================#
def list_subdirs(sStartingDir):
    '''
    Recursively descend the directory rooted at sStartingDir,
    appending each sub-folder to the LIST
    '''

    aFileList = []

    #aPathsToSearch = os.listdir(sStartingDir)
    aPathsToSearch = subdirs(sStartingDir)

    # Look through all the files/directories in the specified Starting directory
    for sPath in aPathsToSearch:
        sPathname = os.path.join(sStartingDir, sPath)

        #print2(sPathname)
        aFileList.append(sPathname)
        # Its a directory so recursively call this function again
        # Until all the sub-directories are searched
        for sNewFile in list_subdirs(sPathname):
            aFileList.append(sNewFile)

        # end
    # end


    return aFileList
# end list_subdirs()

#=============================================================================#
#--
# Function: list_tree(...)
#++
#
# Description: Returns a alpha sorted recursively listing of a filesystem search
#
#
# Returns: LIST = An LIST of STRINGS - Each item in the LIST is a fullpathname to a file
#
# Syntax: sStartingDir = STRING - The fullpath to use as the root directory of the search
#
# Pre-requisites:
#                 import os
#
# Usage Examples: To get a recursive listing of the sub-directories in the path C:\My_Path\subpath\folder:
#
#                    sRootDir =  "C:\My_Path\subpath\folder"
#                    aListing = list_tree(sRootDir)
#                    for sPath in aListing:
#                        print2(sPath)
#                    # end
#
#                 To get a list of files matching a specific search criteria:
#
#                    sRootDir = os.getcwd()
#                    sFileToFind = "*.py"        # The search criteria (i.e. *.txt, My*.csv, etc.)
#                    hMatchingFiles = []
#                    aListing = list_tree(sRootDir)
#                    for sPath in aListing:
#                        hPossibleMatchingFiles = (glob.glob(os.path.join(sPath, sFileToFind)))
#                        if hPossibleMatchingFiles != []:
#                            hMatchingFiles = hMatchingFiles + hPossibleMatchingFiles
#                        #end
#                    #end
#                    print2("Found matching files: ...")
#                    for sFile in hMatchingFiles:
#                        print2( "\t" + sFile)
#                    # end
#=============================================================================#
def list_tree(sStartingDir):

    '''
    Recursively descend the directory rooted at sStartingDir,
    appending each regular file to the LIST that is returned
    '''

    aFileList = []

    aPathsToSearch = os.listdir(sStartingDir)

    # Look through all the files/directories in the specified Starting directory
    for sPath in aPathsToSearch:
        sPathname = os.path.join(sStartingDir, sPath)
        #sPathname = '%s\%s' % (sStartingDir, sPath)

        # Determine if the current pathname is a file or directory
        if os.path.isdir(sPathname):

            # Its a directory so recursively call this function again
            # Until all the sub-directories are searched
            for sNewFile in list_tree(sPathname):
                aFileList.append(sNewFile)
            # end
            #aPathsToSearch.append(sPathname)
        else:
            # Found a file, append it to the list
            aFileList.append(sPathname)
        # end
    # end

    return list(aFileList)
# END Function list_tree()


#=============================================================================#
#--
# Function: ordinal
#++
#
# Description: Converts Integer to String with the appropriate English ordinal appended.
#              i.e. 1st, 2nd, 3rd, 4th, 125th etc.
#
#              From: http://snippets.dzone.com/tag/ruby/
#
# Usage Examples:
#                 1) ordinal(int(21)) #=> "21st"
#
#                 2) [1, 22, 123, 10, -3.1415].collect { |i| i.ordinal }
#                     => ["1st", "22nd", "123rd", "10th", "3rd"]
#
#                      # Print each Ordinal from iMin to iMax
#                      iMin = 1
#                      iMax = 120
#                      iMin.upto(iMax) { | iInteger |  print2(str(iInteger) + " " + ordinal(int(iInteger))) }
#
#=============================================================================#
def ordinal(self):

    '''
    Converts Integer to String with the appropriate English ordinal appended.
    i.e. 1st, 2nd, 3rd, 4th, 125th etc.
    '''

    # Cover the majority of the cases
    if 10 <= self % 100 < 20:
        return str(self) + 'th'
    else: # Cover special cases for values where last digit is 1,2,or 3
        return  str(self) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(self % 10, "th")
# End Function - ordinal



#=============================================================================#
#--
# Function: parse_ascii_file(...)
#++
#
# Description: Returns an LIST containing the lines of text read from the specified ASCII Text file
#              Each line in the file becomes a separate item in the LIST.
#              Verifies that the file exists and is readable
#
# Returns: LIST = An LIST of STRINGS - Each item in the LIST is a separate line read from the ASCII file
#
# Syntax: sFullPathToFile = STRING - The fullpath to the ASCII text file to be read
#
# Pre-requisites:
#                 The file must:
#                    a) Exist at the specified location
#                    b) Be a file NOT a folder
#                    c) Be a Readable ASCII text file
#                    d) NOT a zero length file
#
# Usage Examples: To read an ASCII text file at C:\MyTextFile.txt into an LIST:
#
#                    aContentsOfFile =  parse_ascii_file("C:\MyTextFile.txt")
#                    print2("Number of lines in the file: " + str(aContentsOfFile.length))
#                    print2("Last line in file: " + str(((aContentsOfFile.length) -1))
#                    for sLineOfText in aContentsOfFile:
#                        print2(sLineOfText)
#                    # end
#=============================================================================#
def parse_ascii_file(sFullPathToFile):

    '''
    Returns an LIST containing the lines of text read from the specified ASCII Text file
    Each line in the file becomes a separate item in the LIST.
    '''

    #VERBOSE = True

    # Define default return value
    aFileContents = ["FAILED_TO_READ_ASCII_FILE", "False"]


    # Perform some basic checks on the file. Any error will return the default value
    #
    # Verify the file exists
    if(os.path.exists(sFullPathToFile) == False):
        if(VERBOSE == True):
            print2("File does not exist")
        # end
        return aFileContents

    else:  # It exists so perform additional test on the file

        # Verify it is a file and not a directory
        if(os.path.isfile(sFullPathToFile) == False):
            if(VERBOSE == True):
                print2("Not a file, its a Directory")
            # end
            return aFileContents
        # end


        # Verify the file is an ASCII Text file NOT a directory, characterSpecial, blockSpecial, fifo, link, socket, or unknown file type
        if(os.path.isfile(sFullPathToFile) == False):
            if(VERBOSE == True):
                print2("File is not an ASCII text file")
            # end
            return aFileContents
        # end
        '''
        # Verify the file is readable  (F_OK = exists, R_OK = Readable, W_OK = Writable, X_OK = Executable)
        # TODO: Jython 2.2.1 does NOT support os.access(), nor os.R_OK
        if(os.access(sFullPathToFile, os.R_OK) == False):
            if(VERBOSE == True):
                print2("File is not readable")
            # end
            return aFileContents
        # end
        '''


        # Verify the file is not a zero length file
        if(os.path.getsize(sFullPathToFile) < 0):
            if(VERBOSE == True):
                print2("File is of zero len")
            # end
            return aFileContents
        # end

    # End Perform some basic checks on the file

    if (VERBOSE == True):
        print2("Opening file, read-only")
    # End

    # Access the file (read-only) and populate an LIST with its contents, line by line
    #aFileContents = file.open.(sFullPathToFile, "r").collect
    fFile = open(sFullPathToFile, 'r')
    aFileContents = fFile.readlines()
    fFile.close()

    return aFileContents

# End Function - parse_ascii_file()


#=============================================================================#
#--
# Function: parse_csv_file(...)
#
# TODO: Jython 2.2.1 does not include the module "csv"
#       The csv module was included in a later release
#++
#
# Description: Returns a DICT LIST containing data read from the
#              specified Comma Separated Value (CSV) file read from
#              the file in the specified sub-directory (e.g. my_data).
#              In the CSV file the data needs to be arranged by record=row, NOT record=column
#
#
# Returns: LIST = Data read from CSV file (aCSVData)
#
# Syntax: sCSVFilename = STRING - Excel workbook's filename
#         sSubDirName = STRING - name of the sub-directory that holds the CSV file
#
# Pre-requisites:
#                 The CSV data file must:
#                    a) Exist within the specified sub-directory
#                    b) Be readable from the specified sub-directory
#                 In the CSV file the data must be:
#                    a) Arranged by record=row, NOT record=column
#                    b) Contained in a contiguous block
#=============================================================================#
def parse_csv_file(sCSVFilename="", sSubDirName=DATA_DIR):

    '''
    Returns a DICT LIST containing data read from the specified Comma Separated Value (CSV) file
    '''

    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - parse_csv_file:")
        print2("  sCSVFilename: " + sCSVFilename)
        print2("  Containting folder: " + sSubDirName)
    # end

    # The CSV library
    import csv

    # Define default value
    aCSVData = []

    # Find the location of the directory holding the testsuite data
    sDataDir = find_folder_in_tree(sSubDirName)

    if(VERBOSE == True):
        print2(" Found containing folder: '" + sDataDir + "'")
    # end

    # Verify that the files exist in the proper location
    try:

        # Generate the full path to the CSV file
        sFullPathToFile = os.path.join(sDataDir, sCSVFilename)

        # Cleanup  "\\", or ".."  in path
        sFullPathToFile = os.path.normpath(sFullPathToFile)

        if (VERBOSE == True):
            print2(" Opening CSV file '" + sFullPathToFile + "'")
        # end

        # Check that the files exist
        if (os.path.exists(sFullPathToFile) != False):

            if(VERBOSE == True):
                print2(" Found CSV file: '" + sFullPathToFile + "'")
            # end

            if(VERBOSE == True):
                print2("Open the CSV file and read each record")
            # end

            # Define a null LIST to hold the data
            aCSVData = None

            # Open the CSV file and read each record (record=row) into a DICT
            # where each element in the parent LIST is a record from the CSV,
            # the child LIST holds the individual
            # fields from the CSV record.
            #
            aCSVData = list(csv.reader(open(sFullPathToFile, "r")))

            if(VERBOSE == True):
                print2("RAW Contents of CSV file: " + str(aCSVData))
            # end

            #return aCSVData

        else:
            if(VERBOSE == True):
                print2(" Unable to find CSV file: '" + sFullPathToFile + "'")
            # end
        # end Check that the files exist

    except:

        # Record an  error message
        print2("*** WARNING - Unable to read CSV file: " + str(sCSVFilename), "WARN")
        print2("*** WARNING and trace:")
        print2('-'*60)
        traceback.print_exc(file=sys.stdout)
        print2('-'*60)
    else:
        return aCSVData
    # end

# End  Function - parse_csv_file()


#=============================================================================#
#--
# Function: parse_dictionary(...)
#++
#
# Description: Returns an LIST containing the lines of text read from the PyWorks Dictionary file
#              Each line in the file contains one word, which becomes a separate item in the LIST.
#
# Returns: LIST = An LIST of STRINGS -Each item in the LIST is a separate word read from Dictionary
#
# Syntax: N/A
#
#
# Usage Examples: To read the words in the dictionary into an LIST
#                      aDictionaryContents =  parse_dictionary()
#=============================================================================#
def parse_dictionary(self):

    '''
    Returns an LIST containing the lines of text read from the PyWorks Dictionary file
    '''

    #VERBOSE = True

    # Name of the PyWorks dictionary file
    sFile = "dictionary_en.txt"

    # Determine where in the filesystem that PyWorks is installed
    sPath = get_PyWorks_install_path()
    
    # Get the list of files in the PyWorks tree
    aPyWorksFileList = list_tree(sPath)
    
    for sPath in aPyWorksFileList:
        if re.search(sFile,sPath):
            sFullPathToFile = sPath
        # end
    # end
    
    if (VERBOSE == True):
        print2("Reading file: " + sFullPathToFile)
    # End

    # Populate the LIST with the contents of the dictionary
    aDictionaryContents = parse_ascii_file(sFullPathToFile)

    if(VERBOSE == True):
        print2("File contents...")
        print2(aDictionaryContents)
    # End

    return aDictionaryContents

# End Function - parse_dictionary()


#=============================================================================#
#--
# Function: prefix(...)
#
#++
#
# Description: Returns only the prefix of the string.
#
#              The prefix is the characters proceeding the first Delimiter
#              of the string.
#
# HINT: Use to separate file extensions from file names, or to separate
#       strings like email addresses, or domain names into their sub components.
#
# Returns: STRING = The prefix of the string
#
# Syntax: sDelimiter = STRING - The character to use as the delimiter
#
# Usage Examples:
#               1) To verify a file name (without extension) is "some_file"
#                    sMyFile = "some_long_filename.log"
#                    sMyFilePrefix = prefix(sMyFile, ".")
#                    assert(sMyFilePrefix == "some_file")
#
#               2) To verify the user account of a Email address is "joe"
#                    sMyEmailAddress = "joe@gmail.net"
#                    sMyUserAccount = prefix(sMyEmailAddress,"@")
#                    assert(sMyUserAccount == "joe")
#
#               3) To verify the protocol of a URL is "http"
#                    browser.goto("google.com")
#                    sMyURL = browser.url
#                    sMyPrefix = prefix(sMyURL,":")
#                    assert(sMyPrefix.downcase == "http")
#
#               4) To return the first word in a string
#                    sMyString = "This is a test"
#                    sMyFirstWord = prefix(sMyString," ")
#                    assert(sMyFirstWord == "This")
#
#=======================================================================#
def prefix(self, sDelimiter = "."):

    '''
    Returns only the prefix of the string
    '''

    #VERBOSE = True
    
    if(VERBOSE == True):
        print2("Parameters - prefix:")
        print2("  sDelimiter: " + sDelimiter)
    # end

    # Set default return value
    sPrefix = self

    try:

        # Only allow single character delimiter's, Use 1st char if multiple chars were specified
        sDelimiter = sDelimiter[0]


        # Remove any training whitespace
        sString = self.strip()

        # Find index of the Delimiter
        iIndex = sString.find(sDelimiter, 0)


        # Save character 0, up to the Delimiter's index, leaving off the Delimiter
        #sPrefix = sString[0, iIndex]

        sPrefix = sString[0:iIndex]

    except:

        return self  # If something went wrong, return the original string. No harm no foul

    # end
    if(iIndex == -1):
        return self
    else:
        return sPrefix # Return the modified string

# End Function -prefix()

#=============================================================================#
#--
#  Function: printenv(...)
#++
#
# Description: Display the specified Environment variables and their corresponding values
#              to STDOUT. Similar to the UNIX/Linux command "printenv".
#
#              In effect this methods displays all or part of ENV object to STDOUT.
#
#              The ENV object is populated with the O/S variables
#              that were set when the process that launched Java started.
#
# Syntax: sEnvVar = STRING - The case sensitive string of the Environment variable to display.
#                             If no variable is specified then all the variables are displayed
# Usage examples:
#              To display the variable "COMPUTERNAME" and its setting:
#                  printenv("COMPUTERNAME")
#
#              To display all the variables and their settings:
#                 printenv()
#=============================================================================#
def printenv(sEnvVar = None):

    '''
    Display the specified Environment variables and their corresponding
    values to STDOUT. Similar to the UNIX/Linux command "printenv
    '''

    # Get the O/S Env variables
    hAllEnvVars= get_env(sEnvVar)
    #print2 hAllEnvVars

    # Loop through the O/S Env variables
    for key, value in hAllEnvVars.iteritems():

        if(sEnvVar == None) | (sEnvVar == "") :  # Display all the variables if a specific variable was NOT specified
            #sEnvVar = " "
            #print2(key  + " = " + str(value))
            print2(str(key) + " = " + (str(value)))

        else: # Display only the specified variable if one was specified
            if(key == sEnvVar):
                if value == None:
                    print2(key  + " = ")
                else:
                    print2(key  + " = " + str(value))
            # end


        # end

    # End End of loop

# End Function - printenv()


#=============================================================================#
#--
# Function: print2(...)
#++
#
# Description: Wrapper around the Jython method print()
#
#              If running from within SOAtest:
#                  Allows messages to be sent to STDOUT via print(), and to the SOATest Console
#                  (if one was started) via the SOATest method Application.showMessage(
#
#                  Presumes that when the SOATest Console exists, messages should be output
#                  to both STDOUT and the SOATest Console.
#
#                  If the SOATest Console was NOT started no writes to it occur.
#
#              If running outside of SOATest and a logger is availale:
#
#                  Allows messages to be sent to STDOUT via print(), or to the log file
#                  (if one was started), or to both locations. Defaults to both.
#
#                  Presumes that when a log file exists, messages should be output
#                  to both STDOUT and the log file. So the default parameters are set
#                  to make this the one needing the least parameters.
#
#                  If Global logger was NOT started no writes to the log file occur.
#                  Determines if a Global $logger was started and skips any writes to the log file it it was not.
#
#              The majority of the methods in PyWorks use this method to alleviate the need
#              for separate Jython print() and SOATest Application.showMessage() statements
#
#
# Returns: BOOLEAN - True on success, otherwise False
#
# Syntax: sMessage = STRING - The text to write to STDOUT and/or the log file
#
#         sLogLevel = STRING - The message level. One of the following:
#                             Messages have varying levels (info, error, etc), reflecting their varying importance.
#                             The levels, and their meanings, are:
#                                   CRITICAL: an unhandleable error that results in a program crash
#                                   ERROR: a handleable error condition
#                                   WARN: a warning
#                                   INFO: generic (useful) information about system operation
#                                   DEBUG: low-level information for developers
#                              Defaults to level 1 (INFO) of no sLogLevel is specified.
#
#         iChoice = INTEGER - Values of 0 write only to STDOUT via puts()
#                                Values > 0 write to STDOUT via puts() and to log file via log()  (default setting)
#                                Values < 0 write only to log()
#
# Usage Examples: 1) To output an informational message to both STDOUT
#                    and the SOATest Console (if it exists)
#                       print2("Message")
#
#=============================================================================#
def print2(sMessage, sLogLevel = "INFO", iChoice = 1):

    '''
    Wrapper around the Jython method print() and SOATest method Application.showMessage()
    '''

    #if(VERBOSE == True):
    #    print("Parameters - print2:")
    #    print("  sMessage: " + sMessage)
    #    print("  sLogLevel: " + sLogLevel)
    #    print("  iChoice: " + str(iChoice))
    ## end

    bReturnStatus = False # Set default return value

    # Determine if running from within SOATest
    if(is_SOATest() == True):

        from com.parasoft.api import *

        print(sMessage)  # Echo message to stdout

        # Echo message to the SOATest Console
        Application.showMessage(sMessage)

    else:  # Not running under SOATest
        try:

            import logging

            # Define the valid log level settings
            aValidLogLevels = ["CRITICAL", "ERROR", "WARNING", "WARN", "INFO", "DEBUG"]

            # Validate the Log Level value
            if((sLogLevel.upper() in aValidLogLevels) == False):
                sLogLevel = "ERROR"
            # end

            # Validate the iChoice setting
            if(iChoice > 0):
                iChoice = 1
            # end
            if(iChoice < 0):
                iChoice = -1
            # end

            # Get the PyWorks logger object
            oLogger = logging.getLogger("PyWorks")

            # Now that iChoice is properly set we can attempt to write
            if(iChoice == 0): #  Write only to STDOUT
                print(sMessage)  # Echo message to stdout

            elif(iChoice == 1): # Write to STDOUT and to log file via log()
                print(sMessage)  # Echo message to stdout
                # Write to the log file if one was started
                if (sLogLevel.upper() == "DEBUG"):
                    oLogger.debug(sMessage)           # Calls level 0 error
                elif (sLogLevel.upper() == "INFO"):
                    oLogger.info(sMessage)             # Calls  level 1 info
                elif (sLogLevel.upper() == "WARN"):
                    oLogger.warning(sMessage)           # Calls  level 2 warn
                elif (sLogLevel.upper() == "ERROR"):
                    oLogger.error(sMessage)           # Calls  level 3 error
                else: # (sLogLevel.upper() == "CRITICAL"):
                    oLogger.critical(sMessage)           # Calls  level 5 critical
                #else:
                #    oLogger.info(sMessage)           # If no level is specified, Calls level 1 info
                # end

            elif(iChoice == -1):# Write only to log file via log()

                if (sLogLevel.upper() == "DEBUG"):
                    oLogger.debug(sMessage)           # Calls level 0 error
                elif (sLogLevel.upper() == "INFO"):
                    oLogger.info(sMessage)             # Calls  level 1 info
                elif ("WARN" in sLogLevel.upper()): # Cover both WARN and WARNING
                    oLogger.warning(sMessage)           # Calls  level 2 warn
                elif (sLogLevel.upper() == "ERROR"):
                    oLogger.error(sMessage)           # Calls  level 3 error
                else: # (sLogLevel.upper() == "CRITICAL"):
                    oLogger.critical(sMessage)           # Calls  level 5 critical
                #else:
                #    oLogger.info(sMessage)           # If no level is specified, Calls level 1 info
                # end

            # end

            bReturnStatus = True

        except:

            print(sMessage)  # Echo message to stdout
            
            bReturnStatus = False

        # end

    # end # Not running under SOATest

    bReturnStatus = True

    return bReturnStatus


# End Function - print2()

#=============================================================================#
#--
# Function: random_alphanumeric(...)
#
#++
#
# Description: Generates a String of the specified length that's populated with random alpha-numeric characters
#              Characters used are:  a-z  A-Z  0-9
#
#              From: http://snippets.dzone.com/tag/ruby/
#
# Returns: STRING = The generated string of the specified character length
#
# Syntax: iLength = INTEGER -  The length of the string to generate
#
# Usage Examples:
#                 print2(random_alphanumeric(10)) #=> ab8he2shjz
#
#=============================================================================#
def random_alphanumeric(iLength = 10):

    '''
    Generates a String of the specified length that's populated with random alpha-numeric characters
    '''


    if(VERBOSE == True):
        print2("Parameters - random_alphanumeric:")
        print2("  iLength: " + str(iLength))
        # end

    # Disallow values less than 1
    if(iLength < 1):
        iLength = 1
        # end

    # Define list of ASCII characters to pick from
    sValidChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'


    #  Generate string using random numbers for the ASCII character codes of the characters: 0-9, a-z, A-Z
    sString = ''.join([random.choice(sValidChars) for _ in range(iLength)])

    return sString

    # End Function - random_alphanumeric()



#=============================================================================#
#--
# Function: random_boolean()
#
#++
#
# Description: Generates a random BOOLEAN value of True or False
#
# Returns: BOOLEAN = A random value of 1 (True) or 0 (False)
#
# Syntax: N/A
#
# Usage Examples:  print2(str(random_boolean())) #=> 1
#
#=============================================================================#
def random_boolean():

    '''
    Generates a random BOOLEAN value of True or False
    '''


    if((random_number(0, 1)) == 1):
        return True
    else:
        return False
    # end

# End Function - random_boolean()


#=============================================================================#
#--
# Function: random_char()
#
#++
#
# Description: Generates a random STRING value of a single ASCII character
#
# Returns: STRING = A random value of a single upper case or lower case ASCII character
#
# Syntax: bLowercase = BOOLEAN - True for UPPER CASE or False for lower case,
#
# Usage Examples:  print2(random_char()) #=> w
#                  print2(random_char(True)) #=> G
#
#
#=============================================================================#
def random_char(bUpcase = False):

    '''
    Generates a random STRING value of a single ASCII character
    '''

    if(VERBOSE == True):
        print2("Parameters - random_char:")
        print2("  bUpcase: " + str(bUpcase))

    # Generate the ASCII Character
    sChar = str(chr(random_number(97, 122)))

    # Need to Upcase the character or not
    if(bUpcase == False):
        return sChar.lower()
    else:
        return sChar.upper()

# End Function - random_char()


#=============================================================================#
#--
# Function: random_chars(...)
#
#++
#
# Description: Generates a random STRING value of a specified number of ASCII characters
#
# Returns: STRING = A random set of a lower case or Capitalized ASCII characters
#
# Syntax: iLength = INTEGER - The length of the characters in string to generate
#         bCapitalize = BOOLEAN - True to Capitalize 1st character in string or False for all lower case,
#
# Usage Examples:  print2(random_chars()) #=> wshjeochtybisuaqlxyh
#                  print2(random_chars(10, True)) #=> Gslknmeruh
#
#
#=============================================================================#
def random_chars(iLength = 10, bCapitalize = False):

    '''
    Generates a random STRING value of a specified number of ASCII characters
    '''


    if(VERBOSE == True):
        print2("Parameters - random_chars:")
        print2("  iLength: " + str(iLength))
        print2("  bCapitalize: " + str(bCapitalize))
    # end

    # Disallow values less than 1
    if(iLength < 1):
        iLength = 1
    # end

    # Start with an empty character set
    sChars = ""

    # Populate the set of ASCII Characters
    for _ in xrange(iLength):
        sChars += random_char()
    # end

    # Capitalize the character set?
    if(bCapitalize == False):
        return sChars
    else:
        return sChars.capitalize()
    # end

# End Function - random_chars()


#=============================================================================#
#--
# Function: random_number(...)
#
#++
#
# Description: Generates a random Integer value between the specified Min and Max values (inclusive)
#
# Returns: INTEGER = A random number >= iMin, but <= iMax
#
# Syntax: iMin = INTEGER -  The minimum value
#         iMax = INTEGER -  The maximum value
#
# Usage Examples: print2(str(random_number(5, 10))) #=> 6
#
#
#=============================================================================#
def random_number(iMin = 0, iMax = 1):

    '''
    Generates a random Integer value between the specified Min and Max values (inclusive)
    '''

    if(VERBOSE == True):
        print2("Parameters - random_number:")
        print2("  iMin: " + str(iMin))
        print2("  iMax: " + str(iMax))

    # Generate the random number
    return random.randint(iMin, iMax)

# End Function - random_number()


#=============================================================================#
#--
# Function: random_paragraph(...)
#
#++
#
# Description: Generates a random STRING value of a specified number of sentences that are
#              comprised of pseudo words which in turn are comprised of random ASCII characters.
#
# Returns: STRING = A random set of sentences comprised of pseudo words  of ASCII characters
#
# Syntax: iNumberOfSentences = INTEGER - The number of sentences in the paragraph to generate
#         iMaxWordsPerSentence = INTEGER - The maximum number of pseudo words per sentence to generate
#         iMaxCharsPerWord = INTEGER - The max number of characters in each pseudo words to generate
#
# Usage Examples:  Generate as set of 4 sentences with a max of 6 pseudo words of 10 characters each:
#                     print2(random_paragraph(4, 6, 10))
#
#                  Generate a random paragraph of sentences from a random set of pseudo words of random length
#                     print2(random_paragraph(random_number(3,5), random_number(4,6), random_number(5,7)))
#
#
#=============================================================================#
def random_paragraph(iNumberOfSentences = 2, iMaxWordsPerSentence = 10, iMaxCharsPerWord = 10):

    '''
    Generates a random STRING value of a specified number of sentences that are
    comprised of pseudo words which in turn are comprised of random ASCII characters.
    '''

    if(VERBOSE == True):
        print2("Parameters - random_paragraph:")
        print2("  iNumberOfSentences: " + str(iNumberOfSentences))
        print2("  iMaxWordsPerSentence: " + str(iMaxWordsPerSentence))
        print2("  iMaxCharsPerWord: " + str(iMaxCharsPerWord))
    # end

    # Start with an empty paragraph
    sParagraph = ""

    # Disallow values less than 1
    if(iNumberOfSentences < 1):
        iNumberOfSentences = 1
    # end

    # Disallow values less than 1
    if(iMaxWordsPerSentence < 1):
        iMaxWordsPerSentence = 1
    # end

    # Disallow values less than 1
    if(iMaxCharsPerWord < 1):
        iMaxCharsPerWord = 1
    # end

    # Loop for each sentence
    for _ in xrange(iNumberOfSentences):

        sString = random_pseudowords(random_number(2, iMaxWordsPerSentence), iMaxCharsPerWord)
        sParagraph += to_sentence(sString) + " "

    # Loop for each sentence

    return sParagraph + "\n\n"

# End Function - random_paragraph()


#=============================================================================#
#--
# Function: random_pseudowords(...)
#
#++
#
# Description:  Generates a random STRING value of a specified number of pseudo words comprised
#               of random ASCII characters.
#
#               If you need a set of dictionary words please use the method random_words() .
#
# Returns: STRING = A random set of a lower case or Capitalized pseudo words comprised  of ASCII characters
#
# Syntax: iSetLength = INTEGER -  The length of the number of pseudo words to generate
#         iMaxWordLength = INTEGER - The max length of the number of characters in each pseudo words to generate
#         bCapitalize = BOOLEAN - True to Capitalize 1st character in string or False for all lower case,
#
# Usage Examples:  Generate as set of 3 pseudo words of 10 characters each:
#                     print2(random_pseudowords(3, 10, False)) #=> wshjeochty mjuhygtrfd mkliygcdwk
#
#                 Generate a random set of pseudo words of random length and Capitalize the set.
#                     print2(random_pseudowords(random_number(2,5), random_number(2,10), True)) #=> Go lkdknmeruh jsdhf fie om
#
#
#=============================================================================#
def random_pseudowords(iSetLength = 10, iMaxWordLength = 10, bCapitalize = False):

    '''
    Generates a random STRING value of a specified number of pseudo words comprised
    of random ASCII characters
    '''

    if(VERBOSE == True):
        print2("Parameters - random_pseudowords:")
        print2("  iSetLength: " + str(iSetLength))
        print2("  iMaxWordLength: " + str(iMaxWordLength))
        print2("  bCapitalize: " + str(bCapitalize))
    # end

    # Disallow values less than 1
    if(iSetLength < 1):
        iSetLength = 1
    # end

    # Disallow values less than 1
    if(iMaxWordLength < 1):
        iMaxWordLength = 1
    # end

    # Start with an empty word set
    sPsuedoWords = ""

    # Populate the set of pseudo words with a set of random length character sets, with each word separated by a space
    for _ in xrange(iSetLength):
        sPsuedoWords += random_chars(random_number(1, iMaxWordLength)) + " "
    # end

    # Remove the trailing white space
    sPsuedoWords.strip()

    # Capitalize the pseudo word set?
    if(bCapitalize == False):
        return sPsuedoWords
    else:
        return sPsuedoWords.capitalize()
    # end

# End Function - random_pseudowords()


#=============================================================================#
#--
# Function: random_sentence(...)
#
#++
#
# Description: Makes a sentence of a specified number of words randomly selected from the PyWorks Dictionary
#
# Returns: STRING = A random sentence
#
# Syntax:  iNumberOfWords = INTEGER - The number of words to include in the sentence,
#
# Usage Examples: print2(random_sentence(5)) #=> Cabinetmaker ungraded cub's minimalist irene?
#                 print2(random_sentence(3)) #=> Lifestyles popper radish's!
#
#
#=============================================================================#
def random_sentence(iNumberOfWords = 2):

    '''
    Makes a sentence of a specified number of words randomly selected from the PyWorks Dictionary
    '''

    if(VERBOSE == True):
        print2("Parameters - random_sentence:")
        print2("  iNumberOfWords: " + str(iNumberOfWords))
    # end

    # Define default return value
    sSentence = ""

    # Disallow values less than 1
    if(iNumberOfWords < 1):
        iNumberOfWords = 1
    # end

    for _ in xrange(iNumberOfWords):
        sSentence += str((random_word()) + " ")


    return to_sentence(sSentence)

# End Function - random_sentence()


#=============================================================================#
#--
# Function: random_word(...)
#
#++
#
# Description: Retrieves a random word read from the PyWorks Dictionary
#
# Returns: STRING = A random lower case or Capitalized word
#
# Syntax:  bCapitalize = BOOLEAN - True to Capitalize 1st character in word or False for all lower case,
#
# Usage Examples: print2(random_word()) #=> word
#                 print2(random_word(True)) #=> Random
#
#
#=============================================================================#
def random_word(bCapitalize = False):

    '''
    Retrieves a random word read from the PyWorks Dictionary
    '''

    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - random_word:")
        print2("  bCapitalize: " + str(bCapitalize))
    # end

    DICTIONARY = None


    # To save time only read the dictionary into a global LIST if that LIST wasn't populated already
    if(DICTIONARY == None):
        # Populate the global LIST of words from the dictionary
        DICTIONARY = parse_dictionary(None)
    # End - To save time ...

    iNumberOfWords = len(DICTIONARY)
    if(VERBOSE == True):
        print2("Number Of Words = " +  str(iNumberOfWords))
    # End

    # Pick a random word from the dictionary
    sWord = DICTIONARY[random_number(1, iNumberOfWords-1)]
    #sWord = DICTIONARY[4]

    #Remove and leading or trailing spaces
    sWord = sWord.strip()

    # Capitalize the word?
    if(bCapitalize == False):
        return str(sWord.lower())   # Words in the dictionary may be UPPER, lower or Capitalized so standardize on lower case
    else:
        return str(sWord.capitalize())
    # End Capitalize the word?

# End Function - random_word()



#=============================================================================#
#--
# Function: remove_prefix(...)
#
#++
#
# Description: Returns the string with the prefix removed.
#
#              The prefix is the characters proceeding the first Delimiter
#              of the string.
#
# HINT: Use to separate file extensions from file names, or to separate
#       strings like email addresses, or domain names into their sub components.
#
# Returns: STRING = The string with the prefix removed.
#
# Syntax: sDelimiter = STRING - The character to use as the delimiter
#
# Usage Examples:
#               1) To verify a file name extension is "log"
#                    sMyFile = "some_long_filename.log"
#                    sMyFileExt = remove_prefix(sMyFile, ".")
#                    assert(sMyFileExt == "log")
#
#               2) To verify the domain of a Email address is "gmail.net"
#                    sMyEmailAddress = "joe@gmail.net"
#                    sMyDomain = remove_prefix(sMyEmailAddress, "@")
#                    assert(sMyDomain == "gmail.net")
#
#               3) To return the string with the first word removed
#                    sMyString = "This is a test"
#                    sMyStringLessFirstWord = remove_prefix(sMyString, " ")
#                    assert(sMyStringLessFirstWord == "is a test")
#
#=======================================================================#
def remove_prefix(self, sDelimiter = "."):

    '''
    Returns the string with the prefix removed
    '''

    if(VERBOSE == True):
        print2("Parameters - remove_prefix:")
        print2("  sDelimiter: " + sDelimiter)
    # end

    # Set default return value
    sString = self

    try:

        # Only allow single character delimiter's, Use 1st char if multiple chars were specified
        sDelimiter = sDelimiter[0]

        # Remove any training whitespace
        sString = self.strip()

        # Find index of the Delimiter
        iIndex = sString.find(sDelimiter)

        # Find the length of the string
        iStringLength = len(sString)

        # Save characters from one after the Delimiter's index, leaving off the Delimiter, to the end of the string
        sString = sString[iIndex + 1: iStringLength]

    except:

        return self  # If something went wrong, return the original string. No harm no foul

    # end

    return sString # Return the modified string

# End Function - remove_prefix()


#=============================================================================#
#--
# Function: remove_suffix(...)
#
#++
#
# Description: Returns the string with the suffix removed.
#
#              The suffix is the characters following the last Delimiter
#              to the end of the string.
#
# HINT: Use to separate file extensions from file names, or to separate
#       strings like email addresses, or domain names into their sub components.
#
# Returns: STRING = The string with the suffix removed
#
# Syntax: sDelimiter = STRING - The character to use as the delimiter
#
# Usage Examples:
#               1) To verify a file name without the extension is "some_long_filename"
#                    sMyFile = "some_long_filename.log"
#                    sMyFileLessExtension = remove_suffix(sMyFile, ".")
#                    assert(sMyFileLessExtension == "some_long_filename")
#
#               2) To verify the User Account of a Email address is "me"
#                    sMyURL = "me@gmail.net"
#                    sMyStringLessSuffix = remove_suffix(sMyURL, "@")
#                    assert(sMyStringLessSuffix == "me")
#
#               3) To verify the To Level Domain of a URL is "net"
#                    sMyDomain = "gmail.net"
#                    sMySuffix = remove_suffix(sMyDomain, ".")
#                    assert(sMySuffix == "net")
#
#               3) To return the last word in a string
#                    sMyString = "This is a test"
#                    sMyLastWord = remove_suffix(sMyString, " ")
#                    assert(sMyLastWord == "test")
#
#=======================================================================#
def remove_suffix(self, sDelimiter = "."):

    '''
    Returns the string with the suffix removed
    '''

    if(VERBOSE == True):
        print2("Parameters - remove_suffix:")
        print2("  sDelimiter: " + sDelimiter)
    # end

    # Set default return value
    sString = self

    try:

        # Only allow single character delimiter's, Use 1st char if multiple chars were specified
        sDelimiter = sDelimiter[0]

        # Remove any training whitespace
        sString = self.strip()

        # Flip the string so that the suffix is at the beginning
        sReversedString = sString[::-1]

        # Find the length of the string
        iStringLength = len(sReversedString)

        # Find index of the Delimiter
        iIndex = sReversedString.find(sDelimiter)

        # Save character from 0, up to the Delimiter's index, leaving off the Delimiter
        sReversedString = sReversedString[iIndex + 1: iStringLength]

        #Flip the remaining string which now has the suffix by itself
        sString = sReversedString[::-1]

    except:

        return self  # If something went wrong, return the original string. No harm no foul

    # end

    return sString # Return the modified string

# End Function - remove_suffix()

#=============================================================================#
#--
#  Function: reverse_string()
#++
#
# Description: Reverses the characters in a string.
#
#`             There is no existing String method to reverse the order of the
#              characters in a string.
#              Strings are immutable, so cast it to a list object
#              then use the list object's method .reverse() which flips
#              the order of the members of the list in place.
#              finally use .join to reassemble the individual list components
#              back into a string.
#
# Syntax: self = STRING - The string to be reversed
#
# Usage examples:
#              To reverse the string "COMPUTERNAME" :
#                  sString = "COMPUTERNAME"
#                  sReversedString = reverse_string(sString)
#                  print2(sReversedString)
#
#=============================================================================#
def reverse_string(self):

    '''
    Reverses the characters in a string
    '''


    if(VERBOSE == True):
        print2("Parameters - reverse_string:")
        print2("  self: " + str(self))
    # end

    # Cast the string to a list
    aStringList = list(self)

    # Reverse the list's components
    aStringList.reverse()

    # Reassemble the list components into a string
    sString = ''.join(aStringList)

    if (VERBOSE == True):
        print2("\tReversed string = '" + sString + "'")
    # end

    return sString
# End Function reverse_string()

#=============================================================================#
#--
# Function: set_env(...)
#++
#
# Description: Sets the specified environment variable to the specified value,
#              Similar to the UNIX/Linux command "setenv".
#
#              In effect this method modifies the ENV object.
#
#              The ENV object is populated with the O/S environment variables
#              that were set when the process that launched Java started.
#
# Note: This method is not any more useful that accessing the O/S variable values directly
#       from the ENV object, (i.e. ENV["Path"] = "NewValue" will set  that O/S variable),
#       Since a printenv() and a getenv() method were also coded, this setenv() method is
#       supplied to complete the set.
#
# Returns: DICT = hEnvVars - A DICT of the environment variables (key) and setting (value)
#
# Syntax: sEnvVar = STRING - The case sensitive string of the O/S Environment variable to set.
#         sValue = STRING - The case sensitive string of the value to set the O/S Environment variable to
#
# Usage examples:
#                set_env("COMPUTERNAME", "MyPC")
#=============================================================================#
def set_env(sEnvVar = None, sValue = None):

    '''
    Sets the specified environment variable to the specified value,
    Similar to the UNIX/Linux command "setenv".
    '''

    if sEnvVar == None:
        return False
    # end

    # Set the specified variable to the specified value
    os.putenv(sEnvVar, sValue)

# End Function - set_env()


#=============================================================================#
#--
# Function: start_logger(...)
#
#++
#
# Description: Creates a new LOGGER object to write to a log file.
#              The logging module is not part of the jython2.2.1 release
#              It was added in a later release, and is present in the 2.5.2 release
#
#              When running within SOATest you should NOT use the logger.
#              OATest has a custom means to handle logging to the SOATest Console.
#
# Calls: Logger() to open a log file and sets parameters to use and maintain the log file.
#
# Returns: LOGGER object
#
# Syntax: sFullPathToFile = STRING - The full pathname and filename of the log file (Case sensitive)
#
#         iLogsToKeep = INTEGER - Number of log file to keep. Default value is 50
#
#         iMaxLogSize = INTEGER - Max size in bytes of the current log file. Once reached it
#                                 will roll to a new log file and rename the old file(s)
#                                 Default value is 50000000     5Mb
#
#         sLogLevel = STRING - The message level. One of the following (Per the Ruby Core API):
#                              Messages have varying levels (info, error, etc), reflecting their varying importance.
#                                 The levels, and their meanings, are:
#                                     CRITICAL: an unhandleable error that results in a program crash
#                                     ERROR: a handleable error condition
#                                     WARN: a warning
#                                     INFO: generic (useful) information about system operation
#                                     DEBUG: low-level information for developers
#
#                                (default value is "INFO")
#
#=============================================================================#
def start_logger(sFullPathToFile="Logfile.log", iLogsToKeep=50, iMaxLogSize= 5000000, sLogLevel="DEBUG"):

    '''
    Creates a new LOGGER object to write to a log file

    When running within SOAtest you should NOT use the logger.
    SOATest has a custom means to handle logging to the SOATest Console.
    '''

    #VERBOSE = True

    if(VERBOSE == True):
        print2("Parameters - start_logger:")
        print2("  sFullPathToFile: " + sFullPathToFile)
        print2("  iLogsToKeep: " + str(iLogsToKeep))
        print2("  iMaxLogSize: " + str(iMaxLogSize))
        print2("  sLogLevel: " + sLogLevel)
    # end

    # When running withinSOAtest you can't use the Jython logger
    if(is_SOATest() == False):
        import logging                      # The Jython logger which is the basis for the PyWorksLogger
    # end

    # Don't allow a blank values
    if((sFullPathToFile == "") | (sFullPathToFile == None)):
        sFullPathToFile = "Logfile.log"
    # end

    if((iLogsToKeep < 1) |  (iLogsToKeep > 1000)):
        iLogsToKeep=50
    # end

    if((iMaxLogSize < 1) |  (iMaxLogSize > 100000000)):
        iMaxLogSize=5000000
    # end

    if((sLogLevel == "") | (sLogLevel == None)):
        sLogLevel = "INFO"
    # end
    if(VERBOSE == True):
            print2("Starting the logger...")
    # end

    # Define the name of the logger's application to log
    oLogger = logging.getLogger("PyWorks")

    # Define the default log level
    if (sLogLevel.upper() == "DEBUG"):
        oLogger.setLevel(logging.DEBUG)
    elif (sLogLevel.upper() == "INFO"):
        oLogger.setLevel(logging.INFO)
    elif (sLogLevel.upper() == "WARN"):
        oLogger.setLevel(logging.WARN)
    elif (sLogLevel.upper() == "ERROR"):
        oLogger.setLevel(logging.ERROR)
    else:
        oLogger.setLevel(logging.CRITICAL)
    # end

    # Define the format of the log file entries and the timestamp
    #sFormat = "%(name)s - %(asctime)s - - %(message)s"
    sFormat = "%(levelname)8s - %(asctime)s - %(message)s"
    sDatefmt ='%a, %d %b %Y %H:%M:%S'

    # Create a log message handler
    oHandler = logging.handlers.RotatingFileHandler(sFullPathToFile, backupCount=iLogsToKeep, maxBytes=iMaxLogSize)

    # Assign the handler to the logger
    oLogger.addHandler(oHandler)

    # Create a formatter object
    oFormatter = logging.Formatter(sFormat, sDatefmt)

    # Assign the formatter to the handler
    oHandler.setFormatter(oFormatter)

    print2("PyWorks log file started.")
    oLogger.info("PyWorks log file started.")

    return oLogger

# END Function - start_logger()

#=============================================================================#
#--
# Function: string_to_date(...)
#++
#
# Description: Convert the specified date string to a date.
#              (e.g. "7/6/05"  to the date 2005-07-06)
#
# Returns: DATE - The converted date
#
# Syntax: sDateString = STRING - The string representation of a date to be converted
#                   Dates expressed as STRINGs must be format like:   mm/dd/yy    m/d/yyyy   m/d/yy   mm/d/yyyy
#
#          sDelimiter = STRING - The delimiter character
#
# Usage Examples:
#                 oDate = string_to_date("3/29/2011")
#
#=============================================================================#
def string_to_date(sDateString, sDelimiter="/"):

    '''
    Convert the specified date string to a date
    (e.g. "7/6/05"  to the date 2005-07-06)
    '''

    if(VERBOSE == True):
        print2("Parameters - string_to_date:")
        print2("  sDateString: " + sDateString)
        print2("  sDelimiter: " + sDelimiter)
    # end

    # Create a date object
    dToday = date.today()

    # Split the string into Month, Day and 4-digit year based on delimiter
    aMMDDYYY = sDateString.split(sDelimiter)

    if(VERBOSE == True):
        print2(aMMDDYYY)
    # end

    # Separate the List into its individual components
    sMM = aMMDDYYY[0]
    sDD = aMMDDYYY[1]
    sYYYY = aMMDDYYY[2]

    if(VERBOSE == True):
        print2("Month: " + sMM)
        print2("Day: " + sDD)
        print2("Year: " + sYYYY)
    # end

    # Covert string to integers
    iYear = int(sYYYY)
    iMonth = int(sMM)
    iDay = int(sDD)

    # Change and 2-digit year to a year in the current century
    if (iYear < 100):
        iYear = iYear + 2000
        print2(" Adjusted Year: " + str(iYear))
    # end

    # Generate the new date object
    oDate = date.replace(dToday, iYear, iMonth, iDay)

    return oDate

# end method - string_to_date()
#=============================================================================#
#--
# Function: subdirs(...)
#++
#
# Description: Returns a listing of the sub-directories in the specified filesystem directory
#
# Returns: LIST = An LIST of STRINGS - Each item in the LIST is a fullpathname of a directory
#
# Syntax: sRootDir = STRING - The fullpath to use as the root directory of the search
#         bSkip_symlinks = BOOLEAN - True = Don't follow links, False = follow links
#
# Pre-requisites:
#                 import os
#
# Usage Examples: To get a recursive listing of the sub-directories in the path C:\My_Path\subpath\folder:
#
#                    sRootDir =  "C:\My_Path\subpath\folder"
#                    aListing = list_tree(sRootDir)
#                    for sPath in aListing:
#                        print2(sPath)
#                    # end
#=============================================================================#
def subdirs(sRootDir, bSkip_symlinks = 1):
    '''
    Returns a listing of the sub-directories in the specified filesystem directory
    Given a root directory, returns the first-level subdirectories.
    '''

    try:
        dirs = [os.path.join(sRootDir, x)
                for x in os.listdir(sRootDir)]
        dirs = filter(os.path.isdir, dirs)
        if bSkip_symlinks:
            dirs = filter(lambda x: not os.path.islink(x), dirs)
        dirs.sort()
        return dirs
    except OSError, IOError: return []


#=============================================================================#
#--
# Function: suffix(...)
#
#++
#
# Description: Returns only the suffix of the string.
#
#              The suffix is the characters following the last Delimiter
#              to the end of the string.
#
# HINT: Use to separate file extensions from file names, or to separate
#       strings like email addresses, or domain names into their sub components.
#
# Returns: STRING = The suffix of the string
#
# Syntax: sDelimiter = STRING - The character to use as the delimiter
#
# Usage Examples:
#               1) To verify a file name extension is "log"
#                    sMyFile = "some_long_filename.log"
#                    sMyFileExtension = suffix(sMyFile,".")
#                    assert(sMyFileExtension == "log")
#
#               2) To verify the Domain of a Email address is "gmail.net"
#                    sMyURL = "me@gmail.net"
#                    sMySuffix = suffix(sMyURL,"@")
#                    assert(sMySuffix == "gmail.net")
#
#               3) To verify the Top Level Domain of a URL is "net"
#                    sMyDomain = "gmail.net"
#                    sMySuffix = suffix(sMyDomain,".")
#                    assert(sMySuffix == "net")
#
#               4) To return the last word in a string
#                    sMyString = "This is a test"
#                    sMyLastWord = suffix(sMyString," ")
#                    assert(sMyLastWord == "test")
#
#=======================================================================#
def suffix(self, sDelimiter = "."):

    '''
    Returns only the suffix of the string
    '''

    if(VERBOSE == True):
        print2("Parameters - suffix:")
        print2("  sDelimiter: " + sDelimiter)
    # end

    # Set default return value
    sSuffix = self

    try:

        # Only allow single character delimiter's, Use 1st char if multiple chars were specified
        sDelimiter = sDelimiter[0]

        # Remove any training whitespace
        sString = self.strip()

        # Flip the string so that the suffix is at the beginning
        sReversedString = sString[::-1]

        # Find index of the Delimiter
        iIndex = sReversedString.find(sDelimiter)

        # Save character from 0, up to the Delimiter's index, leaving off the Delimiter
        sReversedString = sReversedString[0: iIndex]

        #Flip the remaining string which now has the suffix by itself
        sSuffix = sReversedString[::-1]

    except:

        return self  # If something went wrong, return the original string. No harm no foul

    # end

    if (iIndex == -1):
        return self
    else:
        return sSuffix # Return the modified string

# End Function - suffix()
#=============================================================================#
#--
# Function: to_sentence(...)
#
#++
#
# Description: Converts a string, of one or more words, into a sentence by
#              Capitalizing it and appending a randomly selected punctuation mark (. ? !)
#
# Returns: STRING = The Capitalized string with the punctuation mark appended.
#
# Syntax: N/A
#
# Usage Examples:
#                 To change the string "this is a string" into a sentence
#                    sMyString = "this is a string"
#                    sSentence = to_sentence(sMyString)
#                    print2(sSentence)   #=> This is a string?
#
#
#=======================================================================#
def to_sentence(self):

    '''
    Converts a string, of one or more words, into a sentence by
    Capitalizing it and appending a randomly selected punctuation mark (. ? !)
    '''

    # Skip if None or blank
    if(self == None or self == ""):
        return self
    # end

    # Define the punctuation marks
    aPunctuationMarks = [".", "?", "!"]

    # Randomly select a punctuation mark to append
    sRandomPunctuationMark = aPunctuationMarks[random_number(0, 2)]

    if(VERBOSE == True):
        print2("sRandomPunctuationMark: " + sRandomPunctuationMark)
    # end

    try:

        sString = self

        # Remove any training whitespace and apply the capitalization to the 1st char in the string
        sString = sString.strip()
        sString = sString.capitalize()

        # Determine if the string ends with a period, question mark or exclamation point.
        #if(sString == r'/ . * [\.\?\ ! ]$ /'):
        if(re.search(r'.*[\.\?\!]$', sString)):

            # No need to append punctuation so apply the capitalization to the 1st char in the string
            return sString
        else:
            # Append punctuation to the string
            sString += sRandomPunctuationMark
            return sString
        # end



    except:

        return self  # If something went wrong, return the original string. No harm no foul

    # end

    return sString # Return the modified string

# End Function - to_sentence()


#=============================================================================#
#--
# Function: word_count()
#++
#
# Description:  Counts the words in a String like UNIX's word count command.
#               Words are counted as contiguous characters separated by whitespace.
#               Does not count whitespace.
#
# Returns: INTEGER = The number of words that were counted in the strings
#
# Usage Examples:
#
#     1.  print2(word_count("hello world")) #=> 2
#
#     2.  sStringVariable = "Don't count contractions or hyphens as two-words"
#
#            aListOfStrings = [
#              "Two words",
#              "  Multiple   Whitespace including tabs\t are ignored. Doesn't count new line\n or 123-456 \n a+b i:2  1/2    ",
#              sStringVariable,
#              "THE END"
#              ]
#
#           for sString in aListOfStrings:
#           print2("String: + sString)
#           print2("  Word count: " + str(word_count(sString)))
#
#         #> String:   Multiple   Whitespace is     ignored. New line
#          also.
#          123-456
#          a+b i:2  1/2
#           Word count: 11
#         String: Doesn't count contractions or hyphens as two-words
#           Word count: 7
#         String: THE END
#           Word count: 2
#
#=============================================================================#
def word_count(self):

    '''
    Counts the words in a String like UNIX's word count (wc) command
    '''

    self = self.strip() # Remove leading / trailing whitespace
    self = self.split(None) # Separate the STRING into a LIST so its characters can be counted

    #VERBOSE = True
    if (VERBOSE == True):
        print2(str(self))
    # end

    return len(self) # Return the INTEGER of the number of characters in the LIST
# End Function - word_count

# Define an alias
wc = word_count


#=============================================================================#
#======================= END  ================================================#
#=============================================================================#

# END File - PyWorks_Utilities.py
