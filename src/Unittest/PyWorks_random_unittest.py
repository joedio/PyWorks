#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_random_unittest.py
#
# Description: Unit tests for other string related methods:
#                   random_alphanumeric(...)
#                   random_number(...)
#                   random_boolean()
#                   random_char(...)
#                   random_chars(...)
#                   random_pseudowords(...)
#                   random_paragraph(...)
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
# Class: UnitTest_Random
#
#
# Test Case Methods: setUp, tearDown
#
#
#
#=============================================================================#
class UnitTest_Random(unittest.TestCase):

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
    # Testcase method: test_Random_001_RandomNumber
    #
    # Description: Test the method random_number()
    #              This method is NOT a extension of the STRING object, but
    #              is unit tested here along with other random STRING manipulation methods
    #===========================================================================#
    def test_Random_001_RandomNumber(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_Random_001_RandomNumber")
        print2("#######################")
    
        print2("Random number between 1 to 6 = " + str(random.randint(1, 6)))
        print2("Random number between 0 to 1 = " + str(random.randint(0, 1)))
        #print2("Random number between 1 and 6 = " + str(random_number(1, 6)))
        
        print2("\nTwenty-five random numbers between 100 and 125...")
        for _ in xrange(20):
            print2(" Random number: " + str(random_number(100, 125)))
    
    # End of test method - test_Random_001_RandomNumber
    
    #===========================================================================#
    # Testcase method: test_Random_002_RandomBoolean
    #
    # Description: Test the method random_boolean()
    #              This method is NOT a extension of the STRING object, but
    #              is unit tested here along with other random STRING manipulation methods
    #===========================================================================#
    def test_Random_002_RandomBoolean(self):
    
        VERBOSE = False
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Random_002_RandomBoolean")
        print2("#######################")
    
        print2("\nTen random BOOLEAN values...")
    
        for _ in xrange(10):
            print2(" Random BOOLEAN value: " + str(random_boolean()))
    
    # End of test method - test_Random_002_RandomBoolean

 
    #===========================================================================#
    # Testcase method: test_Random_003_RandomAlphaNumeric
    #
    # Description: Test the method random_alphanumeric()
    #              This method is NOT a extension of the STRING object, but
    #              is unit tested here along with other random STRING manipulation methods
    #===========================================================================#
    def test_Random_003_RandomAlphaNumeric(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_Random_003_RandomAlphaNumeric")
        print2("#######################")
    
        print2("")
        sMyString = random_alphanumeric(10)
        
        print2("Random 10 " + " AlphaNumeric character string: " + sMyString)
    
        print2("Random 20 " + " AlphaNumeric character string: " + random_alphanumeric(20))
        print2("")
    
        # Print the random sting of lengths from iMin to iMax
        iMin = -1
        iMax = 25
        for iInteger in xrange(iMin, iMax):
            print2("Random " + str(iInteger) + " character string: " + random_alphanumeric(iInteger))
    
    # End of test method - test_Random_003_RandomAlphaNumeric
        
    #===========================================================================#
    # Testcase method: test_Random_004_RandomChar
    #
    # Description: Test the method random_char()
    #              This method is NOT a extension of the STRING object, but
    #              is unit tested here along with other random STRING manipulation methods
    #===========================================================================#
    def test_Random_004_RandomChar(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_Random_004_RandomChar")
        print2("#######################")
    
        print2("\nThirty random lower case ASCII characters...")
        for _ in xrange(30):
            print2(" Random lower case character: " + random_char(False))
    
        print2("\nThirty random UPPER CASE Characters...")
        for _ in xrange(30):
            print2(" Random UPPER CASE Character: " + random_char(True))
    
    # End of test method - test_Random_004_RandomChar
    
    #===========================================================================#
    # Testcase method: test_Random_005_RandomChars
    #
    # Description: Test the method random_chars()
    #              This method is NOT a extension of the STRING object, but
    #              is unit tested here along with other random STRING manipulation methods
    #===========================================================================#
    def test_Random_005_RandomChars(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_Random_005_RandomChars")
        print2("#######################")
    
        print2("\nTen random sets of 10 ASCII characters...")
        for _ in xrange(10):
            print2(" Random lower case character set: " + random_chars())
    
        print2("\nFive random Capitalized sets of 10 ASCII characters...")
        for _ in xrange(5):
            print2(" Random Capitalized Character set: " + random_chars(10, True))
    
        print2("\nTen random Capitalized sets of a random number of ASCII characters...")
        for _ in xrange(5):
            print2(" Random Capitalized Character set: " + random_chars(random_number(0, 10), True))
    
        for _ in xrange(5):
            print2(" Random Capitalized Character set: " + random_chars(random_number(10, 20), True))
    
    # End of test method - test_Random_005_RandomChars
    
    #===========================================================================#
    # Testcase method: test_Random_006_RandomPseudoWords
    #
    # Description: Test the method random_pseudowords()
    #              This method is NOT a extension of the STRING object, but
    #              is unit tested here along with other random STRING manipulation methods
    #===========================================================================#
    def test_Random_006_RandomPseudoWords(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_Random_006_RandomPseudoWords")
        print2("#######################")
    
        print2("\nFour random lower case sets of 2 pseudo words of up to 10 ASCII characters...")
        for _ in xrange(4):
            print2(" Random lower case pseudo word set: " + random_pseudowords(2, 10))
    
        print2("\nTwo random Capitalized sets of 10 pseudo words of up to 5 ASCII characters...")
        for _ in xrange(2):
            print2(" Random Capitalized pseudo word set: " + random_pseudowords(10, 5, True))
    
        print2("\nTen random Capitalized sets of a random pseudo words comprised of a random number of ASCII characters...")
        for _ in xrange(5):
            print2(" Random Capitalized pseudo word set: " + random_pseudowords(random_number(2, 10), random_number(2, 10), True))
            
        for _ in xrange(5):
            print2(" Random Capitalized pseudo word set: " + random_pseudowords(random_number(10, 20), random_number(2, 10), True))
    
    # End of test method - test_Random_006_RandomPseudoWords

    
    #===========================================================================#
    # Testcase method: test_Random_007_RandomParagraph
    #
    # Description: Test the method random_paragraph()
    #              This method is NOT a extension of the STRING object, but
    #              is unit tested here along with other random STRING manipulation methods
    #===========================================================================#
    def test_Random_007_RandomParagraph(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_Random_007_RandomParagraph")
        print2("#######################")
    
        print2("\n Paragraph of 4 sentences with a max of 6 words per sentence, and 10 chard per word.")
        print2(random_paragraph(4, 6, 10))
    
        print2("\n More paragraphs...")
        print2(random_paragraph(5, 6, 10))
        print2(random_paragraph(7, 10, 10))
        print2(random_paragraph(random_number(3, 5), random_number(4, 6), random_number(5, 7)))
    
    
    # End of test method - test_Random_007_RandomParagraph
    
    
    #===========================================================================#
    # Testcase method: test_Random_008_RandomWord
    #
    # Description: Test the method random_word()
    #              This method is NOT a extension of the STRING object, but
    #              is unit tested here along with other random STRING manipulation methods
    #===========================================================================#
    def test_Random_008_RandomWord(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_Random_008_RandomWord")
        print2("#######################")
    
        print2("\nTwenty lower case random words read from the PyWorks DICTIONARY....")
        for _ in xrange(20):
            print2("Word: " + random_word())
    
        print2("\nTwenty Capitalized random words read from the PyWorks DICTIONARY....")
        for _ in xrange(20):
            print2("Word: " + random_word(True))
    
    
    # End of test method - test_Random_008_RandomWord
    
    #===========================================================================#
    # Testcase method: test_Random_009_RandomSentence
    #
    # Description: Test the method random_sentence()
    #              This method is NOT a extension of the STRING object, but
    #              is unit tested here along with other random STRING manipulation methods
    #===========================================================================#
    def test_Random_009_RandomSentence(self):
    
        print2("")
        print2("#######################")
        print2("Testcase: test_Random_009_RandomSentence")
        print2("#######################")
    
        print2("\nTen sentences of 5 random words read from the PyWorks DICTIONARY....")
        for _ in xrange(10):
            print2("Sentence: " + random_sentence(5))
    
        print2("\nTen sentences of a random number of random words read from the PyWorks DICTIONARY....")
        for _ in xrange(10):
            print2("Sentence: " + random_sentence(random_number(2, 5)))
    
        # Clear the global variable so it doesn't impact other unittests
        DICTIONARY = False
    
    # End of test method - test_Random_009_RandomSentence

# End of class - UnitTest_Random

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_Random)
unittest.TextTestRunner(verbosity=2).run(suite)
