#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_date_unittest.py
#
#  Copyright (c) 2008-2011, Joe DiMauro
#  All rights reserved.
#
# Description: Unit test showing various examples of date manipulation using
#               methods to split various date strings into their components.
#
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by this test
#=============================================================================#

import unittest
from datetime import date, datetime, timedelta # Add ability to get/format Dates
#import time                    # Add ability to get/format Time



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
sRun_TestType = "ready"
iRun_TestLevel = 0
VERBOSE = False
#=============================================================================#

#=============================================================================#
# Class: UnitTest_Date
#
#
# Test Case Methods: setUp, tearDown
#                    test_date_001_jython_date_manipulation
#
#=============================================================================#
class UnitTest_JythonDate(unittest.TestCase):


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
    # Testcase method: test_date_001_jython_date_manipulation
    #
    # Description: Jython's methods to split various date strings into their components.
    #
    # Formatting parameters for methods:
    #            time.strptime(string[, format])
    #            time.strftime([format,] time)
    # 
    #     %a - abbreviated weekday name
    #     %A - full weekday name
    #     %b - abbreviated month name
    #     %B - full month name
    #     %c - preferred date and time representation
    #     %C - century number (the year divided by 100, range 00 to 99)
    #     %d - day of the month (01 to 31)
    #     %D - same as %m/%d/%y
    #     %e - day of the month (1 to 31)
    #     %g - like %G, but without the century
    #     %G - 4-digit year corresponding to the ISO week number (see %V).
    #     %h - same as %b
    #     %H - hour, using a 24-hour clock (00 to 23)
    #     %I - hour, using a 12-hour clock (01 to 12)
    #     %j - day of the year (001 to 366)
    #     %m - month (01 to 12)
    #     %M - minute
    #     %n - newline character
    #     %p - either am or pm according to the given time value
    #     %r - time in a.m. and p.m. notation
    #     %R - time in 24 hour notation
    #     %S - second
    #     %t - tab character
    #     %T - current time, equal to %H:%M:%S
    #     %u - weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday=1
    #     %U - week number of the current year, starting with the first Sunday as the first day of the first week
    #     %V - The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week
    #     %W - week number of the current year, starting with the first Monday as the first day of the first week
    #     %w - day of the week as a decimal, Sunday=0
    #     %x - preferred date representation without the time
    #     %X - preferred time representation without the date
    #     %y - year without a century (range 00 to 99)
    #     %Y - year including the century
    #     %Z or %z - time zone or name or abbreviation
    #     %% - a literal % character
    #
    #===========================================================================#
    def test_date_01_jython_date_set(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_date_001_jython_date_setting")
        print2("#######################")
        
        
        print2("Set date and datetime to today")
        dToday = date.today()
        dtToday = datetime.now()
        
        print2("Today is date: " + str(dToday))
        print2("Today is datetime: " + str(dtToday))
        
        print2("-"*15)
        print2("Set date and datetime to other dates")
        
        aDateStrings = ["3/29/2011", "07/04/1776", "12/31/2000", "1/1/01", "2/29/2004", "12/31/18"]
        
        for sDateString in aDateStrings:
            
            print2("-"*10)
            print2("Create date using string '" + sDateString + "'")
            
            dNewDate = string_to_date(sDateString)
            
            print2(" New created datetime is: " + str(dNewDate))
        # end
        
        print2("-"*5)
        sDateString = "01-22-2011"
        print2("Converting string " + sDateString)
        
        dNewDate = string_to_date(sDateString, "-")
        
        print2("Converted String to Date: " + str(dNewDate))
        '''
        print2("-"*5)
        sDateString = "21 June 2011"
        
        print2("Converting string " + sDateString)
        dNewDate = string_to_date(sDateString, " ")
        print2("Converted String to Date: " + str(dNewDate))
        '''
            
        
    # End of test method - test_date_001_jython_date_setting
    
    #===========================================================================#
    # Testcase method: test_date_002_jython_date_caclulation
    #
    # Description: Jython's methods to split various date strings into their components.
    #===========================================================================#
    def test_date_02_jython_date_caclulation(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_date_002_jython_date_caclulation")
        print2("#######################")
        

        
        print2("Calculate datetimes based on today's datetime...")
        
        # Get the current datetime
        dtToday = datetime.now()
        
        # Syntax:
        # class timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[,hours[,weeks]]]]]]])
        
        print2("\tYesterday (datetime): \t" + str(dtToday - timedelta(days=1)))
        print2("\tToday (datetime): \t" + str(dtToday))
        print2("\tTomorrow (datetime): \t" + str(dtToday + timedelta(days=1)))
        
        print2("\tFour hours from now (datetime): " + str(dtToday + timedelta(hours=4)))
        print2("\t360 minutes from now (datetime): " + str(dtToday + timedelta(minutes=360)))
        print2("\tFifty sec from now (datetime): " + str(dtToday + timedelta(seconds=50)))
        print2("\t21 days from now(datetime): " + str(dtToday + timedelta(days=21)))
        print2("\tFifty-one weeks from now(datetime): " + str(dtToday + timedelta(weeks=51)))
        
        print2("\tTen days ago (datetime): " + str(dtToday - timedelta(days=10)))
        print2("\tTen days three hours ago (datetime): " + str(dtToday - timedelta(days=10, hours=3)))
        print2("\tOne Hundred days three hours from now (datetime): " + str(dtToday + timedelta(days=100, hours=3)))
        print2("\tThree Hundred sixty four days three hours from now (datetime): " + str(dtToday + timedelta(days=364, hours=3)))
        
        print2("-"*5)
        
        ##################################################
        print2("Calculate dates based on today's date...")
        
        # Get the current date
        dToday = date.today()
        
        print2("\tYesterday (date): \t" + str(dToday - timedelta(days=1)))
        print2("\tToday (date): \t\t" + str(dToday))
        print2("\tTomorrow (date): \t" + str(dToday + timedelta(days=1)))
        
        print2("\tFour hours from now (date): " + str(dToday + timedelta(hours=4)))
        print2("\t360 minutes from now (date): " + str(dToday + timedelta(minutes=360)))
        print2("\tFifty sec from now (date): " + str(dToday + timedelta(seconds=50)))
        print2("\t21 days from now(date): " + str(dToday + timedelta(days=21)))
        print2("\tFifty-one weeks from now(date): " + str(dToday + timedelta(weeks=51)))
        
        print2("\tTen days ago (date): " + str(dToday - timedelta(days=10)))
        print2("\tTen days three hours ago (date): " + str(dToday - timedelta(days=10, hours=3)))
        print2("\tOne Hundred days three hours from now (date): " + str(dToday + timedelta(days=100, hours=3)))
        print2("\tThree Hundred sixty four days three hours from now (date): " + str(dToday + timedelta(days=364, hours=3)))
        
        print2("-"*5)
        
        dDayAfter = dToday + timedelta(days=1)
        print2("\tThe day after is date \t\t" + str(dDayAfter))
        
        dMonthBefore = dToday - timedelta(days=31)
        print2("\tThe month before is date \t" + str(dMonthBefore))
        
        dMonthAfter= dToday + timedelta(days=31)
        print2("\tThe month after is date \t" + str(dMonthAfter))
        
        dYearBefore = dToday - timedelta(days=365)
        print2("\tThe year before is date \t" + str(dYearBefore))
        
        dYearAfter = dToday + timedelta(days=365)
        print2("\tThe year after is date \t\t" + str(dYearAfter))
        
    # End of test method - test_date_001_jython_date_setting
    
    
    #===========================================================================#
    # Testcase method: test_date_002_jython_timespan_caclulation
    #
    # Description: Jython's methods to split various date strings into their components.
    #===========================================================================#
    def test_date_03_jython_timespan_caclulation(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_date_002_jython_timespan_caclulation")
        print2("#######################")
        
        print2("Calculate time spans...")
        
        # Get the current datetime
        #dtToday = datetime.now()
        
        # Get the current date
        dToday = date.today()
        
        print2("\tToday (date): \t\t" + str(dToday))
        print2("\tYesterday (date): \t" + str(dToday - timedelta(days=1)))
        print2("\tTomorrow (date): \t" + str(dToday + timedelta(days=1)))
        
        dDayBefore = (dToday - timedelta(days=1))
        dDayAfter = (dToday + timedelta(days=1))
        
        dOffset = (dDayBefore - dToday)  # assert is instance(daysecondsfrac, float)
        dOffset2 = (dDayAfter - dToday)
        print2("\tTimespan (from yesterady to today ): " + str(dOffset))
        print2("\tTimespan (from today to tomorrow ): " + str(dOffset2))
        
        #dDayOffset=datetime.timedelta(days = 1) 
        
        print2("\tThe day before is \t" + str(dDayBefore))
        print2("\tThe day before is also \t" + dDayBefore.strftime("%m/%d/%Y"))
        print2("\tThe day after is \t" + str(dDayAfter))
        print2("\tThe day after is also \t" + dDayAfter.strftime("%m/%d/%Y"))
        print2("-"*5)
        
        dNewDate = dToday + timedelta(days=100, hours=24)
        print2("\tOne Hundred days 24 hours from now (date): \t" + str(dNewDate))
        print2("\tTimespan (date from today): \t\t" + str(dNewDate - dToday))
        
        dNewDate = dToday - timedelta(days=100, hours=24)
        print2("\tOne Hundred days 24 hours before now (date): \t" + str(dNewDate))
        print2("\tTimespan (date from today): \t\t" + str(dNewDate - dToday))
    # End of test method - test_date_002_jython_date_caclulation
    
    
# end of Class - UnitTest_Date

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_JythonDate)
unittest.TextTestRunner(verbosity=2).run(suite)