#!/usr/bin/python
#--
#=============================================================================#
# File: PyWorks_xml_unittest.py
#
# Description: Unit tests for PyWorks WebUtilities methods:
#    createXMLTags(...)
#    getXMLTagValue(...)
#    isTagInXML(..)
#    removeXMLBrackets(...)
#
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
from PyWorks_WebUtilities import *    # PyWorks Web Utilities
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
class UnitTest_WebUtilities(unittest.TestCase):

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
    # end
    
    
    #===========================================================================#
    # Testcase method: test_xml_001_isTagInXML
    #
    # Description: Test the methods:
    #                                isTagInXML(...)
    #                                createXMLTags(...)
    #                                removeXMLBrackets(...)
    #===========================================================================#
    def test_xml_001_isTagInXML(self):
        
        
        '''
        '''
        
        print2("")
        print2("#######################")
        print2("Testcase: test_xml_001_isTagInXML")
        print2("#######################")
        
        if(VERBOSE == True):
            pass
        # end
        
        sXML = '<soapenv:Body><getUserInfoResponse><result><accessibilityMode>false</accessibilityMode><currencySymbol>$</currencySymbol><orgDefaultCurrencyIsoCode>USD</orgDefaultCurrencyIsoCode><orgDisallowHtmlAttachments>false</orgDisallowHtmlAttachments><orgHasPersonAccounts>false</orgHasPersonAccounts><organizationId>00DS00000009AAaMAM</organizationId><organizationMultiCurrency>false</organizationMultiCurrency><organizationName>Qwest (BMG)</organizationName><profileId>00eA0000000tw4dIAA</profileId><roleId>00EA0000000UO5PMAW</roleId><userDefaultCurrencyIsoCode xsi:nil="true"/><userEmail>sfdcitv1@qwest.com</userEmail><userFullName>Sfainttest Sfainttest</userFullName><userId>005S0000000iQPQIA2</userId><userLanguage>en_US</userLanguage><userLocale>en_US</userLocale><userName>sfainttest1@qwest.com.e2e</userName><userTimeZone>America/Denver</userTimeZone><userType>Standard</userType><userUiSkin>Theme3</userUiSkin></result></getUserInfoResponse></soapenv:Body>'
        
        aTags = ["bogus_tag", "<bogus_tag>","</bogus_tag>","userName", "<userName>", "</userName>", "userEmail", "userId", "profileId", "roleId"]
        
        for sTag in aTags:
            
            sTagExists = str(isTagInXML(sXML, sTag))
            print2("Closing Tag for " + sTag + " in XML = " + str(sTagExists))
        # end
        
    # end test_XMLTtest_xml_001_isTagInXML()
    
    
    #===========================================================================#
    # Testcase method: test_xml_002_getXMLTagValue
    #
    # Description: Test the methods:
    #                                getXMLTagValue(...)
    #===========================================================================#
    def test_xml_002_getXMLTagValue(self):
        
        
        '''
        '''
        
        print2("")
        print2("#######################")
        print2("Testcase: test_xml_002_getXMLTagValue")
        print2("#######################")
        
        if(VERBOSE == True):
            pass
        # end
        
        sXML = '<soapenv:Body><getUserInfoResponse><result><accessibilityMode>false</accessibilityMode><currencySymbol>$</currencySymbol><orgDefaultCurrencyIsoCode>USD</orgDefaultCurrencyIsoCode><orgDisallowHtmlAttachments>false</orgDisallowHtmlAttachments><orgHasPersonAccounts>false</orgHasPersonAccounts><organizationId>00DS00000009AAaMAM</organizationId><organizationMultiCurrency>false</organizationMultiCurrency><organizationName>Qwest (BMG)</organizationName><profileId>00eA0000000tw4dIAA</profileId><roleId>00EA0000000UO5PMAW</roleId><userDefaultCurrencyIsoCode xsi:nil="true"/><userEmail>sfdcitv1@qwest.com</userEmail><userFullName>Sfainttest Sfainttest</userFullName><userId>005S0000000iQPQIA2</userId><userLanguage>en_US</userLanguage><userLocale>en_US</userLocale><userName>sfainttest1@qwest.com.e2e</userName><userTimeZone>America/Denver</userTimeZone><userType>Standard</userType><userUiSkin>Theme3</userUiSkin></a_null_tag></result></getUserInfoResponse></soapenv:Body>'
        
        aTags = ["bogus_tag", "<bogus_tag>","</bogus_tag>","userName", "<userName>", "</userName>", "userEmail", "userId", "profileId", "roleId", "a_null_tag", "result"]
        
        for sTag in aTags:
            
            sXMLTagValue = str(getXMLTagValue(sXML, sTag))
            print2("Value of XML Tag '" + sTag + "' in XML = '" + sXMLTagValue + "'")
        # end
        
    # end test_xml_002_getXMLTagValue()(...)


    #===========================================================================#
    # Testcase method: test_xml_003_getMultipleXMLTagValues
    #
    # Description: Test the methods:
    #                                getMultipleXMLTagValues(...)
    #===========================================================================#
    def test_xml_003_getMultipleXMLTagValues(self):
        
        
        '''
        '''
        
        print2("")
        print2("#######################")
        print2("Testcase: test_xml_003_getMultipleXMLTagValues")
        print2("#######################")
        
        if(VERBOSE == True):
            pass
        # end
        
        sXML = '<soapenv:Body><getUserInfoResponse><result><userName><FirstName>Bob</FirstName><userId>01</userId></userName><userName><FirstName>Tom</FirstName><userId>02</userId></userName></a_null_tag></result></getUserInfoResponse></soapenv:Body>'
        
        #sXML = '<soapenv:Body><getUserInfoResponse><result><accessibilityMode>false</accessibilityMode><currencySymbol>$</currencySymbol><orgDefaultCurrencyIsoCode>USD</orgDefaultCurrencyIsoCode><orgDisallowHtmlAttachments>false</orgDisallowHtmlAttachments><orgHasPersonAccounts>false</orgHasPersonAccounts><organizationId>00DS00000009AAaMAM</organizationId><organizationMultiCurrency>false</organizationMultiCurrency><organizationName>Qwest (BMG)</organizationName><profileId>00eA0000000tw4dIAA</profileId><roleId>00EA0000000UO5PMAW</roleId><userDefaultCurrencyIsoCode xsi:nil="true"/><userEmail>sfdcitv1@qwest.com</userEmail><userFullName>Sfainttest Sfainttest</userFullName><userId>005S0000000iQPQIA2</userId><userLanguage>en_US</userLanguage><userLocale>en_US</userLocale><userName>sfainttest1@qwest.com.e2e</userName><userTimeZone>America/Denver</userTimeZone><userType>Standard</userType><userUiSkin>Theme3</userUiSkin></a_null_tag></result></getUserInfoResponse></soapenv:Body>'
        
        aTags = ["bogus_tag", "<bogus_tag>","</bogus_tag>","userName", "<userName>", "</userName>", "FirstName", "userId", "userEmail", "a_null_tag", "result"]
        
        for sTag in aTags:
            
            sXMLTagValue = str(getMultipleXMLTagValues(sXML, sTag))
            print2("Value of XML Tag '" + sTag + "' in XML = '" + sXMLTagValue + "'")
        # end
        
        print2("-"*15)
        
        sXML = '<env:Body> <CreateProjectTasksRequest xmlns="http://com/qwest/qcworkflow/service"> <OpportunityId>50025454</OpportunityId> <PrimaryRepId>A6W0</PrimaryRepId> <SecondaryRepId xsi:nil="true" /> <LoggedInSalesRepId xsi:nil="true" /> <LoggedInCUID>rxpras2</LoggedInCUID> <CustomerName>Testing_QNDC</CustomerName> <CustomerHubUUID>123545245234</CustomerHubUUID> <CompanyMainAddr> <StreetAddr1>700 W mineral Ave</StreetAddr1> <StreetAddr2 xsi:nil="true" /> <PostalCd>80120</PostalCd> <City>Littleton</City> <StateCd>CO</StateCd> <Country>USA</Country> </CompanyMainAddr> <QCID>1234567890</QCID> <CompanyMainPhone>(720) 229-0655</CompanyMainPhone> <CompanyMainFax xsi:nil="true" /> <SalesChannelId>1</SalesChannelId> <BusinessProcessType>BMG</BusinessProcessType> <ContactList> <Contact xsi:nil="true" /> <Contact> <ContactType>RATE</ContactType> <ContactName xsi:nil="true" /> <Phone xsi:nil="true" /> <Fax xsi:nil="true" /> <Pager xsi:nil="true" /> <Email xsi:nil="true" /> </Contact> <Contact> <ContactType>LEGAL</ContactType> <ContactName xsi:nil="true" /> <Phone xsi:nil="true" /> <Fax xsi:nil="true" /> <Pager xsi:nil="true" /> <Email xsi:nil="true" /> </Contact> <Contact> <ContactType>CONTR</ContactType> <ContactName xsi:nil="true" /> <Phone xsi:nil="true" /> <Fax xsi:nil="true" /> <Pager xsi:nil="true" /> <Email xsi:nil="true" /> </Contact> <Contact> <ContactType>OPPTY</ContactType> <ContactName xsi:nil="true" /> <Phone xsi:nil="true" /> <Fax xsi:nil="true" /> <Pager xsi:nil="true" /> <Email xsi:nil="true" /> </Contact> </ContactList> <QuoteList> <Quote> <QoaRequestId>235847637</QoaRequestId> <OfferingId>5076</OfferingId> <QuoteSourceCode>DETAIL</QuoteSourceCode> <TaskTypeCode>OAEID</TaskTypeCode> <ServiceCategoryCode>CPE</ServiceCategoryCode> </Quote> </QuoteList> </CreateProjectTasksRequest> </env:Body> '
        aTags = ["Contact"]
        
        for sTag in aTags:
            
            sXMLTagValue = str(getMultipleXMLTagValues(sXML, sTag))
            print2("Value of XML Tag '" + sTag + "' in XML = '" + sXMLTagValue + "'")
        # end
        
        print2("-"*15)
        sXML = '<env:Body> <n1:CIESubmitForApprovalResponse xmlns:n1="http://www.qwest.com/CIE/xsd"> <n1:CIEId xsi:nil="true"></n1:CIEId> <n1:CIEStatus xsi:nil="true"></n1:CIEStatus> <n1:OpportunityId xsi:nil="true"></n1:OpportunityId> <n1:MsgResponseCd>2</n1:MsgResponseCd> <n1:MsgResponseDesc>CIE Request must include a direct rep and at least one partner (QC or QCC) rep</n1:MsgResponseDesc> <n1:MsgResponseDesc>Federal CIE Request must include Federal Account Manager Id</n1:MsgResponseDesc> </n1:CIESubmitForApprovalResponse> </env:Body>'
        aTags = ["n1:MsgResponseDesc"]
        
        for sTag in aTags:
            
            sXMLTagValue = str(getMultipleXMLTagValues(sXML, sTag))
            print2("Value of XML Tag '" + sTag + "' in XML = '" + sXMLTagValue + "'")
        # end
         

    # end test_xml_003_getMultipleXMLTagValues()(...)
    
# End of class - UnitTest_WebUtilities

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest_WebUtilities)
unittest.TextTestRunner(verbosity=2).run(suite)
