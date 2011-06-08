#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_string_unittest.py
#
# Description: Unit tests for PyWorks STRING methods:
#                   word_count()
#                   prefix(...)
#                   suffix(...)
#                   format_dateString_mdyy(...)
#                   format_dateString_mmddyyyy(...)
#                   to_sentence()
#
#              Unit tests for other string related methods:
#                   reverse_String()
#                   random_alphanumeric(...)
#                   random_number(...)
#                   random_boolean()
#                   random_char(...)
#                   random_chars(...)
#                   random_pseudowords(...)
#                   random_paragraph(...)
#                   compare_strings_in_lists(...)
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
class UnitTest_String(unittest.TestCase):

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
    # Testcase method: test_String_001_isBlank
    #
    # Description: Test the method is_blank()
    #              This method is  a extension of the STRING class
    #===========================================================================#
    def test_String_001_isBlank(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_String_001_isBlank")
        print2("#######################")
    
        # Space, tab, empty, and formatting strings that should test as blank
        aStrings = [" ", ' ', "    ", "", "\n", "\t"]
        for sString in aStrings: 
            bIsBlank = is_blank(sString)
            print2("Expected False: "  + str(bIsBlank) + ' "' + str(sString) + '" ')
        # end
    
        # Strings that  should test and NOT blank
        aStrings = ["a", "a b", " a ", "    b    ", chr(120), "blank" ]
    
        for sString in aStrings: 
            bIsBlank = is_blank(sString)
            print2("Expected True: " + str(bIsBlank) + ' "' + sString + '" ')
        # end
    
    
    # End of test method - test_String_001_isBlank
        
    #===========================================================================#
    # Testcase method: test_String_002_wordcount
    #
    # Description: Test the method wc()
    #===========================================================================#
    def test_String_002_wordcount(self):

        print2("")
        print2("#######################")
        print2("Testcase: test_String_002_wordcount")
        print2("#######################")


        sStringVariable = "Doesn't count contractions or hyphens as two-words"
        aListofStrings = [
       "  Multiple \t Whitespace  is \tignored. New line\n also. \n123-456 \n a+b i:2  1/2    ",
       sStringVariable,
       "THE END"
        ]

        for sString in aListofStrings:
            print2("\nString: " + sString)
            print2("Word count: " + str(word_count(sString)))
            #print2("Word count: " + str(str(sString).wc()))

        # end

    # End of test method - test_String_002_wordcount

    
    #===========================================================================#
    # Testcase method: test_String_003_reverse_String
    #
    # Description: Test the method reverse_string()
    #              This method is NOT a extension of the STRING object, but
    #              is unit tested here along with other random STRING manipulation methods
    #===========================================================================#
    def test_String_003_reverse_String(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_String_003_reverse_String")
        print2("#######################")
        
        print2("")
        sMyString = 'skroWyP'
        sReversedString = reverse_string(sMyString)
        print2("Reversed '" + sMyString + "' to '" + sReversedString + "'")\
    
    # End of test method - test_String_003_reverse_String
    
 
    #===========================================================================#
    # Testcase method: test_String_004_ToSentence
    #
    # Description: Test the method to_sentence()
    #              This method is as extension of the STRING object,
    #===========================================================================#
    def test_String_004_ToSentence(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_String_004_ToSentence")
        print2("#######################")
    
    
        print2("\nA specific string...")
        sString = "oNCE UPON a time Long ago and far away"
        print2("\n String: " + sString)
        sSentence = to_sentence(sString)
        print2(" Sentence: " + str(sSentence))
    
        print2("\nFour sets of 2 pseudo words as sentences...")
        for _ in xrange(4):
            sString = random_pseudowords(2, 10)
            print2("\n String: " + sString)
            sSentence = to_sentence(sString)
            print2(" Sentence: " + str(sSentence))
    
        print2("\nTwo sets of 3 pseudo words ending in a period as sentences...")
        for _ in xrange(2):
            sString = random_pseudowords(3, 10) + "."
            print2("\n String: " + sString)
            sSentence = to_sentence(sString)
            print2(" Sentence: " + str(sSentence))
    
        print2("\nTwo sets of 4 pseudo words ending in a exclamation point as sentences...")
        for _ in xrange(2):
            sString = random_pseudowords(4, 10) + "!"
            print2("\n String: " + sString)
            sSentence = to_sentence(sString)
            print2(" Sentence: " + str(sSentence))
    
        print2("\nTwo sets of 5 pseudo words ending in a question mark as sentences...")
        for _ in xrange(2):
            sString = random_pseudowords(5, 10) + "?"
            print2("\n String: " + sString)
            sSentence = to_sentence(sString)
            print2(" Sentence: " + str(sSentence))
    
    # End of test method - test_String_004_ToSentence


    #===========================================================================#
    # Testcase method: test_String_005_prefix
    #
    # Description: Test the method prefix()
    #===========================================================================#
    def test_String_005_prefix(self):

        
        print2("")
        print2("#######################")
        print2("Testcase: test_String_005_prefix")
        print2("#######################")

        sMyFile = "some_long_filename.log"
        print2("\nReturn the file name without its extension for: " + sMyFile)
        sMyFilePrefix = prefix(sMyFile,".")
        print2("File name: " + sMyFilePrefix)
        #
        sMyEmailAddress = "joe@gmail.net"
        print2("\nReturn the user account of the Email address: " + sMyEmailAddress)
        sMyUserAccount = prefix(sMyEmailAddress,"@")
        print2("User account: " + sMyUserAccount)

        sMyString = "This is a test"
        print2("\nReturn the first word in the string: " + sMyString)
        sMyFirstWord = prefix(sMyString," ")
        print2("First word: " + sMyFirstWord)

        sMyString = "   String with leading & trailing white space "
        print2("\nReturn the first word of the String: " + sMyString)
        sMyFirstWord = prefix(sMyString," ")
        print2("First word: " + sMyFirstWord)

        sMyString = "   No delimiter specified "
        print2("\nReturn the whole String if: " + sMyString)
        sMyFirstWord = prefix(sMyString,"")
        print2("String: " + sMyFirstWord)

        sMyString = "   Multiple delimiter-characters that are in the specified string   "
        print2("\nReturn the first word of the String: " + sMyString)
        sMyFirstWord = prefix(sMyString," #")
        print2("First word: " + sMyFirstWord)

        sMyString = "   Delimiter character is NOT in the string "
        print2("\nReturn the whole String if: " + sMyString)
        sMyFirstWord = prefix(sMyString,".")
        print2("String: " + sMyFirstWord)

    # End of test method - test_String_005_prefix


    #===========================================================================#
    # Testcase method: test_String_006_suffix
    #
    # Description: Test the method suffix()
    #===========================================================================#
    def test_String_006_suffix(self):

        print2("")
        print2("#######################")
        print2("Testcase: test_String_006_suffix")
        print2("#######################")

        sMyFile = "some_long_filename.log"
        print2("\nReturn the file extension for: " + sMyFile)
        sMyFileSuffix = suffix(sMyFile,".")
        print2("File name extension: " + sMyFileSuffix)
        #
        sMyEmailAddress = "joe@gmail.net"
        print2("\nReturn the domain of the Email address: " + sMyEmailAddress)
        sMyDomain = suffix(sMyEmailAddress,"@")
        print2("Domain: " + sMyDomain)

        sMyString = "This is a test"
        print2("\nReturn the last word in the string: " + sMyString)
        sMyLastWord = suffix(sMyString," ")
        print2("Last word: " + sMyLastWord)

        sMyString = "   String with leading & trailing white space "
        print2("\nReturn the last word of the String: " + sMyString)
        sMyLastWord = suffix(sMyString, " ")
        print2("Last word: " + sMyLastWord)

        sMyString = "   No delimiter specified "
        print2("\nReturn the whole String if: " + sMyString)
        sMyLastWord = suffix(sMyString,"")
        print2("String: " + sMyLastWord)

        sMyString = "   Multiple delimiter-characters that are in the specified string   "
        print2("\nReturn the last word of the String: " + sMyString)
        sMyLastWord = suffix(sMyString," #")
        print2("Last word: " + sMyLastWord)

        sMyString = "   Delimiter character is NOT in the string "
        print2("\nReturn the whole String if: " + sMyString)
        sMyLastWord = suffix(sMyString,".")
        print2("String: " + sMyLastWord)

    # End of test method - test_String_006_suffix

    #===========================================================================#
    # Testcase method: test_String_007_remove_prefix
    #
    # Description: Test the method remove_prefix()
    #===========================================================================#
    def test_String_007_remove_prefix(self):

        print2("")
        print2("#######################")
        print2("Testcase: test_String_007_remove_prefix")
        print2("#######################")

        sMyFile = "some_long_filename.log"
        print2("\nReturn the file extension for: " + sMyFile)
        sMyFilePrefix = remove_prefix(sMyFile,".")
        print2("File name: " + sMyFilePrefix)
        #
        sMyEmailAddress = "joe@gmail.net"
        print2("\nReturn the Domain Name of the Email address: " + sMyEmailAddress)
        sMyUserAccount = remove_prefix(sMyEmailAddress,"@")
        print2("User account: " + sMyUserAccount)

        sMyString = "This is a test"
        print2("\nReturn the string with the first word removed: " + sMyString)
        sMyFirstWord = remove_prefix(sMyString," ")
        print2("First word: " + sMyFirstWord)

        sMyString = "   String with leading & trailing white space "
        print2("\nReturn the first word of the String: " + sMyString)
        sMyFirstWord = remove_prefix(sMyString," ")
        print2("First word: " + sMyFirstWord)

        sMyString = "   No delimiter specified "
        print2("\nReturn the whole String if: " + sMyString)
        sMyFirstWord = remove_prefix(sMyString,"")
        print2("String: " + sMyFirstWord)

        sMyString = "   Multiple delimiter-characters that are in the specified string   "
        print2("\nReturn the string with the first word removed: " + sMyString)
        sMyFirstWord = remove_prefix(sMyString," #")
        print2("First word: " + sMyFirstWord)

        sMyString = "   Delimiter character is NOT in the string "
        print2("\nReturn the whole String if: " + sMyString)
        sMyFirstWord = remove_prefix(sMyString,".")
        print2("String: " + sMyFirstWord)

    # End of test method - test_String_007_remove_prefix


    #===========================================================================#
    # Testcase method: test_String_007_remove_suffix
    #
    # Description: Test the method remove_suffix()
    #===========================================================================#
    def test_String_007_remove_suffix(self):

        print2("")
        print2("#######################")
        print2("Testcase: test_String_007_remove_suffix")
        print2("#######################")

        sMyFile = "some_long_filename.log"
        print2("\nReturn the file name with the extension removed: " + sMyFile)
        sMyFileSuffix = remove_suffix(sMyFile,".")
        print2("File name extension: " + sMyFileSuffix)
        #
        sMyEmailAddress = "joe@gmail.net"
        print2("\nReturn the User Account of the Email address: " + sMyEmailAddress)
        sMyDomain = remove_suffix(sMyEmailAddress,"@")
        print2("Domain: " + sMyDomain)

        sMyString = "This is a test"
        print2("\nReturn the string with the last word removed: " + sMyString)
        sMyLastWord = remove_suffix(sMyString," ")
        print2("Last word: " + sMyLastWord)

        sMyString = "   String with leading & trailing white space "
        print2("\nReturn the string with the last word removed: " + sMyString)
        sMyLastWord = remove_suffix(sMyString," ")
        print2("Last word: " + sMyLastWord)

        sMyString = "   No delimiter specified "
        print2("\nReturn the whole String if: " + sMyString)
        sMyLastWord = remove_suffix(sMyString,"")
        print2("String: " + sMyLastWord)

        sMyString = "   Multiple delimiter-characters that are in the specified string   "
        print2("\nReturn the string with the last word removed: " + sMyString)
        sMyLastWord = remove_suffix(sMyString," #")
        print2("Last word: " + sMyLastWord)

        sMyString = "   Delimiter character is NOT in the string "
        print2("\nReturn the whole String if: " + sMyString)
        sMyLastWord = remove_suffix(sMyString,".")
        print2("String: " + sMyLastWord)

    # End of test method - test_String_007_remove_suffix

    #===========================================================================#
    # Testcase method: test_String_008_format_dateString_mdyy
    #
    # Description: Test the method dateString_mdyy(...) with dates expressed as strings
    #===========================================================================#
    def test_String_008_format_dateString_mdyy(self):
    
        # require 'date'
    
        print2("")
        print2("#######################")
        print2("Testcase: test_String_008_format_dateString_mdyy")
        print2("#######################")
    
        print2("\nTesting slash delimited dates expressed as STRINGS")
    
        # LIST of date strings to test
        aDateStrings = [
        "12/31/2000",
        "1/1/01",
        "01/02/2002",
        "01/3/2003",
        "11/5/1900",
        "10/06/1901"
        ]
    
        # Loop through the list, converting each date string
        for sDateString in aDateStrings: 
            print2(sDateString + " formatted as  " + format_dateString_mdyy(sDateString,"/"))
        # end
    
        print2("\nTesting period delimited dates expressed as STRINGS")
        # LIST of date strings to test
        aDateStrings = [
        "12.31.2000",
        "1.1.01",
        "01.02.2002",
        "01.3.2003",
        "11.5.1900",
        "10.06.1901"
        ]
    
        # Loop through the list, converting each date string
        for sDateString in aDateStrings: 
            print2(sDateString + " formatted as  " + format_dateString_mdyy(sDateString,"."))
        # end
    
    # End of testcase - test_String_008_format_dateString_mdyy
    
    #===========================================================================#
    # Testcase method: test_String_009_format_dateString_mmddyyyy
    #
    # Description: Test the method format_dateString_mmddyyyy(...) with dates expressed as strings
    #===========================================================================#
    def test_String_009_format_dateString_mmddyyyy(self):
    
        #require 'date'
    
        print2("")
        print2("#######################")
        print2("Testcase: test_String_009_format_dateString_mmddyyyy")
        print2("#######################")
    
        print2("\nTesting slash delimited dates expressed as STRINGS to the 1900's")
    
        # LIST of date strings to test
        aDateStrings = [
        "1/1/01",
        "01/02/01",
        "11/1/01",
        "1/10/01",
        "12/31/2000",
        ]
    
        # Loop through the list, converting each date string
        for sDateString in aDateStrings: 
            print2(sDateString + "  formatted as  " + format_dateString_mmddyyyy(sDateString,"/" , "19"))
        # end
    
    
        print2("\nTesting period delimited dates expressed as STRINGS to the 2300's")
    
        # LIST of date strings to test
        aDateStrings = [
        "1.1.01",
        "01.02.01",
        "11.1.01",
        "1.10.01",
        "12.31.2000",
        ]
    
        # Loop through the list, converting each date string
        for sDateString in aDateStrings: 
            print2(sDateString + "  formatted as  " + format_dateString_mmddyyyy(sDateString,"." , "23"))
        # end
    
    # End of testcase - test_String_009_format_dateString_mmddyyyy
    

    #===========================================================================#
    # Testcase method: test_String_010_compare_strings_in_lists
    #
    # Description: Test the method compare_strings_in_lists(...)
    #              This method is NOT a extension of the STRING object, but
    #              is unit tested here as it deals with STRINGS
    #===========================================================================#
    def test_String_010_compare_strings_in_lists(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_String_010_compare_strings_in_lists")
        print2("#######################")
        
        sString = "Some strings are identical, and some strings are not identical"
        
        # OLD CODE # sString.scan(/ (^| \s)(\S +)(? = \s. * ?\2) /) { print2 $2 }
        print2(sString) 
        
        
        print2("\nTesting Compare strings...")
        aFirstList = ["the", "end", "the end", "stop"]
        aSecondList = ["The end", "end", "start", "the", "Stop"]
        print2("Compare first LIST:")
        print2(str(aFirstList))
        print2("\nWith second LIST:")
        print2(str(aSecondList))
        print2("Expect 5 case insensitive matches")
        aFound = compare_strings_in_lists(aFirstList, aSecondList)
        print2("Exact Matches Found: " + str(aFound[0]))
        print2(" Matching text: " + str(aFound[1]))
        
        print2("\nTesting Compare strings Ignore case...")
        aFirstList = ["the", "end", "the end", "stop"]
        aSecondList = ["The end", "end", "start", "the", "Stop"]
        print2("Compare first LIST:")
        print2(str(aFirstList))
        print2("\nWith second LIST:")
        print2(str(aSecondList))
        print2("Expect 8 case sensitive exact matches")
        aFound = compare_strings_in_lists(aFirstList, aSecondList, True)
        print2("Exact Matches Found: " + str(aFound[0]))
        aMatches = str(aFound[1])
        #print2(" Matching text: " + str(aFound[1]))
        print2(" Matching text: " + aMatches)
        
        print2("\nTesting Compare Regexp (Ignore case)...")
        aFirstList = ["the", "end", "the end", "stop"]
        aSecondList = ["The end", "end", "start", "the", "Stop"]
        print2("Compare first LIST:")
        print2(str(aFirstList))
        print2("\nWith second LIST:")
        print2(str(aSecondList))
        print2("Expect 4 case insensitive exact matches")
        aFound = compare_strings_in_lists(aFirstList, aSecondList, True, True)
        
        # Display the matches
        if (aFound[0] != None):
            print2("\tClose Matches Found: " + str(aFound[0]))
            aMatches = str(aFound[1])
            print2("\tMatching text: " + aMatches)
        # end
    
    # End of test method - test_String_010_compare_strings_in_lists

 

# End of class - UnitTest_String

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_String)
unittest.TextTestRunner(verbosity=2).run(suite)
