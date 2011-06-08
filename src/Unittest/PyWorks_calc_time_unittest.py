#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_calc_time_unittest.py
#
#  Copyright (c) 2008-2011, Joe DiMauro
#  All rights reserved.
#
# Description: Unit test for time calculations. Tests method:
#                calc_elapsed_time(...)
#                Exercises various methods to show their flexibility
#                to manipulate Dates as Strings
#
# Test cases:    UnitTest_CalcTime
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by this test
#=============================================================================#

import unittest
#from datetime import date, datetime # Add ability to get/format Dates
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
# Class: UnitTest_CalcTime
#
#
# Test Case Methods: setUp, tearDown
#                   test_Year
#
#
#=============================================================================#
class UnitTest_CalcTime(unittest.TestCase):


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
        #print2("SetUp")
        
    # # end of setUp

    #===========================================================================#
    # Method: teardown
    #
    # Description: After every testcase Test::Unit runs teardown
    #===========================================================================#
    def tearDown(self):
        
        print2("Testcase finished in " + calc_elapsed_time(tTestCase_StartTime) + " (h:m:s.ms)")
        
        # Restore the Global variable's original settings
        VERBOSE = VERBOSE_ORIG
        DICTIONARY = DICTIONARY_ORIG
        
        #print2("tearDown")
        
    # end of tearDown
    
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
    # Testcase method: test_CalcTime_001_CalcElapsedTime
    #
    # Description: Tests method calc_elapsed_time(...)
    #===========================================================================#
    def test_CalcTime_001_CalcElapsedTime(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_CalcTime_001_CalcElapsedTime")
        print2("#######################")
        
        # Activate the Verbose flag during this test and
        # use the methods verbose statements for output
        #$VERBOSE = true
        
        tStartTime = datetime.now()
        
        print2("Start time = " + str(tStartTime))
        
        time.sleep(2)
        print2("Elapsed time = " + calc_elapsed_time(tStartTime))
        
        time.sleep(3)
        print2("Elapsed time = " + calc_elapsed_time(tStartTime))
        
    # End of test method - test_CalcTime_001_CalcElapsedTime
    
    
    #===========================================================================#
    # Testcase method: test_CalcTime_002_CalcYear
    #
    # Description: Exercises various methods to show
    #              their flexibility to manipulate Dates as Strings
    #===========================================================================#
    def test_CalcTime_002_CalcYear(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_CalcTime_002_CalcYear")
        print2("#######################")
        
        # String holding 4-character year
        sCurrentYear = str(datetime.now().year)
        
        # Another string holding a different 4-character year
        sNextYear = str(date.today().year + 1)
        
        print2("")
        print2("This year string = " + sCurrentYear)
        print2("Next year string = " + sNextYear)
        
        sTHIS_YEAR_YY = sCurrentYear[2:4]
        print2("")
        print2("This year string [yy] = " + sTHIS_YEAR_YY)
        
        iCurrentYear = int(sCurrentYear)
        iNextYear = int(sNextYear)
        
        print2("")
        print2("This year integer to string = " + str(iCurrentYear))
        print2("This Year as an integer: ...")
        print2(iCurrentYear)
        
        print2("Next year integer to string = " + str(iNextYear))
        print2("Next Year as an integer...")
        print2(iNextYear)
        
        iCalculatedYear_plus1 = iCurrentYear + 1
        iCalculatedYear_minus1 = iCurrentYear - 1
        
        print2("")
        print2("This year integer plus 1 year = " + str(iCalculatedYear_plus1))
        print2("This year integer minus 1 year = " + str(iCalculatedYear_minus1))
        
        #######################
        
        iVariance = 1
        
        while iVariance < 10:
            
            print2("")
            print2("This year integer plus " + str(iVariance) + " years = " + str(iCurrentYear + iVariance))
            print2("This year integer minus " + str(iVariance) + " years = " + str(iCurrentYear - iVariance))
            print2("")
            print2("This year string plus " + str(iVariance) + " years = " + str(int(sCurrentYear) + iVariance))
            print2("This year string minus " + str(iVariance) + " years = " + str(int(sCurrentYear) - iVariance))
            
            iVariance = iVariance + 1
            
        # end
        
        if(iCurrentYear > iNextYear):
            print2("The current year integer is larger than the next year integer")
        else:
            print2("The next year is integer is larger than the Current year integer")
        # end
        
        if(sCurrentYear > sNextYear):
            print2("The current year string is larger than the next year string")
        else:
            print2("The next year is string larger than the Current year string")
        # end
        ##########################
        
    # end # End of test method - test_CalcTime_002_CalcYear

#===========================================================================#
    # Testcase method: test_CalcTime_003_calc_datestrings
    #
    # Description: Tests method calc_datestrings(...)
    #===========================================================================#
    def test_CalcTime_003_calc_datestrings(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_CalcTime_003_calc_datestrings")
        print2("#######################")
        
        # Activate the Verbose flag during this test and
        # use the methods verbose statements for output
        #$VERBOSE = true
        
        tStartTime = datetime.now()
        
        print2("Start time = " + str(tStartTime))
        
        # Define the dictionary
        hCalculatedDateStrings = calc_datestrings()
        
        # Loop through the sorted Dictionary
        for key, value in hCalculatedDateStrings.iteritems():
            # Display each key and its value
            print2(key + "\t = '" + value + "'")
        # end
        
        print2("The date-string for 30 days ago is '" + hCalculatedDateStrings["DAYS_PAST_30"] +"'")
    # End of test method - test_CalcTime_003_calc_datestrings
    
# end of Class - UnitTest_CalcTime
    
suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_CalcTime)
unittest.TextTestRunner(verbosity=2).run(suite)