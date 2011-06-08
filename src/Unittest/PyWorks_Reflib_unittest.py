#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_Reflib_unittest.py
#
#  Copyright (c) 2008-2010, Joe DiMauro
#  All rights reserved.
#
# Description:  The PyWorks Reference Library's unit test
#
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by this test
#=============================================================================#

import unittest                      # Jython Unit Test Framework
#from datetime import date, datetime  # Add ability to get/format Dates

# PyWorks
from PyWorks_Reflib import *    #  PyWorks Reference data module
from PyWorks_Utilities import *        # PyWorks General Utilities
from test.test_support import sortdict
#=============================================================================#

#=============================================================================#
# Global Variables section
# Set global variables that will be inherited by each of the test files
#=============================================================================#

# PyWorks global variables
#
sRun_TestType = "ready"
iRun_TestLevel = 0
VERBOSE = False
DICTIONARY = ""


#=============================================================================#


#=============================================================================#
# Class: UnitTest_RefLib
#
#
# Test Case Methods: setup, teardown
#                   test_Year
#
#
#=============================================================================#
class UnitTest_RefLib(unittest.TestCase):

    #===========================================================================#
    # Method: setUp
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

    # end of setUp

    #===========================================================================#
    # Method: tearDown
    #
    # Description: After every testcase Test::Unit runs tearDown
    #===========================================================================#
    def tearDown(self):

        print2("Testcase finished in " + calc_elapsed_time(tTestCase_StartTime) + " (h:m:s.ms)")

        # Restore the Global variable's original settings
        VERBOSE = VERBOSE_ORIG
        DICTIONARY = DICTIONARY_ORIG
        
        #print2("tearDown")

    # end of tearDown
    #'''
    #===========================================================================#
    # Method: runTest
    #
    # Description: The list of tests to run
    #===========================================================================#
    def runTest(self):
        """ List of tests to run """
        self.test_RefLib_001_Dates()
        self.test_RefLib_002_States()
        self.test_RefLib_003_Streets()
        self.test_RefLib_004_Months()
        self.test_RefLib_005_TopLevelDomains()
    #'''
    
    #===========================================================================#
    # Testcase method: test_RefLib_001_Dates
    #
    # Description: Test the Reference date values
    #=============================================================================#
    def test_RefLib_001_Dates(self):
        print2("")
        print2("#######################")
        print2("Testcase: test_RefLib_001_Dates")
        print2("#######################")
        print2("")
        print2(" This year is " + THIS_YEAR + ", a.k.a. '" + THIS_YR)
        print2(" Next year is " + NEXT_YEAR + ", a.k.a. '" + NEXT_YR)
        print2(" Last year was " + LAST_YEAR + ", a.k.a. '" + LAST_YR)
        print2(" It's month nunber " + THIS_MONTH)
        print2(" It's day " + THIS_DAY + " of the month")
        
        print2(" TODAY \t " + TODAY)
        print2(" TOMORROW \t " + TOMORROW)
        print2(" YESTERDAY \t " + YESTERDAY)
        
        print2(" DAYS_FUTURE_7 \t " + DAYS_FUTURE_7)
        print2(" DAYS_FUTURE_30 \t " + DAYS_FUTURE_30)
        print2(" DAYS_FUTURE_60 \t " + DAYS_FUTURE_60)
        print2(" DAYS_FUTURE_90 \t " + DAYS_FUTURE_90)
        print2(" DAYS_FUTURE_365 \t " + DAYS_FUTURE_365)
        
        print2(" DAYS_PAST_7 \t" + DAYS_PAST_7)
        print2(" DAYS_PAST_30 \t " + DAYS_PAST_30)
        print2(" DAYS_PAST_60 \t " + DAYS_PAST_60)
        print2(" DAYS_PAST_90 \t " + DAYS_PAST_90)
        print2(" DAYS_PAST_365 \t " + DAYS_PAST_365)
        
        print2(" WEEKS_FUTURE_1 \t " + WEEKS_FUTURE_1)
        print2(" WEEKS_FUTURE_2 \t " + WEEKS_FUTURE_2)
        print2(" WEEKS_FUTURE_4 \t " + WEEKS_FUTURE_4)
        print2(" WEEKS_FUTURE_8 \t " + WEEKS_FUTURE_8)
        print2(" WEEKS_FUTURE_12 \t " + WEEKS_FUTURE_12)
        print2(" WEEKS_FUTURE_52 \t " + WEEKS_FUTURE_52)
        
        print2(" WEEKS_PAST_1 \t " + WEEKS_PAST_1)
        print2(" WEEKS_PAST_2 \t " + WEEKS_PAST_2)
        print2(" WEEKS_PAST_4 \t " + WEEKS_PAST_4)
        print2(" WEEKS_PAST_8 \t " + WEEKS_PAST_8)
        print2(" WEEKS_PAST_12 \t " + WEEKS_PAST_12)
        print2(" WEEKS_PAST_52 \t " + WEEKS_PAST_52)
        
    
    # End of test method - test_RefLib_001_Dates
    
    
    #===========================================================================#
    # Testcase method: test_RefLib_002_States
    #
    # Description: Test the Reference State values
    #===========================================================================#
    def test_RefLib_002_States(self):
        print2("")
        print2("#######################")
        print2("Testcase: test_RefLib_002_States")
        print2("#######################")
        print2("")
        print2("Canadian Provinces")
        for key, value in CANADIAN_PROVINCES.iteritems():
            print2(" Abbreviation " + key + ", is " + value)
        # end
        
        print2("")
        print2("Mexican States")
        for key, value in MEXICAN_STATES.iteritems():
            print2(" Abbreviation " + key + ", is " + value)
        # end
        
        print2("")
        print2("USPS States")
        for key, value in USPS_STATES.iteritems(): 
            print2(" Abbreviation " + key + ", is " + value)
        # end
    # End of test method - test_RefLib_002_States
      
    #===========================================================================#
    # Testcase method: test_RefLib_003_Streets
    #
    # Description: Test the Reference address values
    #===========================================================================#
    def test_RefLib_003_Streets(self):
        "Test the Reference address values"
        print2("")
        print2("#######################")
        print2("Testcase: test_RefLib_003_Streets")
        print2("#######################")
        
        print2("")
        print2("USPS Street Suffix")
        for key, value in USPS_STREET_SUFFIX.iteritems():
            print2(" Abbreviation " + key + ", is " + value)
        # end
        
        print2("")
        print2("USPS Secondary Unit Designators")
        for key, value in USPS_SECONDARY_UNIT_DESIGNATOR.iteritems(): 
            print2(" Abbreviation " + key + ", is " + value)
        # end
        
    # End of test method - test_RefLib_003_Streets
    
    #=============================================================================#
    # Testcase method: test_RefLib_004_Months
    #
    # Description: Test the Reference month values
    #===========================================================================#
    def test_RefLib_004_Months(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_RefLib_004_Months")
        print2("#######################")
    
        print2("")
        print2("Months")
        for key, value in MONTH_ABBREVIATION.iteritems(): 
            print2(" Abbreviation " + key + ", is " + value)
        # end
        
    # End of test method - test_RefLib_004_Months
    
    #===========================================================================#
    # Testcase method: test_RefLib_005_TopLevelDomains
    #
    # Description: Test the Reference Top Level Domain values
    #===========================================================================#
    def test_RefLib_005_TopLevelDomains(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_RefLib_005_TopLevelDomains")
        print2("#######################")
        
        print2("")
        print2("Valid Top Level Domains:")
        for tld in TOP_LEVEL_DOMAINS:
            print2(tld)
        # end 
    # End of test method - test_RefLib_005_TopLevelDomains


    #=============================================================================#
    # Testcase method: test_RefLib_006_Countries
    #
    # Description: Test the Reference Country 2-Character values
    #===========================================================================#
    def test_RefLib_006_Countries(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_RefLib_006_Countries")
        print2("#######################")
        
        print2("")
        print2("Countries 2-Char")
        for key, value in COUNTRY_CODES_2CHAR.iteritems(): 
            print2(" Abbreviation " + key + ", is " + value)
        # end
        
        print2("-"*20)
        
        print2("")
        print2("Countries 3-Char")
        for key, value in COUNTRY_CODES.iteritems(): 
            print2(" Abbreviation " + key + ", is " + value)
        # end
    # End of test method - test_RefLib_006_Countries
    
    
# End of Class - UnitTest_RefLib

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_RefLib)
unittest.TextTestRunner(verbosity=2).run(suite)

# End of file - PyWorks_Reflib_unittest.py
