#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_filesystem_unittest.py
#
#  Copyright (c) 2008-2010, Joe DiMauro
#  All rights reserved.
#
# Description: Unit tests for WatirWorks methods:
#                     find_folder(...)
#                     compare_files(...)
#                     parse_csv_file(...)
#                     parse_dictionary()
#                     get_watirworks_install_path()
#                     parse_ascii_file(...)
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
# Class: UnitTest_FileSytem
#
#
# Test Case Methods: setup, teardown
#                    find_folder(...)
#                    compare_files(...)
#                    parse_csv_file(...)
#
#=============================================================================#
class UnitTest_FileSytem(unittest.TestCase):


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
    # Testcase method: test_FileSystem_001_subdirs
    #
    # Description: Test the method subdirs(...)
    #===========================================================================#
    def test_FileSystem_001_subdirs(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_FileSystem_001_subdirs")
        print2("#######################")
        
        #VERBOSE = True
        
        # Get the Current Working Directory
        sDir = os.getcwd()
        
        print2("\nSearch for sub-dirs directly under the directory: \n " + sDir)
        
        aSubdirs = subdirs(sDir)
        
        print2("Found sub-dirs... ")
        for sFolder in aSubdirs:
            print2("\t " + sFolder)
        # end
        
        # Get the Current Working Directory
        sDir = get_PyWorks_install_path()
        
        print2("\nSearch for sub-dirs directly under the directory: \n " + sDir)
        
        aSubdirs = subdirs(sDir)
        
        print2("Found sub-dirs... ")
        for sFolder in aSubdirs:
            print2("\t " + sFolder)
        # end
        
        
        
        
    # End of test method - test_FileSystem_001_subdirs
    
    
    #===========================================================================#
    # Testcase method: test_FileSystem_002_list_subdirs
    #
    # Description: Test the method list_subdirs(...)
    #===========================================================================#
    def test_FileSystem_002_list_subdirs(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_FileSystem_002_list_subdirs")
        print2("#######################")
        
        #VERBOSE = True
        
        # Get the Current Working Directory
        sPWD = os.getcwd()
        
        print2("\nRecursive directory search from the location: \n " + sPWD)
        
        aSubdirs = list_subdirs(sPWD)
        
        print2(" Found folders... ")
        #print2(aSubdirs)
        for sListing in aSubdirs:
            print2(sListing)
        # end
        
    # End of test method - test_FileSystem_002_list_subdirs
    
    
    #===========================================================================#
    # Testcase method: test_FileSystem_002_list_tree
    #
    # Description: Test the method list_tree(...)
    #===========================================================================#
    def test_FileSystem_002_list_tree(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_FileSystem_002_list_tree")
        print2("#######################")
        
        #VERBOSE = True
        
        # Get the Current Working Directory
        sPWD = os.getcwd()
        
        print2("\nRecursive file search from the location: \n " + sPWD)
        
        aSubdirs = list_tree(sPWD)
        
        print2(" Found files... ")
        #print2(aSubdirs)
        for sListing in aSubdirs:
            print2(sListing)
        # end
        
    # End of test method - test_FileSystem_002_list_tree
    
    
    
    #===========================================================================#
    # Testcase method: test_FileSystem_003_find_folder_in_tree
    #
    # Description: Test the method find_folder_in_tree(...)
    #===========================================================================#
    def test_FileSystem_003_find_folder_in_tree(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_FileSystem_003_find_folder_in_tree")
        print2("#######################")
        
        # For additional output during this test activate the Verbose flag
        #VERBOSE = True
        
        print2("\nSearch for sub-folders from the location: \n " + os.getcwd())
        
        aFoldersToFind = ["data", "subfolder", "src", "Unittest", "PyWorks"] # sub-directories
        #aFoldersToFind = ["Lib", "src", "PyWorks", "Unittest", "data", "subfolder"]
        
        for sFolder in aFoldersToFind:
            print2("\nSearching for folder: " + sFolder)
            sPath = find_folder_in_tree(sFolder)
            print2(" Full path to folder: " + sPath)
        # end
        '''
        print2("\nSearch for the parent folders from the location: \n " + os.getcwd())
        
        aFoldersToFind = ["Lib", "src", "PyWorks"]
        
        for sFolder in aFoldersToFind:
            print2("\nSearching for folder: " + sFolder)
            sPath = find_folder_in_tree(sFolder)
            print2(" Full path to folder: " + sPath)
        # end
        
        
        print2("\nSearch for a non-existant folder...")
        sFolder = "no such folder exists"
        print2("Searching for folder: " + sFolder)
        sPath = find_folder_in_tree(sFolder)
        print2("Full path to folder: "  + sPath)
        '''
        
        
    # End of test method - test_FileSystem_003_find_folder_in_tree
    
    #===========================================================================#
    # Testcase method: test_FileSystem_004_compare_files
    #
    # Description: Test the method compare_files(...)
    #===========================================================================#
    def test_FileSystem_004_compare_files(self):
        
        #VERBOSE = True
        
        print2("")
        print2("#######################")
        print2("Testcase: test_FileSystem_004_compare_files")
        print2("#######################")
        
        sFile_1 = "data/FileOne.txt"
        sFile_2 = "data/FileTwo.txt"
        sFile_3 = "data/subfolder/FileThree.txt"
        
        sCSVFile_1 = "data/data.csv"
        sCSVFile_2 = "data/data2.csv"
        sCSVFile_3 = "data/data3.csv"
        
        print2("\nCompare a text file to itself")
        if(compare_files(sFile_1, sFile_1)):
            print2("Files match")
        else:
            print2("Files DIFFER")
        # end
        
        print2("\nCompare 2 text files that should match")
        if(compare_files(sFile_1, sFile_2)):
            print2("Files match")
        else:
            print2("Files DIFFER")
        # end
        
        print2("\nCompare 2 text files that should differ")
        if(compare_files(sFile_1, sFile_3)):
            print2("Files match")
        else:
            print2("Files DIFFER")
        # end
        
        print2("\nCompare a CSV file to itself")
        if(compare_files(sCSVFile_1, sCSVFile_1)):
            print2("Files match")
        else:
            print2("Files DIFFER")
        # end
        
        print2("\nCompare 2 CSV files that should differ")
        if(compare_files(sCSVFile_1, sCSVFile_2)):
            print2("Files match")
        else:
            print2("Files DIFFER")
        # end
        
        print2("\nCompare 2 CSV files that should match")
        if(compare_files(sCSVFile_1, sCSVFile_3)):
            print2("Files match")
        else:
            print2("Files DIFFER")
        # end
        
    # End of test method - test_FileSystem_004_compare_files
    
    #==========================================================================#
    # Testcase method: test_FileSystem_005_parse_csv_file
    #
    # Description: Test the method parse_csv_file(...)
    #===========================================================================#
    def test_FileSystem_005_parse_csv_file(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_FileSystem_005_parse_csv_file")
        print2("#######################")
        
        print2("*** SKIPPING csv ***")
        
        '''
        #VERBOSE = True
        
        sCSVFile = "data.csv"
        sDataDir = "data"
        
        aCSV_DataList = parse_csv_file(sCSVFile, sDataDir)
        
        if aCSV_DataList != []:
            # Iterate through the LIST to display each of its values (A row  of data read from the CSV file)
            for sRowRecord in aCSV_DataList:
                print2("Row: ")
                for sCellData in sRowRecord:
                    print2(" Cell: " + str(sCellData))
                # end
            # end
        # end
        
        ''' # Skipping
        
    # End of test method - test_FileSystem_005_parse_csv_file
    
    
    #===========================================================================#
    # Testcase method: test_FileSystem_006_get_text_from_file
    #
    # Description: Test the method get_text_from_file(...)
    #===========================================================================#
    def test_FileSystem_006_get_text_from_file(self):
        
        
        print2("")
        print2("#######################")
        print2("Testcase: test_FileSystem_006_get_text_from_file")
        print2("#######################")
        
        # VERBOSE = True
        
        sSearchString = "OK"
        sFile = os.path.join("data", "FileOne.txt")
        
        # Get the current directory
        sCurrentPath = os.getcwd()
        sFullPathToFile = os.path.join(sCurrentPath, sFile)
        
        # Cleanup  "\\", or ".."  in path
        sFullPathToFile = os.path.normpath(sFullPathToFile)
        
        print2("\nThe string 'OK' is only on line 2 of the file")
        print2("Any of the following searches that include parsing line 2 (the 3rd line) should find a match")
        
        print2("\n Down 1) Search file " + sFullPathToFile)
        print2("\t Search for string '" + sSearchString + "' from first line(0) DOWN to last line (0)")
        aMatched = get_text_from_file(sSearchString, sFullPathToFile, 0, 0)
        
        if (VERBOSE == True):
            print2("-"*20)
            #print2("Found list '" + str(aMatched) + "'")
            print2(aMatched)
            #print2(aMatches.__class.__name__) # AttributeError: 'list' object has no attribute '_UnitTest_FileSytem__class'
            print2("-"*20)
        # end
        print2("Match: " + str(aMatched[0]))
        print2("Line: " + str(aMatched[1]) + "  Text: " + str(aMatched[2]))
        
        
        print2("\nDown 2) Search file " + sFullPathToFile)
        print2("\t Search for string '" + sSearchString + "' from first line (0) DOWN for (2) lines")
        aMatched = get_text_from_file(sSearchString, sFullPathToFile, 0, 2)
        
        if (VERBOSE == True):
            print2("-"*20)
            #print2("Found list '" + str(aMatched) + "'")
            print2(aMatched)
            #print2(aMatches.__class.__name__) # AttributeError: 'list' object has no attribute '_UnitTest_FileSytem__class'
            print2("-"*20)
        # end
        print2("Match: " + str(aMatched[0]))
        print2("Line: " + str(aMatched[1]) + "  Text: " + str(aMatched[2]))
        
        print2("\nDown 3) Search file " + sFullPathToFile)
        print2("\t Search for string '" + sSearchString + "' from line (2) DOWN for (3) lines")
        aMatched = get_text_from_file(sSearchString, sFullPathToFile, 2, 3)
        
        if (VERBOSE == True):
            print2("-"*20)
            #print2("Found list '" + str(aMatched) + "'")
            print2(aMatched)
            #print2(aMatches.__class.__name__) # AttributeError: 'list' object has no attribute '_UnitTest_FileSytem__class'
            print2("-"*20)
        # end
        print2("Match: " + str(aMatched[0]))
        print2("Line: " + str(aMatched[1]) + "  Text: " + str(aMatched[2]))
        
        print2("\nDown 4) Search file " + sFullPathToFile)
        print2("\t Search for string '" + sSearchString + "' from first line (0) DOWN for out of bounds lines (9999)")
        aMatched = get_text_from_file(sSearchString, sFullPathToFile, 0, 9999)
        
        if (VERBOSE == True):
            print2("-"*20)
            #print2("Found list '" + str(aMatched) + "'")
            print2(aMatched)
            #print2(aMatches.__class.__name__) # AttributeError: 'list' object has no attribute '_UnitTest_FileSytem__class'
            print2("-"*20)
        # end
        print2("Match: " + str(aMatched[0]))
        print2("Line: " + str(aMatched[1]) + "  Text: " + str(aMatched[2]))
        
        print2("\nDown 5) Search file " + sFullPathToFile)
        print2("\t Search for string '" + sSearchString + "' from line (3) DOWN for out of bounds lines (9999)")
        aMatched = get_text_from_file(sSearchString, sFullPathToFile, 3, 9999)
        
        print2("Match: " + str(aMatched[0]))
        print2("Line: " + str(aMatched[1]) + "  Text: " + str(aMatched[2]))
        
        print2("\nDown 6) Search file " + sFullPathToFile)
        print2("\t Search for string '" + sSearchString + "' from out-of-bounds line (9999) DOWN for out of bounds lines (9999)")
        aMatched = get_text_from_file(sSearchString, sFullPathToFile, 9999, 9999)
        
        print2("Match: " + str(aMatched[0]))
        print2("Line: " + str(aMatched[1]) + "  Text: " + str(aMatched[2]))
        
        #===================================================================#
        
        print2("\nUp 1) Search file " + sFullPathToFile)
        print2("\t Search for string '" + sSearchString + "' from last line (-1) UP for (5) lines")
        aMatched = get_text_from_file(sSearchString, sFullPathToFile, -1, -5)
        
        print2("Match: " + str(aMatched[0]))
        print2("Line: " + str(aMatched[1]) + "  Text: " + str(aMatched[2]))
        
        print2("\nUp 2) Search file " + sFullPathToFile)
        print2("\t Search for string '" + sSearchString + "' from line (5) UP for (4) lines")
        aMatched = get_text_from_file(sSearchString, sFullPathToFile, 5, -4)
        
        print2("Match: " + str(aMatched[0]))
        print2("Line: " + str(aMatched[1]) + "  Text: " + str(aMatched[2]))
        
        
        print2("\nUp 3) Search file " + sFullPathToFile)
        print2("\t Search for string '" + sSearchString + "' from last line (-1) UP for (4) lines")
        aMatched = get_text_from_file(sSearchString, sFullPathToFile, -1, -4)
        
        print2("Match: " + str(aMatched[0]))
        print2("Line: " + str(aMatched[1]) + "  Text: " + str(aMatched[2]))
        
        print2("\nUp 4) Search file " + sFullPathToFile)
        print2("\t Search for string '" + sSearchString + "' from out of bounds line (9999) up for out of bounds lines (-9999)")
        aMatched = get_text_from_file(sSearchString, sFullPathToFile, 9999, -9999)
        
        print2("Match: " + str(aMatched[0]))
        print2("Line: " + str(aMatched[1]) + "  Text: " + str(aMatched[2]))
        '''
        # Iterate through the LIST to display each of its values (A row  of data read from the file)
        for aMatch in aMatches:
            print2("Match: " + str(aMatch[0]))
            print2("Line: " + str(aMatch[1]) + "  Text: " + str(aMatch[2]))
        # end
        '''
        
    # End of test method - test_FileSystem_006_get_text_from_file
    
    
    #===========================================================================#
    # Testcase method: test_FileSystem_007_parse_dictionary
    #
    # Description: Test the methods: parse_dictionary()
    #                                             get_PyWorks_install_path()      # Called by parse_dictionary()
    #                                             parse_ascii_file(...)      # Called by parse_dictionary()
    #===========================================================================#
    def test_FileSystem_007_parse_dictionary(self):
        
        print2("")
        print2("#######################")
        print2("Testcase: test_FileSystem_007_parse_dictionary")
        print2("#######################")
        
        aDictionaryContents = parse_dictionary(self)
        
        print2("First word in dictionary: " + aDictionaryContents[0])
        print2("Second word in dictionary: " + aDictionaryContents[1])
        
        iLastLineInFile = (len(aDictionaryContents) -1)
        print2("Words in dictionary:" + str(iLastLineInFile))
        
        print2("Last word in dictionary: " + aDictionaryContents[iLastLineInFile])
        
        # Clear the global variable so it doesn't impact other unittests
        DICTIONARY = None
        
    # End of test method - test_FileSystem_007_parse_dictionary
    
# End of Class - UnitTest_FileSytem

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_FileSytem)
unittest.TextTestRunner(verbosity=2).run(suite)
