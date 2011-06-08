#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_isvalid_unittest.py
#
#  Copyright (c) 2008-2010, Joe DiMauro
#  All rights reserved.
#
# Description: Unit tests for WatirWorks methods:
#                       isValid_Password(...)
#                       isValid_EmailAddress?(...)
#                       sValid_ZipCode?(...)
#                       isValid_TopLevelDomain(...)
#=============================================================================#
#=============================================================================#
# Import section
# Entries for additional files or methods needed by this test
#=============================================================================#

import unittest
#from datetime import datetime # Add ability to get/format Dates

# PyWorks
#from PyWorks_Reflib import *    #  PyWorks Reference data module
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

global VERBOSE
VERBOSE = False

global DICTIONARY
DICTIONARY = ""

global PYTHONPATH
PYHTONPATH = ""

#=============================================================================#

#=============================================================================#
# Class: UnitTest_IsValid
#
#
# Test Case Methods: setUp, tearDown,
#                    test_001_isValid_Password
#                    test_002_isValid_ZipCode
#                    test_003_isValid_TopLevelDomain
#                    test_004_isValid_EmailAddress
#=============================================================================#
class UnitTest_IsValid (unittest.TestCase):

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
    # Testcase method: test_IsValid_001_Password
    #--
    #
    # Description: Test the methods:
    #                       isValid_Password(...)
    #===========================================================================#
    def test_IsValid_001_Password(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_IsValid_001_Password")
        print2("#######################")
        
        #VERBOSE=True
        
        # Define a LIST of zip codes to try
        aPasswords = [ 12345678, "pwd", "abcdefgh", "ABCDEFGH", "12345678", "Pass w0rd", "Pas&w0rd", "Passw0rd","123qweasdZXC", "MyPa55w0rd", "123456Az"]
        
        # Loop
        for sPassword in aPasswords:
            
            print2("\nPassword = " + str(sPassword))
            bIsValid = isValid_Password(sPassword)
            
            if(bIsValid == True): # Check validity
                print2("Valid")
            else:
                print2("Invalid")
            # end # Check validity
        # end Loop
        
    # End of test method - test_IsValid_001_Password
    
    
    #===========================================================================#
    # Testcase method: test_IsValid_002_ZipCode
    #--
    #
    # Description: Test the methods:
    #                       sValid_ZipCode?(...)
    #===========================================================================#
    def test_IsValid_002_ZipCode(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_IsValid_002_ZipCode")
        print2("#######################")
        
        #VERBOSE=True
        
        # Define a LIST of zip codes to try
        aZipCodes = [ "80021", "12345", "123456", "1", "1234",  "12345-1234", "12345-123", "00000" ]
        
        # Loop
        for sZipCode in aZipCodes:
           
            print2("\nZip Code = " + sZipCode)
            if(isValid_ZipCode(sZipCode) == True): # Check validity
                print2("Valid")
            else:
                print2("Invalid")
            # end # Check validity
        # end # Loop
        
        # End of test method - test_IsValid_002_ZipCode

    #===========================================================================#
    # Testcase method: test_IsValid_003_TopLevelDomain
    #--
    #
    # Description: Test the methods:
    #                       isValid_TopLevelDomain(...)
    #===========================================================================#
    def test_IsValid_003_TopLevelDomain(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_IsValid_003_TopLevelDomain")
        print2("#######################")
        
        #VERBOSE=True
        
        #sTopLevelDomains = "com"
        
        # Define a LIST of TLD's to try
        sTopLevelDomains = [ "COM", "com", "biz", "gov", "net", "org", "de", "museum", "travel", "d", "bizz", "xyv", "123" ]
        
        # Loop
        for sTLD in sTopLevelDomains:
            
            print2("\nTop Level Domain = " + sTLD)
            
            if(isValid_TopLevelDomain(sTLD) == True): # Check validity
                print2("Valid")
            else:
                print2("Invalid")
            # end # Check validity
        # end # Loop
        
        
    # End of test method - test_IsValid_003_TopLevelDomain

    #===========================================================================#
    # Testcase method: test_IsValid_004_EmailAddress
    #--
    #
    # Description: Test the methods:
    #                       isValid_EmailAddress?(...)
    #===========================================================================#
    def test_IsValid_004_EmailAddress(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_IsValid_004_EmailAddress")
        print2("#######################")
        
        #VERBOSE=True
        
        # Define a LIST of email addresses to try
        sEmailAddresses = [ "emailaddress.com", "1@3.5", "me@server.com", "you@yourserver.gov", "me@123.xyz", "$5@_#.xyz"]
        
        # Loop
        for sAddress in sEmailAddresses:
            
            print2("\nEmail Address = " + sAddress)
            if(isValid_EmailAddress(sAddress) == True): # Check validity
                print2("Valid")
            else:
                print2("Invalid")
            #end # Check validity
        #end # Loop
        
    # End of test method - test_IsValid_004_EmailAddress
    
    
# end of Class - UnitTest_IsValid

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_IsValid)
unittest.TextTestRunner(verbosity=2).run(suite)