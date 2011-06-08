#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_integer_unittest.py
#
#  Copyright (c) 2008-2011, Joe DiMauro
#  All rights reserved.
#
# Description: Unit tests for PyWorks INTEGER methods:
#                 ordinal()
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by this test
#=============================================================================#


import unittest
#from datetime import date, datetime # Add ability to get/format Dates

# PyWorks
#from PyWorks_Reflib import *       #  PyWorks Reference data module
from PyWorks_Utilities import *    # PyWorks General Utilities

#=============================================================================#
# Global Variables section
# Set global variables that will be inherited by each of the test files
#=============================================================================#

# Java global variables
#

# PyWorks global variables
#
sRun_TestType = "ready"
iRun_TestLevel = 0
VERBOSE = False
#=============================================================================#
#=============================================================================#
# Class: UnitTest_Integer
#
#
# Test Case Methods: setUp, tearDown
#                    test_Integer_001_ordinal
#
#
#=============================================================================#
class UnitTest_Integer(unittest.TestCase):
    
    
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
    
    # end of setUp

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
    # Testcase method: test_Integer_001_ordinal
    #
    # Description: Test the INTEGER method ordinal()
    #===========================================================================#
    def test_Integer_001_ordinal(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Integer_001_ordinal")
        print2("#######################")
        
        # Print the Ordinal values from iMin to iMax
        iMin = -1
        iMax = 21
        while iMin < iMax:
            print2(str(iMin) + " has an ordinal of " + ordinal(iMin))
            #print2(str(iMin) + " has an ordinal of " + int(iMin).ordinal())
            iMin = iMin + 1
        # end 
        iMin = 100
        iMax = 121
        while iMin < iMax:
            print2(str(iMin) + " has an ordinal of " + ordinal(iMin))
            #print2(str(iMin) + " has an ordinal of " + int(iMin).ordinal())
            iMin = iMin + 1
    # End of test method - test_Integer_001_ordinal

# end of Class - UnitTest_Integer

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_Integer)
unittest.TextTestRunner(verbosity=2).run(suite)