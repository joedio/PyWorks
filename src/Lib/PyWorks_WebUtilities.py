#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_WebUtilities.py
#
#  Copyright (c) 2008-2011, Joe DiMauro
#  All rights reserved.
#
# Description: Functions and methods for PyWorks
#    These functions and methods are application and platform independent,
#    but are specific to Web based applications.
#
#    Some of these methods and functions have been collected from, or based upon
#    Open Source versions found on various sites in the Internet, and are noted.
#
#--
#
#++
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by these methods
#=============================================================================#

# Jython imports
#import sys
#import traceback
#import os                           # Adds ability to set/get OS Variables
#from datetime import date, datetime, timedelta # Add ability to get/format Dates
#import time                         # Add ability to get/format Time
#import random                       # Random number generator
import re                           # Regular expressions

# PyWorks imports
#from PyWorks_Reflib import TIMESTAMP_STRING
from PyWorks_Utilities import print2


#=============================================================================#
# Module: PyWorks_WebUtilities
#=============================================================================#
#
# Description: Functions and methods for PyWorks
#    These functions and methods are application and platform independent.
#
#    Some of these methods and functions have been collected from, or based upon
#    Open Source versions found on various sites in the Internet, and are noted.
#
#
# Instructions: To use these methods in your scripts add these commands:
#                        from PyWorks_WebUtilities import *    # PyWorks Web Utilities
#--
# Table of Contents
#
#  Please manually update this TOC with the alphabetically sorted names of the items in this module,
#  and continue to add new methods alphabetically into their proper location within the module.
#
#  Key:   () = No parameters,  (...) = parameters required
#
# Functions:
#    createXMLTags(...)
#    getMultipleXMLTagValues(...)
#    getXMLTagValue(...)
#    isTagInXML(..)
#    removeXMLBrackets(...)
#
# Pre-requisites:
# ++
#=============================================================================#

# Version of this module
PW_WEB_UTILITIES_VERSION = "1.0.0"

# Define values for True/False since they were not defined in Jython2.2.1
True = 1
False = 0

#  Define the PyWorks Global logger variable to suppress messages when VERBOSE is True

#  Define the PyWorks Global dictionary variable to suppress messages when VERBOSE is True

# Clear the Verbose flag
global VERBOSE
VERBOSE = False



#=============================================================================#
#--
# Function: createXMLTags(...)
#++
#
# Description:  Adds the brackets to tag name to make Opening and Closing XML tags
#               Returns '<tag_name>' and '</tag_name>'  from 'tag_name' 
#
# Returns: LIST = The Opening and Closing XML tags
#                 [0] = STRING - Opening Tag
#                 [1] = STRING - Closing Tag
#
# Syntax: sTag =  STRING - The XML tags to strip of the enclosing brackets "<>"
#
# Usage Examples:
#                    sTag = 'UserName'     # Tag name w/o brackets
#                    addXMLBrackets(sTag)  #=>  UserName
#
#                    sTag = '<Username>'   # Opening tag with Brackets
#                    addXMLBrackets(sTag)  #=>  UserName
#
#                    sTag = '</UserName>'  # Closing tag with Brackets
#                    createXMLTags(sTag)  #=>  UserName
#
#=============================================================================#
def createXMLTags(sTagName):
    '''
    Adds the brackets to tag name to make Opening and Closing XML tags
    Returns '<tag_name>' and '</tag_name>'  from 'tag_name' 
    '''
    
    #VERBOSE = True
    
    if(VERBOSE == True):
        print2("Parameters - createXMLTags:")
        print2("  sTagName: " + sTagName)
    # end
    
    # Add the brackets to make the Opening tag
    sFullOpeningTag = "<" + sTagName + ">"
    
    # Add the brackets and slash to make the Closing tag
    sFullClosingTag = "</" + sTagName + ">"
    
    if (VERBOSE == True):
        print2("Opening tag:  " + sFullOpeningTag)
        print2("Closing tag:  " + sFullClosingTag)
    # end
    
    sXMLTags = [sFullOpeningTag, sFullClosingTag]
    
    return sXMLTags
    
# END method - createXMLTags()



#=============================================================================#
#--
# Function: getMultipleXMLTagValues(...)
#++
#
# Description:  Parses a string containing XML Tags to get the values of the specified
#               XML tag name, when there are multiple occurrences of the same Tag name . 
#               Checks that the Tags exists, NOT if they holds any content.
#               Note that a Closing XML tag </tag_name> with 
#               no Opening tag <tag_name> proceeding it will return ''.
#
# Returns: LIST of STRINGS - Each STRING in the LIST contains the value of an XML Tag
#                 [0] = The STRING between the first Opening and Closing XML Tags, or None
#                 [1] = The STRING between the second Opening and Closing XML Tags, or None
#                 [n] = The STRING between the nth Tags
#
#                 Returns [] If no occurrence of the Tag exists in the XML STRING
#                 Returns a empty STRING' For any an occurrence of the Closing Tag, 
#                 with not Opening Tag in the XML STRING
#
# Syntax: sXML =  STRING - The string containing the XML tags to be searched.
#         sTagName =  STRING - The name of the XML tag to match. Tags can be
#                              specified with or without the enclosing brackets "<>"
#
# Usage Examples:
#                   sXML = '<response><UserName>Bob</UserName><UserName>Pat</UserName><UserName>Tom</UserName></Nickname></response>'
#
#                   sTagName = "UserName"
#                   getMultipleXMLTagValues(sXML, sTag)  #=>  ['Bob','Pat','Tom'] 
#
#                   sTagName = "response"       # XML Tag containing other XML Tags
#                   getXMLTagValue(sXML, sTag)  #=>  ['<UserName>Bob</UserName><UserName>Pat</UserName><UserName>Tom</UserName></Nickname>']
#
#                   sTagName = "Nickname"  # Closing XML tag with no Opening Tag
#                   getXMLTagValue(sXML, sTag)  #=>  ['']
#
#                   sTagName = "<BogusTag>"  # An XML tag not contained within the XML String
#                   getXMLTagValue(sXML, sTag)  #=>  []
#
#=============================================================================#
def getMultipleXMLTagValues(sXML, sTagName):
    '''
    Parses a string containing XML Tags to get the values of the specified
    XML tag name, when there are multiple occurrences of the same Tag name 
    Note that a Closing XML tag (</tag_name> ) with no Opening XML Tag
    <tag_name> proceeding it will return ''
    '''
    
    #VERBOSE = True
    
    # Define default return value
    aMatchingTagValues = []
    
    if(VERBOSE == True):
        print2("Parameters - getMultipleXMLTagValues:")
        print2("  sXML: " + sXML)
        print2("  sTagName: " + sTagName)
    # end
    
    # Generate the Opening and Closing XML tags
    #
    # Its easier to first remove brackets (if they existed).
    sTagWithoutBrackets = removeXMLBrackets(sTagName)
    
    # Generate the Opening and Closing tags (with brackets)
    aXMLTags = createXMLTags(sTagWithoutBrackets)
    
    sFullOpeningTag = aXMLTags[0]
    sFullClosingTag = aXMLTags[1]
    
    if (VERBOSE == True):
        print2("Opening tag:  " + sFullOpeningTag)
        print2("Closing tag:  " + sFullClosingTag)
    # end
    
    # Determine the length of the Opening and Closing Tags
    iOpeningTagLength = len(sFullOpeningTag)
    iClosingTagLength = len(sFullClosingTag)
    
    if (VERBOSE == True):
        print2("Opening tag length:  " + str(iOpeningTagLength))
        print2("Closing tag length:  " + str(iClosingTagLength))
    # end
    #
    iTotalTagCount = sXML.count(sFullClosingTag)
    
    # Verify that the specified tag exists
    if (iTotalTagCount == 0):
        if (VERBOSE == True):
            print2("No Closing tag found:  " + sFullClosingTag)
        # end
        # No occurrence of the Closing Tag found so get out of this function
        return aMatchingTagValues
    # end
    
    if (VERBOSE == True):
        print2("Total Closing tags found:  " + str(iTotalTagCount))
    # end
    
    # Seed the counter
    iCurrentTag = iTotalTagCount
    
    # Loop to get that values of each of the Tags
    while iCurrentTag > 0:
        
        # Find the position of the first character of each Tag in the XML string
        iIndexOfFirstOpeningTag = sXML.find(sFullOpeningTag)
        iIndexOfFirstClosingTag = sXML.find(sFullClosingTag)
        
        if (VERBOSE == True):
            print2("Opening tag index:  " + str(iIndexOfFirstOpeningTag))
            print2("Closing tag index:  " + str(iIndexOfFirstClosingTag))
        # end
        
        # See if either of the Tags can't be found, save a value of ''
        if ((iIndexOfFirstOpeningTag == -1 ) | (iIndexOfFirstClosingTag == -1 )):
            if (VERBOSE == True):
                print2("Missing either Opening XML Tag or Closing XML tag")
            # end
            # Save a value of '' fro the current occurrence of the TAg
            aMatchingTagValues.append('')
            
        else:
            # Get the text between the Opening and Closing Tags
            sFoundXMLTagValue = sXML[(iIndexOfFirstOpeningTag + iOpeningTagLength):iIndexOfFirstClosingTag]
            
            if (VERBOSE == True):
                    print2("Found XML tag value: '" + sFoundXMLTagValue + "'")
            # end
            
            # Save the STRING between the Opening and Closing Tags
            aMatchingTagValues.append(sFoundXMLTagValue)
            
        # end - See if either of the Tags...
        
        # Update the XML STRING with the current Closing tag removed
        sXML = sXML[(iIndexOfFirstClosingTag + iClosingTagLength) :]
        
        if (VERBOSE == True):
                print2("Updated XML STRING: '" + sXML + "'")
        # end
        # Update the count of the remaining Closing Tags
        iCurrentTag = sXML.count(sFullClosingTag)
        
        if (VERBOSE == True):
                print2("Remaining number of XML Tags: " + str(iCurrentTag))
        # end
        
    # end - Loop to get that values
    
    return aMatchingTagValues
    
# END method - getXMLTagValue()


#=============================================================================#
#--
# Function: getXMLTagValue(...)
#++
#
# Description:  Parses an XML string containing XML Tags to get the values of the 
#               first occurrence of the specified tag name.
#
#               If more than one occurrence of the specified tag name can exist
#               in the XML string use: getMultipleXMLTagValues()
#                
#               Checks that the Tag exists, NOT if it holds any content.
#               Note that a Closing XML tag </tag_name> with 
#               no Opening tag <tag_name> proceeding it will return None.
#
# Returns: STRING = The STRING between the Opening and Closing XML Tags, or None
#
# Syntax: sXML =  STRING - The string containing the XML tags to be searched.
#         sTagName =  STRING - The name of the XML tags to match. Tags can be
#                              specified with or without the enclosing brackets "<>"
#
# Usage Examples:
#                   sXML = '<response><UserName>Bob</UserName></Nickname></response>'
#
#                   sTagName = "UserName"
#                   getXMLTagValue(sXML, sTag)  #=>  Bob
#
#                   sTagName = "response"       # XML Tag containing other XML Tags
#                   getXMLTagValue(sXML, sTag)  #=>  <UserName>Bob</UserName></Nickname>
#
#                   sTagName = "Nickname"  # Closing XML tag with no Opening Tag
#                   getXMLTagValue(sXML, sTag)  #=>  None
#
#=============================================================================#
def getXMLTagValue(sXML, sTagName):
    '''
    Parses an  XML string containing XML Tags to get the values of the 
    first occurrence of the specified tag name.
    
    If more than one occurrence of the specified tag name can exist
    in the XML string use: getMultipleXMLTagValues()
    
    Note that a Closing XML tag (</tag_name> ) with no Opening XML Tag
    <tag_name> proceeding it will return None
    '''
    
    #VERBOSE = True
    
    if(VERBOSE == True):
        print2("Parameters - getXMLTagValue:")
        print2("  sXML: " + sXML)
        print2("  sTagName: " + sTagName)
    # end
    
    # Verify that the specified tag exists
    if (isTagInXML == False):
        if (VERBOSE == True):
            print2("No tag:  " + sTagName)
        # end
        return None
    # end
    
    # Generate the Opening and Closing XML tags
    
    # Its easier to first remove brackets (if they existed).
    sTagWithoutBrackets = removeXMLBrackets(sTagName)
    
    # Generate the Opening and Closing tags (with brackets)
    aXMLTags = createXMLTags(sTagWithoutBrackets)
    
    sFullOpeningTag = aXMLTags[0]
    sFullClosingTag = aXMLTags[1]
    
    if (VERBOSE == True):
        print2("Opening tag:  " + sFullOpeningTag)
        print2("Closing tag:  " + sFullClosingTag)
    # end
    
    # Determine the length of the Opening and Closing Tags
    iOpeningTagLength = len(sFullOpeningTag)
    iClosingTagLength = len(sFullClosingTag)
    
    if (VERBOSE == True):
        print2("Opening tag length:  " + str(iOpeningTagLength))
        print2("Closing tag length:  " + str(iClosingTagLength))
    # end
    #
    # Find the position of the first character of each Tag in the XML string
    iIndexOfOpeningTag = sXML.find(sFullOpeningTag)
    iIndexOfClosingTag = sXML.find(sFullClosingTag)
    
    if (VERBOSE == True):
        print2("Opening tag index:  " + str(iIndexOfOpeningTag))
        print2("Closing tag index:  " + str(iIndexOfClosingTag))
    # end
    
    # If either of the Tags can't be found, return None
    if ((iIndexOfOpeningTag == -1 ) | (iIndexOfClosingTag == -1 )):
        if (VERBOSE == True):
            print2("Missing either Opening XML Tag or Closing XML tag")
        # end
        return None
    # end
    
    # Save the STRING between the Opening and Closing Tags
    sXMLTagValue = sXML[(iIndexOfOpeningTag + iOpeningTagLength):iIndexOfClosingTag]
    
    return sXMLTagValue
    
# END method - getXMLTagValue()

#=============================================================================#
#--
# Function: isTagInXML(...)
#++
#
# Description:  Parses a string containing XML Tags to see if the specified
#               tag name exists. 
#               Checks that the Tag exists, NOT if it holds any content.
#               Note that a null tag (e.g. a Closing tag </tag_name> with 
#               no Opening tag <tag_name>) will be identified as existing.
#
# Returns: BOOLEAN = True if the Tag exists, otherwise False
#
# Syntax: sXML =  STRING - The string containing the XML tags to be searched.
#         sTagName =  STRING - The name of the XML tags to match. Names can be
#                          specified with or without the enclosing brackets "<>"
#
# Usage Examples:
#                   sXML = '<response><UserName>Bob</UserName></Password></response>'
#                   sTagName = "UserName"
#                   isTagInXML(sXML, sTag)  #=>  True
#
#                   sTagName = "Username"
#                   isTagInXML(sXML, sTag)  #=>  False
#
#                   sTagName = "<UserName>"  # With Brackets
#                   isTagInXML(sXML, sTag)  #=>  True
#
#                   sTagName = "Password"  # With no Opening tag
#                   isTagInXML(sXML, sTag)  #=>  True
#
#=============================================================================#
def isTagInXML(sXML, sTagName):
    '''
    Parse a string containing XML Tags to see if the specified tag name exists.
    Note that a empty closing tag (e.g. </tag_name> ) with no opening  <tag_name> 
    will be identified as existing
    '''
    
    # VERBOSE = True
    
    if(VERBOSE == True):
        print2("Parameters - isTagInXML:")
        print2("  sXML: " + sXML)
        print2("  sTagName: " + sTagName)
    # end
    
    # Set default return value
    bFound = False
    
    # Instead of checking the specified tag for enclosing brackets <tag_name>.
    # ITs easier to just remove them (if they existed) and then adding them.
    sTagWithoutBrackets = removeXMLBrackets(sTagName)
    
    # Generate the Opening and Closing tags (with brackets)
    aXMLTags = createXMLTags(sTagWithoutBrackets)
    
    #sFullOpeningTag = aTags[0]
    sFullClosingTag = aXMLTags[1]
    
    if (VERBOSE == True):
        #print2("Opening tag:  " + sFullOpeningTag)
        print2("Closing tag:  " + sFullClosingTag)
    # end
    
    # Parse the XML String to see if there is a Closing Tag
    # If the Closing tag is found then the tag exists, even if
    # there is no Opening tag
    if(re.search(sFullClosingTag, sXML)):
        bFound = True
    # end
    
    
    return bFound
    
# END method - isTagInXML()



#=============================================================================#
#--
# Function: removeXMLBrackets(...)
#++
#
# Description:  Removes the brackets from Opening or Closing tags
#               Modifies '</tag_name>'  or '<tag_name>'  to 'tag_name' 
#
# Returns: STRING = The modified tag without the brackets
#
# Syntax: sTag =  STRING - The XML tags to strip of the enclosing brackets "<>"
#
# Usage Examples:
#                    sTag = 'UserName'     # Tag name w/o brackets
#                    removeXMLBrackets(sTag)  #=>  UserName
#
#                    sTag = '<Username>'   # Opening tag with Brackets
#                    removeXMLBrackets(sTag)  #=>  UserName
#
#                    sTag = '</UserName>'  # Closing tag with Brackets
#                    removeXMLBrackets(sTag)  #=>  UserName
#
#=============================================================================#
def removeXMLBrackets(sTag):
    '''
    Removes the brackets from Opening or Closing tags
    Modifies '</tag_name>'  or '<tag_name>'  to 'tag_name' 
    '''
    
    #VERBOSE = True
    
    if(VERBOSE == True):
        print2("Parameters - removeBrackets:")
        print2("  sTag: " + sTag)
    # end
    
    # TODO: Improve to ignore brackets within the tag name 
    # Remove the brackets and slash from the Closing tag
    sTag = sTag.replace('</', '')
    #sTag = sTag.replace(r'^</', '')
    
    # Remove the bracket from the Opening tag
    sTag = sTag.replace('<', '')
    #sTag = sTag.replace(r'^<', '')
    
    # Remove the trailing bracket
    sTag = sTag.replace('>', '')
    #sTag = sTag.replace(r'>$', '')
    
    if (VERBOSE == True):
        print2("Tag w/o brackets:  " + sTag)
    # end
    
    return sTag
    
# END method - removeXMLBrackets()


#=============================================================================#
#======================= END =================================================#
#=============================================================================#

# END File - PyWorks_WebUtilities.py
