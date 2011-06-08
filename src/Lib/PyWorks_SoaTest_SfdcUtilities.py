#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_SoaTest_SfdcUtilities.py
#
#  Copyright (c) 2008-2011, Joe DiMauro
#  All rights reserved.
#
# Description: Functions and methods for PyWorks
#    These functions and methods are platform independent,
#    but are specific to the SOATest and Salesforce.com (SFDC) Web applications.
#
# Instructions: To use these methods in your scripts add these commands:
#                        from PyWorks_SoaTest_SfdcUtilities import *    # PyWorks SOAtest/Salesforce Utilities
#--
# Table of Contents
#
#  Please manually update this TOC with the alphabetically sorted names of the items in this module,
#  and continue to add new methods alphabetically into their proper location within the module.
#
#  Key:   () = No parameters,  (...) = parameters required
#
# Functions:
#    findSfdcObjectID(...)
#    getSfdcAccountIds(...)
#    getSfdcContactIds(...)
#    getSfdcLeadIds(...)
#    getSfdcOpportunityIds(...)
#    getSfdcProfileIds(...)
#    getSfdcRoleIds(...)
#    getSfdcUserIds(...)
#    sfdc_StoreDictInSoaTestVar(...)
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
#import re                           # Regular expressions

# PyWorks imports
#from PyWorks_Reflib import TIMESTAMP_STRING
from PyWorks_Utilities import is_SOATest, print2, getMatchingKeyValue         # PyWorks General Utilities
from PyWorks_WebUtilities import getMultipleXMLTagValues     # PyWorks Web Utilities

#
# SOATest imports
if(is_SOATest()):
    from com.parasoft.api import *
# End

#=============================================================================#

# Version of this module
PW_SOATEST_SFDC_UTILITIES_VERSION = "1.0.0"

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
# Function: findSfdcObjectId(...)
#++
#
# Description: Reads a SOATest Project Variable that contains a DICT of an SFDC Object's Name:Id pairs,
#              Searches the DICT for a Key that matches the specified Object's Name
#              Returns a LIST with the matching Object Name and it's ID value.
#
# Returns: LIST    - LIST[0] = STRING - The matching Key
#                    LIST[1] = STRING - The matching Key's Value
#
# Syntax: sReadVariableName = STRING - The name of the SOATest Variable that contains
#                                        the Dictionary of Name:Id pairs to search
#         sNameKey = STRING - The Key name to search for (May be a partial match)
#         bCaseSensitive = BOLEAN - True to perform a case sensitive search for the Key, False to ignore case
#
# Prerequisites:
#    1. This Function must be called from within a SOATest Extension
#    2. A Query of the SFDC Object for the Name and ID values was made by a previous SOATest test.
#    3. The SOAP Response from that query was saved as a DICT of Name:Id pairs into a SOATest Variable
#    4. Call this function from a SOAtest Extension, by referencing this file, and selecting this function.
#
# Usage Examples:
#
#=============================================================================#
def findSfdcObjectId(context, sReadVariableName, sNameKey, bCaseSensitive=True):
    '''
    RReads a SOATest Project Variable that contains a DICT of an SFDC Object's Name:Id pairs,
    Searches the DICT for a Key that matches the specified Object's Name 
    Returns a LIST with the matching Object Name and it's ID value.
    '''
    
    # VERBOSE = True
    
    # Set a default value
    aMatchingNameValuePair = ["", ""]
    
    # Retrieve the DICT from the SOATest variable
    hNameValuePairs = context.get(sReadVariableName)
    
    # Perform the Search
    aMatchingNameValuePair =  getMatchingKeyValue(hNameValuePairs,sNameKey, bCaseSensitive)
    
    if(VERBOSE == True):
        print2("\tFound Name:Id pair of..")
        print2(aMatchingNameValuePair)
    # end
    
    return aMatchingNameValuePair

# ENd - Function - findSfdcObjectId

#=============================================================================#
#--
# Function: getSfdcAccountIds(...)
#++
#
# Description: Reads the SFDC Account Name and ID values saved in a
#              SOATest Data Source, creates a DICT object from them,
#              and saves the DICT into a SOATest Project Variable that
#              can be used elsewhere in SOATest to lookup the Id based on 
#              its associated Name.
#
# Returns: BOOLEAN - True on success, otherwise False
#
# Prerequisites:
#    1. This Function must be called from within a SOATest Extension
#    2. A Query of the SFDC Object for the Name and ID values was made by a previous SOATest test.
#    3. The SOAP Response from that query was saved into a SOATest Data Source
#    4. Call this function from a SOAtest Extension, by referencing this file, and
#       selecting this function.
#=============================================================================#
def getSfdcAccountIds(input, context):
    
    #from PyWorks_SoaTest_SfdcUtilities import sfdc_StoreDictInSoaTestVar    # PyWorks SOATest for Salesforce.com Utilities
    #from PyWorks_WebUtilities import *
    
    
    #VERBOSE = True
    
    sReadSoaTestDataSourceName = "SFDC Saved Data"
    sReadVariableName = "SFDC: QueryAccount_XML"
    sWriteSoaTestDataSourceName = "SFDC Saved Data"
    sWriteVariableName = "SFDC: AccountIds"
    sTagNameKey = "sf:Name"
    sTagNameValue = "sf:Id"
    
    print2("\tSaving SFDC Account's Name and ID")
    
    # Set the return of this function status based on the return status of the called function
    bStatus = sfdc_StoreDictInSoaTestVar(context, sReadSoaTestDataSourceName, sReadVariableName, sWriteSoaTestDataSourceName, sWriteVariableName, sTagNameKey, sTagNameValue)
    
    if(VERBOSE == True):
        # Read back the saved DICT 
        hUserIDs = context.get(sWriteVariableName)
    
        #print2("\tSaved value '" + str(hUserIDs) + "'")
        print2("\tEntries in DICT = " + str(len(hUserIDs)))
        print2("\tIterate over the DICT '" + sWriteVariableName + "'")
    
        for sKey, sValue in hUserIDs.iteritems():
            print2("\t\t" + sKey + " = " + sValue)
        # end
    # end
    
    return bStatus

# End - Function - getSfdcAccountIds()


#=============================================================================#
#--
# Function: getSfdcContactIds(...)
#++
#
# Description: Reads the SFDC Contact Name and ID values saved in a
#              SOATest Data Source, creates a DICT object from them,
#              and saves the DICT into a SOATest Project Variable that
#              can be used elsewhere in SOATest to lookup the Id based on 
#              its associated Name.
#
# Returns: BOOLEAN - True on success, otherwise False
#
# Prerequisites:
#    1. This Function must be called from within a SOATest Extension
#    2. A Query of the SFDC Object for the Name and ID values was made by a previous SOATest test.
#    3. The SOAP Response from that query was saved into a SOATest Data Source
#    4. Call this function from a SOAtest Extension, by referencing this file, and
#       selecting this function.
#=============================================================================#
def getSfdcContactIds(input, context):
    
    #from PyWorks_SoaTest_SfdcUtilities import sfdc_StoreDictInSoaTestVar    # PyWorks SOATest for Salesforce.com Utilities
    #from PyWorks_WebUtilities import *
    
    
    #VERBOSE = True
    
    sReadSoaTestDataSourceName = "SFDC Saved Data"
    sReadVariableName = "SFDC: QueryContact_XML"
    sWriteSoaTestDataSourceName = "SFDC Saved Data"
    sWriteVariableName = "SFDC: ContactIds"
    sTagNameKey = "sf:Name"
    sTagNameValue = "sf:Id"
    
    print2("\tSaving SFDC Contact's Name and ID")
    
    # Set the return of this function status based on the return status of the called function
    bStatus = sfdc_StoreDictInSoaTestVar(context, sReadSoaTestDataSourceName, sReadVariableName, sWriteSoaTestDataSourceName, sWriteVariableName, sTagNameKey, sTagNameValue)
    
    if(VERBOSE == True):
        # Read back the saved DICT 
        hUserIDs = context.get(sWriteVariableName)
    
        #print2("\tSaved value '" + str(hUserIDs) + "'")
        print2("\tEntries in DICT = " + str(len(hUserIDs)))
        print2("\tIterate over the DICT '" + sWriteVariableName + "'")
    
        for sKey, sValue in hUserIDs.iteritems():
            print2("\t\t" + sKey + " = " + sValue)
        # end
    # end
    
    return bStatus

# End - Function - getSfdcAccountIds()


#=============================================================================#
#--
# Function: getSfdcLeadIds(...)
#++
#
# Description: Reads the SFDC Lead Name and ID values saved in a
#              SOATest Data Source, creates a DICT object from them,
#              and saves the DICT into a SOATest Project Variable that
#              can be used elsewhere in SOATest to lookup the Id based on 
#              its associated Name.
#
# Returns: BOOLEAN - True on success, otherwise False
#
# Prerequisites:
#    1. This Function must be called from within a SOATest Extension
#    2. A Query of the SFDC Object for the Name and ID values was made by a previous SOATest test.
#    3. The SOAP Response from that query was saved into a SOATest Data Source
#    4. Call this function from a SOAtest Extension, by referencing this file, and
#       selecting this function.
#=============================================================================#
def getSfdcLeadIds(input, context):
    
    #from PyWorks_SoaTest_SfdcUtilities import sfdc_StoreDictInSoaTestVar    # PyWorks SOATest for Salesforce.com Utilities
    #from PyWorks_WebUtilities import *
    
    
    #VERBOSE = True
    
    sReadSoaTestDataSourceName = "SFDC Saved Data"
    sReadVariableName = "SFDC: QueryLead_XML"
    sWriteSoaTestDataSourceName = "SFDC Saved Data"
    sWriteVariableName = "SFDC: LeadIds"
    sTagNameKey = "sf:Name"
    sTagNameValue = "sf:Id"
    
    print2("\tSaving SFDC Lead's Name and ID")
    
    # Set the return of this function status based on the return status of the called function
    bStatus = sfdc_StoreDictInSoaTestVar(context, sReadSoaTestDataSourceName, sReadVariableName, sWriteSoaTestDataSourceName, sWriteVariableName, sTagNameKey, sTagNameValue)
    
    if(VERBOSE == True):
        # Read back the saved DICT 
        hUserIDs = context.get(sWriteVariableName)
    
        #print2("\tSaved value '" + str(hUserIDs) + "'")
        print2("\tEntries in DICT = " + str(len(hUserIDs)))
        print2("\tIterate over the DICT '" + sWriteVariableName + "'")
    
        for sKey, sValue in hUserIDs.iteritems():
            print2("\t\t" + sKey + " = " + sValue)
        # end
    # end
    
    return bStatus

# End - Function - getSfdcAccountIds()


#=============================================================================#
#--
# Function: getSfdcOpportunityIds(...)
#++
#
# Description: Reads the SFDC Opportunity Name and ID values saved in a
#              SOATest Data Source, creates a DICT object from them,
#              and saves the DICT into a SOATest Project Variable that
#              can be used elsewhere in SOATest to lookup the Id based on 
#              its associated Name.
#
# Returns: BOOLEAN - True on success, otherwise False
#
# Prerequisites:
#    1. This Function must be called from within a SOATest Extension
#    2. A Query of the SFDC Object for the Name and ID values was made by a previous SOATest test.
#    3. The SOAP Response from that query was saved into a SOATest Data Source
#    4. Call this function from a SOAtest Extension, by referencing this file, and
#       selecting this function.
#=============================================================================#
def getSfdcOpportunityIds(input, context):
    
    #from PyWorks_SoaTest_SfdcUtilities import sfdc_StoreDictInSoaTestVar    # PyWorks SOATest for Salesforce.com Utilities
    #from PyWorks_WebUtilities import *
    
    
    #VERBOSE = True
    
    sReadSoaTestDataSourceName = "SFDC Saved Data"
    sReadVariableName = "SFDC: QueryOpportunity_XML"
    sWriteSoaTestDataSourceName = "SFDC Saved Data"
    sWriteVariableName = "SFDC: OpportunityIds"
    sTagNameKey = "sf:Name"
    sTagNameValue = "sf:Id"
    
    print2("\tSaving SFDC Opportunity's Name and ID")
    
    # Set the return of this function status based on the return status of the called function
    bStatus = sfdc_StoreDictInSoaTestVar(context, sReadSoaTestDataSourceName, sReadVariableName, sWriteSoaTestDataSourceName, sWriteVariableName, sTagNameKey, sTagNameValue)
    
    if(VERBOSE == True):
        # Read back the saved DICT 
        hUserIDs = context.get(sWriteVariableName)
    
        #print2("\tSaved value '" + str(hUserIDs) + "'")
        print2("\tEntries in DICT = " + str(len(hUserIDs)))
        print2("\tIterate over the DICT '" + sWriteVariableName + "'")
    
        for sKey, sValue in hUserIDs.iteritems():
            print2("\t\t" + sKey + " = " + sValue)
        # end
    # end
    
    return bStatus

# End - Function - getSfdcAccountIds()


#=============================================================================#
#--
# Function: getSfdcProfileIds(...)
#++
#
# Description: Reads the SFDC Profile Name and ID values saved in a
#              SOATest Data Source, creates a DICT object from them,
#              and saves the DICT into a SOATest Project Variable that
#              can be used elsewhere in SOATest to lookup the Id based on 
#              its associated Name.
#
# Returns: BOOLEAN - True on success, otherwise False
#
# Prerequisites:
#    1. This Function must be called from within a SOATest Extension
#    2. A Query of the SFDC Object for the Name and ID values was made by a previous SOATest test.
#    3. The SOAP Response from that query was saved into a SOATest Data Source
#    4. Call this function from a SOAtest Extension, by referencing this file, and
#       selecting this function.
#=============================================================================#
def getSfdcProfileIds(input, context):
    
    #from PyWorks_SoaTest_SfdcUtilities import sfdc_StoreDictInSoaTestVar    # PyWorks SOATest for Salesforce.com Utilities
    #from PyWorks_WebUtilities import *
    
    
    #VERBOSE = True
    
    sReadSoaTestDataSourceName = "SFDC Saved Data"
    sReadVariableName = "SFDC: QueryProfile_XML"
    sWriteSoaTestDataSourceName = "SFDC Saved Data"
    sWriteVariableName = "SFDC: ProfileIds"
    sTagNameKey = "sf:Name"
    sTagNameValue = "sf:Id"
    
    print2("\tSaving SFDC Profile's Name and ID")
    
    # Set the return of this function status based on the return status of the called function
    bStatus = sfdc_StoreDictInSoaTestVar(context, sReadSoaTestDataSourceName, sReadVariableName, sWriteSoaTestDataSourceName, sWriteVariableName, sTagNameKey, sTagNameValue)
    
    if(VERBOSE == True):
        # Read back the saved DICT 
        hUserIDs = context.get(sWriteVariableName)
    
        #print2("\tSaved value '" + str(hUserIDs) + "'")
        print2("\tEntries in DICT = " + str(len(hUserIDs)))
        print2("\tIterate over the DICT '" + sWriteVariableName + "'")
    
        for sKey, sValue in hUserIDs.iteritems():
            print2("\t\t" + sKey + " = " + sValue)
        # end
    # end
    
    return bStatus

# End - Function - getSfdcAccountIds()


#=============================================================================#
#--
# Function: getSfdcRoleIds(...)
#++
#
# Description: Reads the SFDC Role Name and ID values saved in a
#              SOATest Data Source, creates a DICT object from them,
#              and saves the DICT into a SOATest Project Variable that
#              can be used elsewhere in SOATest to lookup the Id based on 
#              its associated Name.
#
# Returns: BOOLEAN - True on success, otherwise False
#
# Prerequisites:
#    1. This Function must be called from within a SOATest Extension
#    2. A Query of the SFDC Object for the Name and ID values was made by a previous SOATest test.
#    3. The SOAP Response from that query was saved into a SOATest Data Source
#    4. Call this function from a SOAtest Extension, by referencing this file, and
#       selecting this function.
#=============================================================================#
def getSfdcRoleIds(input, context):
    
    #from PyWorks_SoaTest_SfdcUtilities import sfdc_StoreDictInSoaTestVar    # PyWorks SOATest for Salesforce.com Utilities
    #from PyWorks_WebUtilities import * 
    
    
    #VERBOSE = True
    
    sReadSoaTestDataSourceName = "SFDC Saved Data"
    sReadVariableName = "SFDC: QueryRole_XML"
    sWriteSoaTestDataSourceName = "SFDC Saved Data"
    sWriteVariableName = "SFDC: RoleIds"
    sTagNameKey = "sf:Name"
    sTagNameValue = "sf:Id"
   
    print2("\tSaving SFDC Role's Name and ID")
    
    # Set the return of this function status based on the return status of the called function
    bStatus = sfdc_StoreDictInSoaTestVar(context, sReadSoaTestDataSourceName, sReadVariableName, sWriteSoaTestDataSourceName, sWriteVariableName, sTagNameKey, sTagNameValue)
    
    if(VERBOSE == True):
        # Read back the saved DICT 
        hUserIDs = context.get(sWriteVariableName)
    
        #print2("\tSaved value '" + str(hUserIDs) + "'")
        print2("\tEntries in DICT = " + str(len(hUserIDs)))
        print2("\tIterate over the DICT '" + sWriteVariableName + "'")
    
        for sKey, sValue in hUserIDs.iteritems():
            print2("\t\t" + sKey + " = " + sValue)
        # end
    # end
    
    return bStatus

# End - Function - getSfdcAccountIds()


#=============================================================================#
#--
# Function: getSfdcUserIds(...)
#++
#
# Description: Reads the SFDC User Name and ID values saved in a
#              SOATest Data Source, creates a DICT object from them,
#              and saves the DICT into a SOATest Project Variable that
#              can be used elsewhere in SOATest to lookup the Id based on 
#              its associated Name.
#
# Returns: BOOLEAN - True on success, otherwise False
#
# Prerequisites:
#    1. This Function must be called from within a SOATest Extension
#    2. A Query of the SFDC Object for the Name and ID values was made by a previous SOATest test.
#    3. The SOAP Response from that query was saved into a SOATest Data Source
#    4. Call this function from a SOAtest Extension, by referencing this file, and
#       selecting this function.
#=============================================================================#
def getSfdcUserIds(input, context):
    
    #from PyWorks_SoaTest_SfdcUtilities import sfdc_StoreDictInSoaTestVar    # PyWorks SOATest for Salesforce.com Utilities
    #from PyWorks_WebUtilities import * 
    
    #VERBOSE = True
    
    sReadSoaTestDataSourceName = "SFDC Saved Data"
    sReadVariableName = "SFDC: QueryUser_XML"
    sWriteSoaTestDataSourceName = "SFDC Saved Data"
    sWriteVariableName = "SFDC: UserIds"
    sTagNameKey = "sf:Username"
    sTagNameValue = "sf:Id"
   
    print2("\tSaving SFDC User's Name and ID")
    
    # Set the return of this function status based on the return status of the called function
    bStatus = sfdc_StoreDictInSoaTestVar(context, sReadSoaTestDataSourceName, sReadVariableName, sWriteSoaTestDataSourceName, sWriteVariableName, sTagNameKey, sTagNameValue)
    
    if(VERBOSE == True):
        # Read back the saved DICT 
        hUserIDs = context.get(sWriteVariableName)
    
        #print2("\tSaved value '" + str(hUserIDs) + "'")
        print2("\tEntries in DICT = " + str(len(hUserIDs)))
        print2("\tIterate over the DICT '" + sWriteVariableName + "'")
    
        for sKey, sValue in hUserIDs.iteritems():
            print2("\t\t" + sKey + " = " + sValue)
        # end
    # end
    
    return bStatus

# End - Function - getSfdcAccountIds()


#=============================================================================#
#--
# Function: sfdc_StoreDictInSoaTestVar(...)
#++
#
# Description:  Saves the specified XML Tag settings as Key and Values of a DICT Object into
#               a specified SOATest Variable in the specified SOATest Data Source.
# 
#                The Name and ID values are parsed from the XML of a SOAP response 
#                that was obtained by using the SFDC Enterprise WSDL call like:
#                     query('SELECT Id, Name FROM role')
#                        or
#                     query('SELECT Id, Name FROM profile')
#                and saved into a SOATest Data Source as a Project variable.
#
# Returns: BOOLEAN - True if successful, otherwise False
#
# Syntax:    sReadSoaTestDataSourceName = STRING - The name of the SOATest Data Source to read from
#            sReadVariableName = STRING - The name of the Variable in that Data Source that
#                                            holds the XML from the SOAP response returned by the
#                                            SFDC Enterprise WSDL call like:
#                                                query('SELECT Id, Name FROM role')
#                                                    or
#                                                query('SELECT Id, Name FROM profile')
#            
#            sTagNameKey = STRING - The XML Tag who's setting will be saved as the Key in the DICT
#            sTagNameValue = STRING - The XML Tag who's setting will be saved as the Value in the DICT
#            
#            sWriteSoaTestDataSourceName = STRING -The name of the SOATest Data Source to write to
#            sWriteVariableName = STRING - The name of the Variable in that Data Source that
#                                                will holds HASH of the Name and ID values
#
# Usage Examples:
#                After saving the SOAP Response containing the XML of the Profile Id and Name into a 
#                SOATest Data Table Variable; To store the Id and Name of the Profile's in different SOATest
#                Variable in the same Data Table: 
#                    sfdc_StoreDictInSoaTestVar("SFDC_SAVED_DATA","sSoapResponse","SFDC_SAVED_DATA", "hProfileIDs","Id", "Name")
#
#                After saving the SOAP Response containing the XML of the Role Id and Name into a 
#                SOATest Data Table Variable; To store the Id and Name of the Profile's in different SOATest
#                Variable in the same Data Table: 
#                    sfdc_StoreDictInSoaTestVar("SFDC_SAVED_DATA","sSoapResponse","SFDC_SAVED_DATA", "hRoleIDs","Id", "Name")

#
#=============================================================================#
def sfdc_StoreDictInSoaTestVar(context, sReadSoaTestDataSourceName, sReadVariableName, sWriteSoaTestDataSourceName, sWriteVariableName, sTagNameKey="Id", sTagNameValue="Name"):
    '''
    Saves the specified XML Tag settings as Key and Values of a DICT Object into
    a specified SOATest Variable in the specified SOATest Data Source.
    '''
    
    #VERBOSE = True
    
    if(VERBOSE == True):
        print2("Parameters - sfdc_StoreDictInSoaTestVar:")
        print2("  sReadSoaTestDataSourceName: " + sReadSoaTestDataSourceName)
        print2("  sReadVariableName: " + sReadVariableName)
        print2("  sTagNameKey: " + sTagNameKey)
        print2("  sTagNameValue: " + sTagNameValue)
        print2("  sWriteSoaTestDataSourceName: " + sWriteSoaTestDataSourceName)
        print2("  sWriteVariableName: " + sWriteVariableName)
    # end
    
    # Read the SOAP Response XML STRING from the SOATest Data Source
    sXML = str(context.getValue(sReadSoaTestDataSourceName, sReadVariableName))
    
    
    if(VERBOSE == True):
        pass
        print2("XML '" + sXML + "'")
    # end
    
    # Parse the Tag settings to use as the Key into a LIST
    aKeyList = getMultipleXMLTagValues(sXML, sTagNameKey)
    
    # Parse the Tag settings to use as the Value into a LIST
    aValueList = getMultipleXMLTagValues(sXML, sTagNameValue)
    
    if(VERBOSE == True):
        print2("aKeyList '" + str(aKeyList) + "'" )
        print2("aValueList '" + str(aValueList) + "'" )
    # end
    
    # Create a DICT from the two LIST objects
    hLookupDict = dict(zip(aKeyList, aValueList))
    
    if(VERBOSE == True):
        pass
        print2("DICT ...")
        print2(str(hLookupDict))
    # end
    
    # Save the DICT into a SOATest Data Source
    context.put(sWriteVariableName, hLookupDict)
    
    return True
    
# END method - sfdc_StoreDictInSoaTestVar()


#=============================================================================#
#======================= END =================================================#
#=============================================================================#

# END File - PyWorks_SoaTest_SfdcUtilities.py
