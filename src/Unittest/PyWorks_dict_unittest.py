#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_dict_unittest.py
#
# Description: Unit tests for PyWorks DICT methods:
#                   invertDict()
#                   getMatchingKeyValue(...)
#                   
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by this test
#=============================================================================#

import unittest
#from datetime import datetime # Add ability to get/format Dates

# PyWorks
from PyWorks_Reflib import *    #  PyWorks Reference data module
from PyWorks_Utilities import *    # PyWorks General Utilities
#=============================================================================#

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

global DICTIONARY
DICTIONARY = ""

global PYTHONPATH
PYHTONPATH = ""

#=============================================================================#


#=============================================================================#
# Class: UnitTest_String
#
#
# Test Case Methods: setUp, tearDown
#
#
#
#=============================================================================#
class UnitTest_Dict(unittest.TestCase):

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

    #===========================================================================#
    # Method: runTest
    #
    # Description: The list of tests to run
    #===========================================================================#
    def runTest(self):
        """ List of tests to run """
        pass
    

   
    #===========================================================================#
    # Testcase method: test_Dict_001_InvertDict
    #
    # Description: Test the method invertDict()
    #===========================================================================#
    def test_Dict_001_InvertDict(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_Dict_001_InvertDict")
        print2("#######################")
    
    # Define a DICT of STRING pairs
    hBeatles = { "John" : "Lennon",
                "Paul" : "McCartney",
                "George" : "Harrison",
                "Ringo" : "Star"
                }
    print2("Original Dictionary...")
    print2(hBeatles)
    
    hBeatlesInverted = invertDict(hBeatles)
    print2("\nInverted  Dictionary...")
    print2(hBeatlesInverted)
    
    
    # Define a DICT of INT and STRING pairs
    hNumbers = { 1 : "One",
                2 : "Two",
                3 : "Three",
                4 : "Four"
                }
    print2("\n\nOriginal Dictionary...")
    print2(hNumbers)
    
    hNumbersInverted = invertDict(hNumbers)
    print2("\nInverted  Dictionary...")
    print2(hNumbersInverted)
    
    # End of test method - test_Dict_001_InvertDict

    #===========================================================================#
    # Testcase method: test_Dict_002_getMatchingKeyValue
    #
    # Description: Test the method getMatchingKeyValue()
    #===========================================================================#
    def test_Dict_002_getMatchingKeyValue(self):
        
        '''
        Returns the value of the first matching key from a DICT   
        '''
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Dict_002_getMatchingKeyValue")
        print2("#######################")
        
        if(VERBOSE == True):
            pass
        # end
        
        hDictToSearch = USPS_STATE_ABBREVIATION
        aKeysToSearch = ["Nebraska", "Nebr", "nebr", "aska", "NEBR", "ASKA", "Iowa", "IOWA", "iowa", "Io", "wa"]
        
        for sKeyToMatch in aKeysToSearch:
            
            aMatch = getMatchingKeyValue(hDictToSearch, sKeyToMatch, True)
            
            print2("Case sensitive search for Key '" + sKeyToMatch + "' found " + aMatch[0] + ", with value of " + aMatch[1] )
        # end
        print2("-"*15)
        
        for sKeyToMatch in aKeysToSearch:
            
            aMatch = getMatchingKeyValue(hDictToSearch, sKeyToMatch, False)
            
            print2("Case insensitive search for Key '" + sKeyToMatch + "' found " + aMatch[0] + ", with value of " + aMatch[1] )
        # end
        
    # end test_Dict_002_getMatchingKeyValue()



# End of class - UnitTest_Dict

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_Dict)
unittest.TextTestRunner(verbosity=2).run(suite)
