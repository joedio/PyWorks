#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_convert_datestrings_unittest.py
#
#  Copyright (c) 2008-2011, Joe DiMauro
#  All rights reserved.
#
# Description: Unit tests for PyWorks STRING methods:
#                convert_date(...)
#
#
#
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by this test
#=============================================================================#

import unittest
#from datetime import date, datetime, timedelta # Add ability to get/format Dates
#import time                    # Add ability to get/format Time

# PyWorks
from PyWorks_Reflib import *       #  PyWorks Reference data module
from PyWorks_Utilities import *    # PyWorks General Utilities
#=============================================================================#

#=============================================================================#
# Global Variables section
# Set global variables that will be inherited by each of the test files
#=============================================================================#

# Java global variables
#

# Jython global variables
#

# PyWorks global variables
#
sRun_TestType = "ready"
iRun_TestLevel = 0
VERBOSE = False
#=============================================================================#

#=============================================================================#
# Class: UnitTest_Convert_Date
#
#
# Test Case Methods: setUp, tearDown
#                   test_Convert_Date_001_DateObjects
#                   test_Convert_Date_002_DatesAsStrings
#                   test_Convert_Date_003_InvalidDatesAsStrings
#
#
#=============================================================================#
class UnitTest_Convert_DateStrings(unittest.TestCase):


    #===========================================================================#
    # Method: setup
    #
    # Description: Before every testcase Test::Unit runs setUp
    #===========================================================================#
    def setUp(self):
        
        # Save the Global variable's original settings so that they can be changed in this
        # test without affecting other test, so long as they are restored by tearDown
        global VERBOSE_ORIG
        VERBOSE_ORIG = VERBOSE
        global DICTIONARY_ORIG
        DICTIONARY_ORIG = DICTIONARY
        
        global tTestCase_StartTime
        tTestCase_StartTime = datetime.now()
        
    # # end of setUp

    #===========================================================================#
    # Method: teardown
    #
    # Description: After every testcase Test::Unit runs tearDown
    #===========================================================================#
    def tearDown(self):
        
        print2("Testcase finished in " + calc_elapsed_time(tTestCase_StartTime) + " seconds.")
        
        # Restore the Global variable's original settings
        VERBOSE = VERBOSE_ORIG
        DICTIONARY = DICTIONARY_ORIG
        
        #print2("tearDown")
        
    # # end of tearDown
    
    #===========================================================================#
    # Method: runTest
    #
    # Description: The list of tests to run
    #===========================================================================#
    def runTest(self):
        """ List of tests to run """
        
        #self.test_String_001_wordcount()
        pass
    # End
    

    #===========================================================================#
    # Testcase method: test_Convert_Date_001_DateObjects
    #
    # Description: Test method convert_date(..) with date objects
    #===========================================================================#
    def test_Convert_Date_001_DateObjects(self):
        
        #require 'date'
        
        sToday = str(date.today())
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Convert_Date_001_DateObjects")
        print2("#######################")
        
        print2("Testing Timespan between dates and " + sToday + "\n\n")
        
        # Get the current date
        dToday = date.today()
        
        # 182 days from today
        dDate = dToday + timedelta(days=182)
        print2("182 day from today: " + str(dDate))
        print2(str(dDate) + " converted to  " + convert_date(dDate))
        
        # 181 days from today
        dDate = dToday + timedelta(days=181)
        print2("181 day from today: " + str(dDate))
        print2(str(dDate) + "  converted to  " + convert_date(dDate))
        
        
        iMin = -60
        iMax = 61
        
        while  iMin < iMax:
            dDate = date.today() + timedelta(days=iMin)
            print2(str(dDate) + "  converted to  " + convert_date(dDate))
            iMin +=1
        # end
        
        dDate = date.today()- timedelta(days=181)
        print2(str(dDate) + "  converted to  " + convert_date(dDate))
        
        dDate = date.today()- timedelta(days=182)
        print2(str(dDate) + "  converted to  " + convert_date(dDate))
        
        
    # end # End of testcase - test_Convert_Date_001_DateObjects
    
    
    #===========================================================================#
    # Testcase method: test_Convert_Date_002_DatesAsStrings
    #
    # Description: Test the method convert_date(...) with dates expressed as strings
    #===========================================================================#
    def test_Convert_Date_002_DatesAsStrings(self):
        
        #require 'date'
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Convert_Date_002_DatesAsStrings")
        print2("#######################")
        
        print2("Testing dates expressed as STRINGS\n\n")
        
        # LIST of date strings to test
        aDateStrings = [
                        "12/31/2000",
                        "1/1/01",
                        "01/02/01",
                        "1/3/1",
                        "1/4/01",
                        "1/5/01",
                        "1/6/01",
                        "2/1/01",
                        "3/1/01",
                        "4/1/01",
                        "5/1/01",
                        "6/1/01",
                        "7/1/01",
                        "8/1/01",
                        "9/1/01",
                        "10/1/01",
                        "11/1/01",
                        "12/1/01"
                    ]
        
        # Loop through the list, converting each date string
        for sDateString in aDateStrings:
            print2(sDateString + "  converted to  " + convert_date(sDateString))
        # end
        
    # end # End of testcase - test_Convert_Date_002_DatesAsStrings
    
    #===========================================================================#
    # Testcase method: test_Convert_Date_003_InvalidDatesAsStrings
    #
    # Description: Test the method convert_date(...) with invalid dates expressed as strings
    #===========================================================================#
    def test_Convert_Date_003_InvalidDatesAsStrings(self):
        
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Convert_Date_003_InvalidDatesAsStrings")
        print2("#######################")
        
        print2("Testing invalid dates expressed as STRINGS\n\n")
        
        sDateString = "6/31/08"
        print2("\nTrying an invalid month specific date")
        print2(sDateString + "  converted to  " + convert_date(sDateString))
        
        sDateString = "14/04/2010"
        print2("\nTrying an invalid month specific date")
        print2(sDateString + "  converted too  " + convert_date(sDateString))
        
        sDateString = "12-88-2010"
        print2("\nTrying an invalid date in any month")
        print2(sDateString + "  converted to  " + convert_date(sDateString))
        
        sDateString = "02/29/2001"
        print2("\nTrying an invalid Leap Year date")
        print2(sDateString + "  converted to  " + convert_date(sDateString))
        
    # end # End of testcase - test_Convert_Date_003_InvalidDatesAsStrings


# end of Class - UnitTest_Convert_Date

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_Convert_DateStrings)
unittest.TextTestRunner(verbosity=2).run(suite)