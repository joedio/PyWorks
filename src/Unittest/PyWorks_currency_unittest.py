#!/usr/bin/python
#### -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
#--
#=============================================================================#
# File: PyWorks_currency_unittest.py
#
#  Copyright (c) 2008-2011, Joe DiMauro
#  All rights reserved.
#
# Description: Unit tests for PyWorks methods:
#                  format_to_currency(...)
#                  format_from_currency(...)
#
#
#
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by this test
#=============================================================================#

import unittest
#from datetime import datetime #Add ability to get/format Dates

# PyWorks
#from PyWorks_Reflib import *       #  PyWorks Reference data module
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
# Class: UnitTest_Currency
#
#=============================================================================#
class UnitTest_Currency(unittest.TestCase):

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
    # End
    
    
    #===========================================================================#
    # Testcase method: test_Currency_001_Format_To_Amount
    #
    # Description: Tests PyWorks method: format_to_currency(...)
    #                   Attempts to convert strings to amounts
    #===========================================================================#
    def test_Currency_001_CommaDelimit(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Currency_001_CommaDelimit")
        print2("#######################")
        
        
        fFloatsToDelimit = [1.00, 12.00, 123.00, 1234.00, 12345.00, 123456.00, 1234567.00,12345678.1234, 0.000000]
        
        for fFloat in fFloatsToDelimit:
            sFloat = comma_delimit(fFloat, ",")
            print2("Delimited: " + str(fFloat) + " to: " + str(sFloat))
        # end
           
        # end convert_StringToCurrency
        
    # End of test method - test_Currency_001_CommaDelimit
    
    #===========================================================================#
    # Testcase method: test_Currency_002_Format_To_Amount
    #
    # Description: Tests PyWorks method: format_to_currency(...)
    #                   Attempts to convert strings to amounts
    #===========================================================================#
    def test_Currency_002_Format_To_Amount(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Currency_002_Format_To_Amount")
        print2("#######################")
            
        ############################
        sThisTaskName = "1000 to $1,000.00"
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency("1000")
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "1000 to £1.000.00"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency("1000", "£", ".")
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "  1000   to 1.000.00"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency("  1000  ", "", ".")
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "1000.5 to $1,000.50"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency("1000.5")
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "1.1 to $1.10"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency("1.1")
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "1 to $1.00"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency("1")
        
        print2("Formatted value = " + sConvertedValue)
        
        ############################
        sThisTaskName = ".01 to $0.01"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency(".01")
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = ".1 to $0.10"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency(".1")
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "1. to $1.00"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency("1.")
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "1000000.99 to 1,000,000.99"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency("1000000.99","", ",")
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "1000000.99 to £1.000.000.99"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency("1000000.99", "£", ".")
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "1000000.99 to ¥1:000:000.99"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency("1000000.99", "¥", ":")
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "0.99 to $0.99"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency("0.99", "$", ",")
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "0.999 to $1.00"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_to_currency("0.999", "$", ",")
        print2("Formatted value = " + sConvertedValue)
        ############################
            
        # end convert_StringToCurrency
            
    # End of test method - test_Currency_002_Format_To_Amount
    
    
    
    #=============================================================================#
    # Testcase method: test_Currency_002_Format_From_Amount
    #
    # Description: Tests PyWorks method: format_from_currency(...)
    #                    Attempts to convert amounts to strings
    #=============================================================================#
    def test_Currency_003_Format_From_Amount(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Currency_003_Format_From_Amount")
        print2("#######################") 
            
        ############################
        sThisTaskName = "$1,000 to 1000"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_from_currency("$1,000", "$", ",", True)
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "$1,000,000.00 to 1000000.00"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_from_currency("$1,000,000.00", "$", ",", False)
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "£1.000.50 to 1000"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_from_currency("£1.000.50", "£", ".", True)
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "$1.000.5 to 1000.50"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_from_currency("$1.000.5", "$", ",", False)
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "$1,000,000.50 to $1000000"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_from_currency("$1,000,000.50", "", ",",True)
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "¥1,000,000.5 to 1000000.50"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_from_currency("¥1,000,000.5","¥", ",", False)
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "0.5 to 0.50"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_from_currency("0.5","", ",", False)
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = ".5 to 0.50"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_from_currency(".5","", ",", False)
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "$1. to 1.00"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_from_currency("$1.","$", ",", False)
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        sThisTaskName = "$. to 0.00"
        print2("")
        print2(" # BEGIN: " + sThisTaskName + " #")
        
        sConvertedValue = format_from_currency("$.","$", ",", False)
        
        print2("Formatted value = " + sConvertedValue)
        ############################
        
        # end  convert_StringFromCurrency
        
    # End of test method - test_Currency_003_Format_From_Amount
    

# end of Class - UnitTest_Currency


suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_Currency)
unittest.TextTestRunner(verbosity=2).run(suite)
