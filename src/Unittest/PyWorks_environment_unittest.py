#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_environment_unittest.py
#
#  Copyright (c) 2008-2011, Joe DiMauro
#  All rights reserved.
#
# Description: Unit tests for PyWorks methods:
#                display_java_env()
#                display_jython_env()
#                display_PyWorks_env()
#                find_tmp_dir()
#                is_win()
#                is_win32()
#                is_win64()
#                is_linux()
#                is_osx()
#                is_SOATest()
#                printenv(...)
#                get_env(...)
#                set_env(...)
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by this test
#=============================================================================#


import unittest
#from datetime import date, datetime # Add ability to get/format Dates

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
# Class: UnitTest_Enviroment
#
# Test Case Methods: setup, teardown
#                    test_Enviroment_001_showJavaEnv
#                    test_Enviroment_002_isPlatform
#                    test_Enviroment_003_showPyWorksEnv
#                    test_Enviroment_004_SortMethods
#                    test_Enviroment_005_PrintEnv
#                    test_Enviroment_006_GetEnv
#                    test_Enviroment_007_SetEnv
#
#=============================================================================#
class UnitTest_Environment(unittest.TestCase):

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
        
        #self.test_String_001_wordcount()
        pass
    # End
    
    #===========================================================================#
    # Testcase method: test_Enviroment_001_showJavaEnv
    #
    # Description: Test the methods: display_java_env()
    #                                             display_jython_env()
    #                                             find_tmp_dir()
    #===========================================================================#
    def test_Enviroment_001_showJavaEnv(self):

        print2("")
        print2("#######################")
        print2("Testcase: test_Enviroment_001_showJavaEnv")
        print2("#######################")

        print2("\nTest - display_Java_env")
        # Record info on the Java Environment
        display_java_env()  # Record output

        print2("\n\nTest - display_jython_env")
        display_jython_env()


        print2("\n\nTest - find_tmp_dir")
        print2("TMP is set to: " + find_tmp_dir())

    # end # Unit test - test_Enviroment_001_showJavaEnv


    #===========================================================================#
    # Testcase method: test_Enviroment_002_isPlatform
    #
    # Description: Test the methods
    #                is_win()
    #                is_win32()
    #                is_win64()
    #                is_linux()
    #                is_osx()
    #                #get_registered_ie_version()
    #                #is_ie6_registered?()
    #                #is_ie7_registered?()
    #                #is_ie8_registered?()
    #                #get_registered_firefox_version()
    #                #is_firefox2_registered?()
    #                #is_firefox3_registered?()
    #
    #===========================================================================#
    def test_Enviroment_002_isPlatform(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_Enviroment_002_isPlatform")
        print2("#######################")
        
        print2("Running on Windows: " + str(is_win()))
        print2("Running on Windows 32-bit: " + str(is_win32()))
        print2("Running on Windows 64 bit: " + str(is_win64()))
        print2("Running on Linux: " + str(is_linux()))
        print2("Running on OS/X: " + str(is_osx()))
        
        if(is_win() == True):
            pass
            '''
            print2("\nRegistered IE version: " + get_registered_ie_version())
            print2("Is IE6: " + str(is_ie6_installed()))
            print2("Is IE7: " + str(is_ie7_installed()))
            print2("Is IE8: " + str(is_ie8_installed()))
            
            print2("\nRegistered Firefox version: " + get_registered_firefox_version())
            print2("Is FF2: " + str(is_firefox2_installed()))
            print2("Is FF3: " + str(is_firefox3_installed()))
            '''
        # end

        #end # Unit test - test_Enviroment_002_isPlatform

    #===========================================================================#
    # Testcase method: test_Enviroment_003_showPyWorksEnv
    #
    # Description: Test the method - display_PyWorks_env()
    #===========================================================================#
    def test_Enviroment_003_showPyWorksEnv(self):

        print2("")
        print2("#######################")
        print2("Testcase: test_Enviroment_003_showPyWorksEnv")
        print2("#######################")

        # Record info on the PyWorks Environment
        display_PyWorks_env() # Record output
    # end # Unit test - test_Enviroment_003_showPyWorksEnv


    #===========================================================================#
    # Testcase method: test_Enviroment_004_SOATest
    #
    # Description: Test is_SOATest
    #===========================================================================#
    def test_Enviroment_004_SOATest(self):

        print2("")
        print2("#######################")
        print2("Testcase: test_Enviroment_004_SOATest")
        print2("#######################")
        
        print2("Running on SOATest: " + str(is_SOATest()))
        
        print2("######################")

    # end # End of test method - test_Enviroment_004_SOATest


    #===========================================================================#
    # Testcase method: test_Enviroment_005_GetEnv
    #
    # Description: Test OS environment variables using get_env(...)
    #===========================================================================#
    def test_Enviroment_005_GetEnv(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Enviroment_005_GetEnv")
        print2("#######################")
        
        sEnvVarName = "COMPUTERNAME" # Is this one platform independent?
        
        print2("")
        print2("Retrieve all OS variables using get_env()")
        hMyEnvVars = get_env() # Get them all
        
        # Loop through the DICT and display each variable name and its setting
        for key, value in hMyEnvVars.iteritems():
            print2(" OS variable: " + str(key) + " is set to " + (str(value)))
            #print2(" OS variable: " + key + " is set to " + hMyEnvVars(key))
        # end
        
        print2("")
        print2("Retrieve a specific OS variable using get_env")
        hMyEnvVars = get_env(sEnvVarName)
        
        # Loop through the DICT and display each variable name and its setting
        for key, value  in hMyEnvVars.iteritems():
            print2(" OS variable: " + str(key) + " is set to " + (str(value)))
        # end

    # END Testcase - test_Enviroment_005_GetEnv

    #===========================================================================#
    # Testcase method: test_Enviroment_006_PrintEnv
    #
    # Description: Test OS environment variables using printenv(...)
    #===========================================================================#
    def test_Enviroment_006_PrintEnv(self):

        print2("")
        print2("#######################")
        print2("Testcase: test_Enviroment_006_PrintEnv")
        print2("#######################")
        
        print2("")
        print2(" Display current settings of some OS variables using printenv()...")
        printenv("BOGUS_ENVVAR")
        printenv("COMPUTERNAME") # Is this one platform independent?
        printenv("USERDNSDOMAIN") # Is this one platform independent?
        printenv("NUMBER_OF_PROCESSORS") # Is this one platform independent?
        printenv("OS") # Is this one platform independent?
        printenv("PROCESSOR_IDENTIFIER") # Is this one platform independent?
        #printenv("SHELL") # Is this one platform independent? Yes on: Ubuntu,
        printenv("USERNAME") # Is this one platform independent? Yes on: Win, Ubuntu
        
        print2("")
        print2("")
        print2(" Display current settings of ALL OS variables using printenv()...")
        printenv(None)
        
    # END Testcase method - test_Enviroment_006_PrintEnv

    #===========================================================================#
    # Testcase method: test_Enviroment_007_SetEnv
    #
    # Description: Test setting an OS environment variable using set_env(...)
    #===========================================================================#
    def test_Enviroment_007_SetEnv(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Enviroment_007_SetEnv")
        print2("#######################")
        
        sEnvVarName = "COMPUTERNAME" # Is this one platform independent?
        sNewValue = "MyNewName"
        
        # Display the current value
        print2("Current value of " + sEnvVarName)
        printenv(sEnvVarName)
        
        print2(" Setting " + sEnvVarName + " to " + sNewValue)
        
        # Set new value that will be in effect for duration of this session's test run
        set_env(sEnvVarName, sNewValue)
         
        # Display the current value
        print2("Current value of " + sEnvVarName + " is now")
        printenv(sEnvVarName)
        
    
        sNewEnvVarName = "Jython"
        sNewSetting = "Loves whitespace"
        print2(" Setting a new Environment Variable " + sNewEnvVarName + " to a new setting " + sNewSetting)
        
        # Set new value that will be in effect for duration of this session's test run
        set_env(sNewEnvVarName, sNewSetting)
        
        # Display the current value
        print2("Current value of " + sNewEnvVarName + " is now")
        printenv(sNewEnvVarName)
       
    # END Testcase method - test_Enviroment_007_SetEnv

    #===========================================================================#
    # Testcase method: test_Enviroment_008_PyWorks_install_path
    #
    # Description: Test method: PyWorks_install_path()
    #===========================================================================#
    def test_Enviroment_008_PyWorks_install_path(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Enviroment_008_PyWorks_install_path")
        print2("#######################")
        
        sPyWorks_InstallPath = get_PyWorks_install_path()
        print2("PyWorks install path: " + sPyWorks_InstallPath)
        
    # END Testcase method - test_Enviroment_008_PyWorks_install_path

# END - Class - UnitTest_Enviroment

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_Environment)
unittest.TextTestRunner(verbosity=2).run(suite)