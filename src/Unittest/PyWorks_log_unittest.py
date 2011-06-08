#--
#=============================================================================#
# File: PyWorks_log_unittest.py
#
#
#  Copyright (c) 2008-2011, Joe DiMauro
#  All rights reserved.
#
# Description: Unit tests for the IE browser using WatirWorks methods:
#
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by this test
#=============================================================================#

import unittest
#from datetime import date, datetime, timedelta # Add ability to get/format Dates
#import time                    # Add ability to get/format Time
#import logging                  # Add ability to log messages to a file



# PyWorks
from PyWorks_Reflib import *       # PyWorks Reference data module
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
sRun_TestType = "not_soatest_compatable"
iRun_TestLevel = 0
VERBOSE = False
#=============================================================================#
# Define a custom error class
#
# The def's in this class are used by test_Log_03_ForcedError
# They are define here an an example of how to write a custom error class
# that can be used by other test cases.
#
# For more info see: http://docs.python.org/tutorial/errors.html
###################################
class PyWorksError(Exception):
    def __init__(self, value):
        self.value = value
    # End
    def __str_(self):
        return repr(self.value)
    # end
# end

#=============================================================================#
# Class: UnitTest_Browser_IE
#
# Test Case Methods: setUp, tearDown
#
#
#=============================================================================#
class UnitTest_Log(unittest.TestCase):


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
        #print2("SetUp")
        
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
        
    # # # end of tearDown
    
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
    # Testcase method: test_WIP
    #
    # Description: Test the method: capture_results(...)
    #
    #===========================================================================#
    def test_Log_01_capture_results(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Log_01_capture_results")
        print2("#######################")
        
        # Start a new Logger Object and assign it to a Global Object
        #
        # Using the default values:
        #   Create a "PyWorks/results" directory within the OS's Temporary directory
        #   This directory will contain the single log file used for all tests.
        #   Then create a Global Logger Object to manage that log file.
        global oLogger
        oLogger = capture_results()
        oLogger.info("Logging an entry from test case: test_Log_01_capture_results")
        
        # Try it again, but specify values intead of relying on the defaults
        # Should be ignored, as the Global Logger Object pre-exists. You only get one, Hey its global!
        #oLogger = capture_results(True, "results", "logfile")
        
        # Try it again, but specify other values intead of relying on the defaults
        # Should be ignored, as the Global Logger Object pre-exists. You only get one, Hey its global!
        #oLogger = capture_results(false, "bad_results", "bogus_logfile")
        
    # END testcase - test_Log_01_capture_results
    
    #===========================================================================#
    # Testcase method: test_Log_02_print
    #
    # Description: Test the method: puts2(...)
    #                               is_global_var_set(...)
    #
    #===========================================================================#
    def test_Log_02_print(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Log_02_print")
        print2("#######################")
        
        # Write only to stdout using print2()
        print2("Message sent only to stdout via print2().")
        
        # Get the PyWorks logger object
        oLogger = logging.getLogger("PyWorks")
        
        # Continue test only if a global logger (oLogger) exists
        # Presume it exists if it is NOT None
        if(oLogger):
            
            # Write to the log file using log()
            oLogger.info("Message logged from: test_Log_02_print")
            
            # Write to the log file and stdout, with Logger level set to INFO
            print2(" Informational message sent to the log file and STDOUT.")
            print2(" Second informational message sent to the log file and STDOUT.", "INFO")
            print2(" Debug message suppressed in the log file but sent to STDOUT.", "DEBUG")
            print2(" Warning message sent to the log file and STDOUT.", "WARN")
            print2(" Critical message sent to the log file and STDOUT.", "CRITICAL")
            print2(" Mystery message sent to the log file and STDOUT.", "WXYZ")
            
            print2(" Message sent ONLY to the log file.", "INFO", -1)
            print2(" Message sent ONLY to STDOUT.", "INFO", 0)
            
        else:
            print2("*** WARNING - No Global logger named oLogger found")
        # end
        
    # END testcase - test_Log_02_print
    
    #===========================================================================#
    # Testcase method: test_Log_03_ForcedError
    #
    # Description: Test the method: raise(...), try/except/finally
    #
    #                    If this runs as expected you should see the following at the end of your STDOUT
    #
    #                            Written from finally
    #                            E
    #                            Finished in 0.024 seconds.
    #
    #                            1) Error:
    #                            test_Log_raise(UnitTest_Log):
    #                            RuntimeError: *** ERROR - Written from except after backtrace
    #                            log_unittiest_.rb:194:in `test_Log_ForcedError'
    #
    #                            3 tests, 0 assertions, 0 failures, 1 errors
    #                            >Exit code: 1
    #
    # NOTE: This test case is renamed as te_st_* so that is it no normally run.
    #       To run it rename it as test_*. Note that it will produce errors if it run correctly.
    #===========================================================================#
    def te_st_Log_03_ForcedError(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Log_03_ForcedError")
        print2("#######################")
        
        sTrace = "This is a simulated trace"
        
        try:
            print2("Written from try")
            # This line should make execution jump to the rescue section, the text in it will then be output by e.message
            raise NameError("Simulating a Runtime issue in try")
            print2("Also written from try, but not run due to the raise statement")
            
        except:
            print2("Written from except")
            print2("The following backtrace is a WARN level, thus it does NOT raise a counted error")
            sTrace = "This is a simulated trace" #traceback.print_exc(file=sys.stdout)
            print2("*** WARN Backtrace: " + sTrace + ("\n"), "WARN")
            
            print2("\n\nThe following backtrace is a ERROR level, and raise a counted error")
            print2("*** ERROR Backtrace: " + sTrace + ("\n"), "ERROR")
            
            raise PyWorksError("*** TESTCASE - Written from except after backtrace")
            
        else:
            print2("Written from finally")
        # end
        
        print2("Written from after finally, and NOT run due to the raise statement in except")
        
    # END testcase - test_Log_03_ForcedError
    
# END class - UnitTest_Log

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_Log)
unittest.TextTestRunner(verbosity=2).run(suite)