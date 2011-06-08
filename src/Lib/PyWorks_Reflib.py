#!/usr/bin/python
#=============================================================================#
# File: PyWorks_Reflib.py
#
#  Copyright (c) 2008-2011, Joe DiMauro
#  All rights reserved.
#
# Description: Reference data that is platform and application independent.
#
#--
#
#++
#=============================================================================#

#=============================================================================#
# Import section
# Entries for additional files or methods needed by these methods
#=============================================================================#
from datetime import date, timedelta # Add ability to get/format Dates
import time


#=============================================================================#
# RefLib
#=============================================================================#
#
# Description:  Reference data that is platform and application independent.
#
#               For example, use the Dictionary table USPS_STATES to lookup
#               the full name of a state from its abbreviation.
#
# Instructions: To use the reference data in your scripts, add these commands:
#
#                  # PyWorks
#                  from PyWorks_RefLib import *   # PyWorks Reference Library
#
#--
# Roadmap: Perhaps add other Geo-specific Data like: Countries, Continents, Capitals, Cities, Counties, Planets?
#          Weights & Measures conversion chart? (MileToFeet = 5280)
#          Astrological Signs?, who knows, so long as its useful.
#          For example: Geo-political data is available at:
#              https://www.cia.gov/library/publications/the-world-factbook/
#++
#=============================================================================#
  
# Version of this module
PW_REFLIB_VERSION = "1.0.2"

#
# Common string representations of time constants for year, month, and day
# Year strings (yyyy)
global THIS_YEAR
THIS_YEAR = str(date.today().year)
global NEXT_YEAR
NEXT_YEAR = str(date.today().year + 1)
global LAST_YEAR
LAST_YEAR = str(date.today().year - 1)
 
# Define strings with only the last 2-digits of the year (e.g. 08 for 2008)
# Remember for strings index 1 is the 1st character
global THIS_YR
THIS_YR = str(time.strftime("%y"))
global NEXT_YR
NEXT_YR = str(date.today().year + 1)[2:]  # All but the first 2 characters
global LAST_YR
LAST_YR = str(date.today().year - 1)[2:4] # The third and 4th characters

# This month string (01-12)
global THIS_MONTH
THIS_MONTH = str(date.today().month)

# This Day string (01-31)
global THIS_DAY
THIS_DAY = str(date.today().day)

# Define the format for date strings
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
sDateformat = "%m/%d/%Y"  # e.g. 12/31/2011
#sDateformat = "%Y-%m-%d" # e.g. 2011-12-31

# Set the current date
dToday = date.today()

# Calculate various strings representations of dates (both future and past) based on the current date
# Syntax:
        # class timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[,hours[,weeks]]]]]]])
global TODAY
TODAY = dToday.strftime(sDateformat)
global TOMORROW
TOMORROW = (dToday + (timedelta(days=1))).strftime(sDateformat)
global YESTERDAY
YESTERDAY = (dToday - (timedelta(days=1))).strftime(sDateformat)
global DAYS_FUTURE_7
DAYS_FUTURE_7 = (dToday + (timedelta(days=7))).strftime(sDateformat)
global DAYS_PAST_7
DAYS_PAST_7 = (dToday - (timedelta(days=7))).strftime(sDateformat)
global DAYS_FUTURE_30
DAYS_FUTURE_30 = (dToday + (timedelta(days=30))).strftime(sDateformat)
global DAYS_PAST_30
DAYS_PAST_30 = (dToday - (timedelta(days=30))).strftime(sDateformat)
global DAYS_FUTURE_60
DAYS_FUTURE_60 = (dToday + (timedelta(days=60))).strftime(sDateformat)
global DAYS_PAST_60
DAYS_PAST_60 = (dToday - (timedelta(days=60))).strftime(sDateformat)
global DAYS_FUTURE_90
DAYS_FUTURE_90 = (dToday + (timedelta(days=90))).strftime(sDateformat)
global DAYS_PAST_90
DAYS_PAST_90 = (dToday - (timedelta(days=90))).strftime(sDateformat)
global DAYS_FUTURE_365
DAYS_FUTURE_365 = (dToday + (timedelta(days=365))).strftime(sDateformat)
global DAYS_PAST_365
DAYS_PAST_365 = (dToday - (timedelta(days=365))).strftime(sDateformat)

global WEEKS_FUTURE_1
WEEKS_FUTURE_1 = (dToday + (timedelta(weeks=1))).strftime(sDateformat)
global WEEKS_FUTURE_2
WEEKS_FUTURE_2 = (dToday + (timedelta(weeks=2))).strftime(sDateformat)
global WEEKS_FUTURE_4
WEEKS_FUTURE_4 = (dToday + (timedelta(weeks=4))).strftime(sDateformat)
global WEEKS_FUTURE_8
WEEKS_FUTURE_8 = (dToday + (timedelta(weeks=8))).strftime(sDateformat)
global WEEKS_FUTURE_12
WEEKS_FUTURE_12 = (dToday + (timedelta(weeks=12))).strftime(sDateformat)
global WEEKS_FUTURE_52
WEEKS_FUTURE_52 = (dToday + (timedelta(weeks=52))).strftime(sDateformat)
global WEEKS_PAST_1
WEEKS_PAST_1 = (dToday - (timedelta(weeks=1))).strftime(sDateformat)
global WEEKS_PAST_2
WEEKS_PAST_2 = (dToday - (timedelta(weeks=2))).strftime(sDateformat)
global WEEKS_PAST_4
WEEKS_PAST_4 = (dToday - (timedelta(weeks=4))).strftime(sDateformat)
global WEEKS_PAST_8
WEEKS_PAST_8 = (dToday - (timedelta(weeks=8))).strftime(sDateformat)
global WEEKS_PAST_12
WEEKS_PAST_12 = (dToday - (timedelta(weeks=12))).strftime(sDateformat)
global WEEKS_PAST_52
WEEKS_PAST_52 = (dToday - (timedelta(weeks=52))).strftime(sDateformat)


    
# Save the current time to be used Globally for all test in a suite.
#
# This will ensure that the same time can be used throughout all the tests, and ensures
# that if a STRING is created at one point in the test with a timestamp appended to it,
# that the same timestamp can be re-used at subsequent points in all tests within a testsuite.
global TESTSUITE_START_TIME
TESTSUITE_START_TIME = time.asctime(time.localtime(time.time()))

# Define timestamp format for use with file names
# The timestamp of 14 characters can be appended to a file name (e.g. mylogfile_2007_Dec_30_235959.log)
# Example: sMyPrefix = "mylogfile"
#          sMyExtension = ".log"
#          sMyFilename = sMyPrefix + TIMESTAMP_STRING + sMyExtension
global TIMESTAMP_STRING
TIMESTAMP_STRING = time.strftime("%Y_%m_%d_%H%M%S")

#=============================================================================#
# ObjectName: invert_dict
# Returns: Dictionary
#
# Description: Returns a dictionary with the vale:key pairs switched, so that
#              what were the keys are now the values, and what were the values
#              are now the keys.
#
# Note:        This method needs to remain in this module above any of DICT objects
#              so that it is accessible to those DICT's. It is a clone of the method
#              invertDict() in PyWorks_Utilities.py 
#
# Returns: dict - With Key:value pairs inverted
#
# Syntax: dDict_orig - dict - The Dictionary to be inverted
#
# Usage examples: CANADIAN_PROVINCES["MB"]#=>  "Manitoba"
#                 CANADIAN_PROVINCE_ABBREVIATION = invert_dict(CANADIAN_PROVINCES)
#                 CANADIAN_PROVINCE_ABBREVIATION["Alberta"]#=>  "AB"
#=============================================================================#
def invert_dict(dDict_orig):
    "Returns a dictionary with the value:key pairs flipped"
    dFlipped_dict = {}  # Define a new dictionary
    for key, value in dDict_orig.iteritems():
        dFlipped_dict[value] = key
    return dFlipped_dict

#=============================================================================#
# ObjectName: CANADIAN_PROVINCES
# Returns: Dictionary
#
# Description: Contains a list of Canadian  Province/Territory abbreviations
#              and their full names, from the web site:
#                 http://canadaonline.about.com/library/bl/blpabb.htm
#
# Usage examples: CANADIAN_PROVINCES["MB"] #=>  "Manitoba"
#                 CANADIAN_PROVINCE_ABBREVIATION["Manitoba"] #=>  "MB"
#=============================================================================#
global CANADIAN_PROVINCES
CANADIAN_PROVINCES = {
   "AB" : "Alberta",
   "BC" : "British Columbia",
   "MB" : "Manitoba",
   "NB" : "New Brunswick",
   "NL" : "Newfoundland and Labrador",
   "NT" : "Northwest Territories",
   "NS" : "Nova Scotia",
   "NU" : "Nunavut",
   "ON" : "Ontario",
   "PE" : "Prince Edward Island",
   "QC" : "Quebec",
   "SK" : "Saskatchewan",
   "YT" : "Yukon"
  }
  

# Dictionary with the keys and values flipped
global CANADIAN_PROVINCE_ABBREVIATION
CANADIAN_PROVINCE_ABBREVIATION = invert_dict(CANADIAN_PROVINCES)

#=============================================================================#
# ObjectName: MEXICAN_STATES
# Returns: Dictionary
#
# Description: Contains a list of Mexico's State abbreviations
#              and their full names, from the web site:
#                 http://www.iowa.gov/tax/forms/84055.pdf
#
# Usage examples: MEXICAN_STATES["BS"]#:  "Baja California Sur"
#                 MEXICAN_STATE_ABBREVIATION["Baja California Sur"] #:  "BS"
#=============================================================================#
global MEXICAN_STATES
MEXICAN_STATES = {
   "AG" : "Aguascalientes",
   "BJ" : "Baja California",
   "BS" : "Baja California Sur",
   "CP" : "Campeche",
   "CH" : "Chiapas",
   "CI" : "Chihuahua",
   "CU" : "Coahuila",
   "CL" : "Colima",
   "DF" : "Distrito Federal",
   "DG" : "Durango",
   "GJ" : "Guanajuato",
   "GR" : "Guerrero",
   "HG" : "Hidalgo",
   "JA" : "Jalisco",
   "EM" : "Mexico",
   "MH" : "Michoacan",
   "MR" : "Morelos",
   "NA" : "Nayarit",
   "NL" : "Nuevo Leon",
   "OA" : "Oaxaca",
   "PU" : "Puebla",
   "QA" : "Queretaro",
   "QR" : "Quintana Roo",
   "SL" : "San Luis Potosi",
   "SI" : "Sinaloa",
   "SO" : "Sonora",
   "TA" : "Tabasco",
   "TM" : "Tamaulipas",
   "TL" : "Tlaxcala",
   "VZ" : "Veracruz",
   "YC" : "Yucatan",
   "ZT" : "Zacatecas"
  }
  
# Dictionary with the keys and values flipped
global MEXICAN_STATE_ABBREVIATION
MEXICAN_STATE_ABBREVIATION = invert_dict(MEXICAN_STATES)

#=============================================================================#
# ObjectName: USPS_STATES
# Returns: Dictionary
#
# Description: Contains a list of State abbreviations and their full names
#              from the  United States Postal Service web site:
#                 http:www.usps.com/ncsc/lookups/usps_abbreviations.html
#
# Usage examples: USPS_STATES["CO"]#:  "Colorado"
#                 USPS_STATE_ABBREVIATION["Colorado"] #:  "CO"
#=============================================================================#
global USPS_STATES
USPS_STATES = {
   "AL" : "Alabama",
   "AK" : "Alaska",
   "AS" : "American Samoa",
   "AZ" : "Arizona",
   "AR" : "Arkansas",
   "CA" : "California",
   "CO" : "Colorado",
   "CT" : "Connecticut",
   "DE" : "Delaware",
   "DC" : "District of Columbia",
   "FM" : "Federated States of Micronesia",
   "FL" : "Florida",
   "GA" : "Georgia",
   "GU" : "Guam",
   "HI" : "Hawaii",
   "ID" : "Idaho",
   "IL" : "Illinois",
   "IN" : "Indiana",
   "IA" : "Iowa",
   "KS" : "Kansas",
   "KY" : "Kentucky",
   "LA" : "Louisiana",
   "ME" : "Maine",
   "MH" : "Marshall Islands",
   "MD" : "Maryland",
   "MA" : "Massachusetts",
   "MI" : "Michigan",
   "MN" : "Minnesota",
   "MS" : "Mississippi",
   "MO" : "Missouri",
   "MT" : "Montana",
   "NE" : "Nebraska",
   "NH" : "New Hampshire",
   "NJ" : "New Jersey",
   "NM" : "New Mexico",
   "NY" : "New York",
   "NC" : "North Carolina",
   "ND" : "North Dakota",
   "NV" : "Nevada",
   "MP" : "Northern Mariana Islands",
   "OH" : "Ohio",
   "OK" : "Oklahoma",
   "OR" : "Oregon",
   "PW" : "Palau",
   "PA" : "Pennsylvania",
   "PR" : "Puerto Rico",
   "RI" : "Rhode Island",
   "SC" : "South Carolina",
   "SD" : "South Dakota",
   "TN" : "Tennessee",
   "TX" : "Texas",
   "UT" : "Utah",
   "VI" : "Virgin Islands",
   "VA" : "Virginia",
   "WA" : "Washington",
   "WV" : "West Virginia",
   "WI" : "Wisconsin",
   "WY" : "Wyoming"
  }
  
# Dictionary with the keys and values flipped
global USPS_STATE_ABBREVIATION
USPS_STATE_ABBREVIATION = invert_dict(USPS_STATES)
  
#=============================================================================#
# ObjectName: USPS_SECONDARY_UNIT_DESIGNATOR
# Returns: Dictionary
#
# Description: Contains a list of Secondary Unit Designators and their abbreviations
#              from the United States Postal Service web site:
#                 http:www.usps.com/ncsc/lookups/usps_abbreviations.html
#
# Usage examples: USPS_SECONDARY_UNIT_DESIGNATOR["PENTHOUSE"] # : "PH"
#                 USPS_SECONDARY_UNIT_DESIGNATOR_ABBREVIATION["PH"] #: "PENTHOUSE"
#=============================================================================#
global USPS_SECONDARY_UNIT_DESIGNATOR
USPS_SECONDARY_UNIT_DESIGNATOR = {
    "APARTMENT" : "APT",
    "BASEMENT" : "BSMT",
    "BUILDING" : "BLDG",
    "DEPARTMENT" : "DEPT",
    "FLOOR" : "FL",
    "FRONT" : "FRNT",
    "HANGAR" : "HNGR",
    "LOBBY" : "LBBY",
    "LOT" : "LOT",
    "LOWER" : "LOWR",
    "OFFICE"	: "OFC",
    "PENTHOUSE" : "PH",
    "PIER" : "PIER",
    "REAR" : "REAR",
    "ROOM" : "RM",
    "SIDE" : "SIDE",
    "SLIP" : "SLIP",
    "SPACE" : "SPC",
    "STOP" : "STOP",
    "SUITE" : "STE",
    "TRAILER" : "TRLR",
    "UNIT" : "UNIT",
    "UPPER" : "UPPR"
  }

# Dictionary with the keys and values flipped
global USPS_SECONDARY_UNIT_DESIGNATOR_ABBREVIATION
USPS_SECONDARY_UNIT_DESIGNATOR_ABBREVIATION = invert_dict(USPS_SECONDARY_UNIT_DESIGNATOR)
  
#=============================================================================#
# ObjectName: USPS_STREET_SUFFIX
# Returns: Dictionary
#
# Description: Contains a list of Street Suffixes and their abbreviations
#              from the United States Postal Service web site:
#                 http:www.usps.com/ncsc/lookups/usps_abbreviations.html
#
# Usage examples: USPS_STREET_SUFFIX["DRIVE"] # : "DR"
#                 USPS_STREET_SUFFIX_ABBREVIATION["DR"] #: "DRIVE"
#=============================================================================#
global USPS_STREET_SUFFIX
USPS_STREET_SUFFIX = {
   'ALLEY' :'ALY',
   'ANNEX' : ' ANX',
   'ARCADE' : 'ARC',
   'AVENUE' : 'AVE',
   'BAYOO' : 'BYU',
   'BEACH' : 'BCH',
   'BEND' : 'BND',
   'BLUFF' : 'BLF',
   'BLUFFS' : 'BLFS',
   'BOTTOM' : 'BTM',
   'BOULEVARD' : 'BLVD',
   'BRANCH' : 'BR',
   'BRIDGE' : 'BRG',
   'BROOK' : 'BRK',
   'BROOKS' : 'BRKS',
   'BURG' : 'BG',
   'BURGS' : 'BGS',
   'BYPASS' : 'BYP',
   'CAMP' : 'CP',
   'CANYON' : 'CYN',
   'CAPE' : 'CPE',
   'CAUSEWAY' : 'CSWY',
   'CENTER' : 'CTR',
   'CENTERS' : 'CTRS',
   'CIRCLE' : 'CIR',
   'CIRCLES' : 'CIRS',
   'CLIFF' : 'CLF',
   'CLIFFS' : 'CLFS',
   'CLUB' : 'CLB',
   'COMMON' : 'CMN',
   'CORNER' : 'COR',
   'CORNERS' : 'CORS',
   'COURSE' : 'CRSE',
   'COURT' : 'CT',
   'COURTS' : 'CTS',
   'COVE' : 'CV',
   'COVES' : 'CVS',
   'CREEK' : 'CRK',
   'CRESCENT' : 'CRES',
   'CREST' : 'CRST',
   'CROSSING' : 'XING',
   'CROSSROAD' : 'XRD',
   'CURVE' : 'CURV',
   'DALE' : 'DL',
   'DAM' : 'DM',
   'DIVIDE' : 'DV',
   'DRIVE' : 'DR',
   'DRIVES' : 'DRS',
   'ESTATE' : 'EST',
   'ESTATES' : 'ESTS',
   'EXPRESSWAY' : 'EXPY',
   'EXTENSION' : 'EXT',
   'EXTENSIONS' : 'EXTS',
   'FALL' : 'FALL',
   'FALLS' : 'FLS',
   'FERRY' : 'FRY',
   'FIELD' : 'FLD',
   'FIELDS' : 'FLDS',
   'FLAT' : 'FLT',
   'FLATS' : 'FLTS',
   'FORD' : 'FRD',
   'FORDS' : 'FRDS',
   'FOREST' : 'FRST',
   'FORGE' : 'FRG',
   'FORGES' : 'FRGS',
   'FORK' : 'FRK',
   'FORKS' : 'FRKS',
   'FORT' : 'FT',
   'FREEWAY' : 'FWY',
   'GARDEN' : 'GDN',
   'GARDENS' : 'GDNS',
   'GATEWAY' : 'GTWY',
   'GLEN' : 'GLN',
   'GLENS' : 'GLNS',
   'GREEN' : 'GRN',
   'GREENS' : 'GRNS',
   'GROVE' : 'GRV',
   'GROVES' : 'GRVS',
   'HARBOR' : 'HBR',
   'HARBORS' : 'HBRS',
   'HAVEN' : 'HVN',
   'HEIGHTS' : 'HTS',
   'HIGHWAY' : 'HWY',
   'HILL' : 'HL',
   'HILLS' : 'HLS',
   'HOLLOW' : 'HOLW',
   'INLET' : 'INLT',
   'ISLAND' : 'IS',
   'ISLANDS' : 'ISS',
   'ISLE' : 'ISLE',
   'JUNCTION' : 'JCT',
   'JUNCTIONS' : 'JCTS',
   'KEY' : 'KY',
   'KEYS' : 'KYS',
   'KNOLL' : 'KNL',
   'KNOLLS' : 'KNLS',
   'LAKE ' : 'LK',
   'LAKES' : 'LKS',
   'LAND' : 'LAND',
   'LANDING' : 'LNDG',
   'LANE' : 'LN',
   'LIGHT' : 'LGT',
   'LIGHTS' : 'LGTS',
   'LOAF' : 'LF',
   'LOCK' : 'LCK',
   'LOCKS' : 'LCKS',
   'LODGE' : 'LDG',
   'LOOP' : 'LOOP',
   'MALL' : 'MALL',
   'MANOR' : 'MNR',
   'MANORS' : 'MNRS',
   'MEADOW' : 'MDW',
   'MEADOWS' : 'MDWS',
   'MEWS' : '	MEWS',
   'MILL' : 'ML',
   'MILLS' : 'MLS',
   'MISSION' : 'MSN',
   'MOTORWAY' : 'MTWY',
   'MOUNT' : 'MT',
   'MOUNTAIN' : 'MTN',
   'MOUNTAINS' : 'MTNS',
   'NECK' : 'NCK',
   'ORCHARD' : 'ORCH',
   'OVAL' : 'OVAL',
   'OVERPASS' : 'OPAS',
   'PARK' : 'PARK',
   'PARKWAY' : 'PKWY',
   'PARKWAYS' : 'PKWY',
   'PASS' : 'PASS',
   'PASSAGE' : 'PSGE',
   'PATH' : 'PATH',
   'PIKE' : 'PIKE',
   'PINE' : 'PNE',
   'PINES' : 'PNES',
   'PLACE' : 'PL',
   'PLAIN' : 'PLN',
   'PLAINS' : 'PLNS',
   'PLAZA' : 'PLZ',
   'POINT' : 'PT',
   'POINTS' : 'PTS',
   'PORT' : 'PRT',
   'PORTS' : 'PRTS',
   'PRAIRIE' : 'PR',
   'RADIAL' : 'RADL',
   'RAMP' : 'RAMP',
   'RANCH' : 'RNCH',
   'RAPID' : 'RPD',
   'RAPIDS' : 'RPDS',
   'REST' : 'RST',
   'RIDGE' : 'RDG',
   'RIDGES' : 'RDGS',
   'RIVER' : 'RIV',
   'ROAD' : 'RD',
   'ROADS' : 'RDS',
   'ROUTE' : 'RTE',
   'ROW' : 'ROW',
   'RUE' : 'RUE',
   'RUN' : 'RUN',
   'SHOAL' : 'SHL',
   'SHOALS' : 'SHLS',
   'SHORE' : 'SHR',
   'SHORES' : 'SHRS',
   'SKYWAY' : 'SKWY',
   'SPRING' : 'SPG',
   'SPRINGS' : 'SPGS',
   'SPUR' : 'SPUR',
   'SPURS' : 'SPUR',
   'SQUARE' : 'SQ',
   'SQUARES' : 'SQS',
   'STATION' : 'STA',
   'STRAVENUE' : 'STRA',
   'STREAM' : 'STRM',
   'STREET' : 'ST',
   'STREETS' : 'STS',
   'SUMMIT' : 'SMT',
   'TERRACE' : 'TER',
   'THROUGHWAY' : 'TRWY',
   'TRACE' : 'TRCE',
   'TRACK' : 'TRAK',
   'TRAFFICWAY' : 'TRFY',
   'TRAIL' : 'TRL',
   'TUNNEL' : 'TUNL',
   'TURNPIKE' : 'TPKE',
   'UNDERPASS' : 'UPAS',
   'UNION' : 'UN',
   'UNIONS' : 'UNS',
   'VALLEY' : 'VLY',
   'VALLEYS' : 'VLYS',
   'VIADUCT' : 'VIA',
   'VIEW' : 'VW',
   'VIEWS' : 'VWS',
   'VILLAGE' : 'VLG',
   'VILLAGES' : 'VLGS',
   'VILLE' : 'VL',
   'VISTA' : 'VIS',
   'WALK' : 'WALK',
   'WALKS' : 'WALK',
   'WALL' : 'WALL',
   'WAY' : 'WAY',
   'WAYS' : 'WAYS',
   'WELL' : 'WL',
   'WELLS' : 'WLS'
  }

# Dictionary with the keys and values flipped
global USPS_STREET_SUFFIX_ABBREVIATION
USPS_STREET_SUFFIX_ABBREVIATION = invert_dict(USPS_STREET_SUFFIX)


#=============================================================================#
# ObjectName: COUNTRY_CODES
# Returns: Dictionary
#
# Description: Contains a list of Country Code abbreviations
#              The 3-character codes are supplied by UN which also 
#              and numerical codes to identify nations. 
#
#              From the web site:
#                   http://www.worldatlas.com/aatlas/ctycodes.htm
#
# Usage examples: COUNTRY_CODES["USA"] # : "United States of America"
#                 COUNTRY_CODES_ABBREVIATION["United Arab Emirates"] #: "UAE"
#=============================================================================#
global COUNTRY_CODES
COUNTRY_CODES = {
    "Afghanistan":"AFG",
    "Albania":"ALB",
    "Algeria":"DZA",
    "American Samoa":"ASM",
    "Andorra":"AND",
    "Angola":"AGO",
    "Anguilla":"AIA",
    "Antarctica":"ATA",
    "Antigua and Barbuda":"ATG",
    "Argentina":"ARG",
    "Armenia":"ARM",
    "Aruba":"ABW",
    "Australia":"AUS",
    "Austria":"AUT",
    "Azerbaijan":"AZE",
    "Bahamas":"BHS",
    "Bahrain":"BHR",
    "Bangladesh":"BGD",
    "Barbados":"BRB",
    "Belarus":"BLR",
    "Belgium":"BEL",
    "Belize":"BLZ",
    "Benin":"BEN",
    "Bermuda":"BMU",
    "Bhutan":"BTN",
    "Bolivia":"BOL",
    "Bosnia and Herzegowina":"BIH",
    "Botswana":"BWA",
    "Bouvet Island":"BVT",
    "Brazil":"BRA",
    "British Indian Ocean Territory":"IOT",
    "Brunei Darussalam":"BRN",
    "Bulgaria":"BGR",
    "Burkina Faso":"BFA",
    "Burundi":"BDI",
    "Cambodia":"KHM",
    "Cameroon":"CMR",
    "Canada":"CAN",
    "Cape Verde":"CPV",
    "Cayman Islands":"CYM",
    "Central African Republic":"CAF",
    "Chad":"TCD",
    "Chile":"CHL",
    "China":"CHN",
    "Christmas Island":"CXR",
    "Cocos (Keeling) Islands":"CCK",
    "Colombia":"COL",
    "Comoros":"COM",
    "Congo":"COG",
    "Congo, the DRC":"COD",
    "Cook Islands":"COK",
    "Costa Rica":"CRI",
    "Cote d'Ivoire":"CIV",
    "Croatia (Hrvatska)":"HRV",
    "Cuba":"CUB",
    "Cyprus":"CYP",
    "Czech Republic":"CZE",
    "Denmark":"DNK",
    "Djibouti":"DJI",
    "Dominica":"DMA",
    "Dominican Republic":"DOM",
    "East Timor":"TMP",
    "Ecuador":"ECU",
    "Egypt":"EGY",
    "El Salvador":"SLV",
    "Equatorial Guinea":"GNQ",
    "Eritrea":"ERI",
    "Estonia":"EST",
    "Ethiopia":"ETH",
    "Falkland islands (Malvinas)":"FLK",
    "Faroe Islands":"FRO",
    "Fiji":"FJI",
    "Finland":"FIN",
    "France":"FRA",
    "France, Metropolitan":"FXX",
    "French Guiana":"GUF",
    "French Polynesia":"PYF",
    "French Southern Territories":"ATF",
    "Gabon":"GAB",
    "Gambia":"GMB",
    "Georgia":"GEO",
    "Germany":"DEU",
    "Ghana":"GHA",
    "Gibraltar":"GIB",
    "Greece":"GRC",
    "Greenland":"GRL",
    "Grenada":"GRD",
    "Guadeloupe":"GLP",
    "Guam":"GUM",
    "Guatemala":"GTM",
    "Guinea":"GIN",
    "Guinea-Bissau":"GNB",
    "Guyana":"GUY",
    "Haiti":"HTI",
    "Heard and Mc Donald Islands":"HMD",
    "Holy See (Vatican City State)":"VAT",
    "Honduras":"HND",
    "Hong Kong":"HKG",
    "Hungary":"HUN",
    "Iceland":"ISL",
    "India":"IND",
    "Indonesia":"IDN",
    "Iran (Islamic Republic of)":"IRN",
    "Iraq":"IRQ",
    "Ireland":"IRL",
    "Israel":"ISR",
    "Italy":"ITA",
    "Jamaica":"JAM",
    "Japan":"JPN",
    "Jordan":"JOR",
    "Kazakhstan":"KAZ",
    "Kenya":"KEN",
    "Kiribati":"KIR",
    "Korea, D.P.R.O.":"PRK",
    "Korea, Republic of":"KOR",
    "Kuwait":"KWT",
    "Kyrgyzstan":"KGZ",
    "Laos":"LAO",
    "Latvia":"LVA",
    "Lebanon":"LBN",
    "Lesotho":"LSO",
    "Liberia":"LBR",
    "Libyan Arab Jamahiriya":"LBY",
    "Liechtenstein":"LIE",
    "Lithuania":"LTU",
    "Luxembourg":"LUX",
    "Macau":"MAC",
    "Macedonia":"MKD",
    "Madagascar":"MDG",
    "Malawi":"MWI",
    "Malaysia":"MYS",
    "Maldives":"MDV",
    "Mali":"MLI",
    "Malta":"MLT",
    "Marshall Islands":"MHL",
    "Martinique":"MTQ",
    "Mauritania":"MRT",
    "Mauritius":"MUS",
    "Mayotte":"MYT",
    "Mexico":"MEX",
    "Micronesia, Federated States of":"FSM",
    "Moldova, Republic of":"MDA",
    "Monaco":"MCO",
    "Mongolia":"MNG",
    "Montserrat":"MSR",
    "Morocco":"MAR",
    "Mozambique":"MOZ",
    "Myanmar (Burma)":"MMR",
    "Namibia":"NAM",
    "Nauru":"NRU",
    "Nepal":"NPL",
    "Netherlands":"NLD",
    "Netherlands antilles":"ANT",
    "New Caledonia":"NCL",
    "New Zealand":"NZL",
    "Nicaragua":"NIC",
    "Niger":"NER",
    "Nigeria":"NGA",
    "Niue":"NIU",
    "Norfolk Island":"NFK",
    "Northern Mariana Islands":"MNP",
    "Norway":"NOR",
    "Oman":"OMN",
    "Pakistan":"PAK",
    "Palau":"PLW",
    "Panama":"PAN",
    "Papua New Guinea":"PNG",
    "Paraguay":"PRY",
    "Peru":"PER",
    "Philippines":"PHL",
    "Pitcairn":"PCN",
    "Poland":"POL",
    "Portugal":"PRT",
    "Puerto Rico":"PRI",
    "Qatar":"QAT",
    "Reunion":"REU",
    "Romania":"ROM",
    "Russian Federation":"RUS",
    "Rwanda":"RWA",
    "Saint Kitts and Nevis":"KNA",
    "Saint Lucia":"LCA",
    "Saint Vincent and the Grenadines":"VCT",
    "Samoa":"WSM",
    "San Marino":"SMR",
    "Sao Tome and Principe":"STP",
    "Saudi Arabia":"SAU",
    "Senegal":"SEN",
    "Seychelles":"SYC",
    "Sierra Leone":"SLE",
    "Singapore":"SGP",
    "Slovakia (Slovak Republic)":"SVK",
    "Slovenia":"SVN",
    "Solomon Islands":"SLB",
    "Somalia":"SOM",
    "South Africa":"ZAF",
    "South Georgia and South S.S.":"SGS",
    "Spain":"ESP",
    "Sri Lanka":"LKA",
    "St. Helena":"SHN",
    "St. Pierre and Miquelon":"SPM",
    "Sudan":"SDN",
    "Suriname":"SUR",
    "Svalbard and Jan Mayen Islands":"SJM",
    "Swaziland":"SWZ",
    "Sweden":"SWE",
    "Switzerland":"CHE",
    "Syrian Arab Republic":"SYR",
    "Taiwan, Province of China":"TWN",
    "Tajikistan":"TJK",
    "Tanzania, United Republic of":"TZA",
    "Thailand":"THA",
    "Togo":"TGO",
    "Tokelau":"TKL",
    "Tonga":"TON",
    "Trinidad and Tobago":"TTO",
    "Tunisia":"TUN",
    "Turkey":"TUR",
    "Turkmenistan":"TKM",
    "Turks and Caicos Islands":"TCA",
    "Tuvalu":"TUV",
    "Uganda":"UGA",
    "Ukraine":"UKR",
    "United Arab Emirates":"ARE",
    "United Kingdom":"GBR",
    "United States":"USA",
    "U.s. Minor Islands":"UMI",
    "Uruguay":"URY",
    "Uzbekistan":"UZB",
    "Vanuatu":"VUT",
    "Venezuela":"VEN",
    "Viet Nam":"VNM",
    "Virgin Islands (British)":"VGB",
    "Virgin Islands (U.S.)":"VIR",
    "Wallis and Futuna Islands":"WLF",
    "Western Sahara":"ESH",
    "Yemen":"YEM",
    "Yugoslavia (Serbia and Montenegro)":"YUG",
    "Zambia":"ZMB",
    "Zimbabwe ":"ZWE"
    }


# Dictionary with the keys and values flipped
global COUNTRY_CODES_ABBREVIATION
COUNTRY_CODES_ABBREVIATION = invert_dict(COUNTRY_CODES)

#=============================================================================#
# ObjectName: COUNTRY_CODES_2CHAR
# Returns: Dictionary
#
# Description: Contains a list of Country Code abbreviations
#              The 2-character codes are supplied by the ISO 
#              (International Organization for Standardization),
#              which bases its list of country names and abbreviations on
#              the list of names published by the United Nations. 
#              The UN also uses uses 3-letter codes, and numerical codes to
#              identify nations. 
#
#              From the web site:
#                   http://www.worldatlas.com/aatlas/ctycodes.htm
#
# Usage examples: COUNTRY_CODES_2CHAR["US"] # : "United States"
#                 COUNTRY_CODES_2CHAR_ABBREVIATION["United Arab Emirates"] #: "AE"
#=============================================================================#
global COUNTRY_CODES_2CHAR
COUNTRY_CODES_2CHAR = {
    "AC":"Ascension Island",
    "AD":"Andorra",
    "AE":"United Arab Emirates",
    "AF":"Afghanistan",
    "AG":"Antigua and Barbuda",
    "AI":"Anguilla",
    "AL":"Albania",
    "AM":"Armenia",
    "AN":"Netherlands Antilles",
    "AO":"Angola",
    "AQ":"Antarctica",
    "AR":"Argentina",
    "AS":"American Samoa",
    "AT":"Austria",
    "AU":"Australia",
    "AW":"Aruba",
    "AZ":"Azerbaijan",
    "BA":"Bosnia and Herzegovina",
    "BB":"Barbados",
    "BD":"Bangladesh",
    "BE":"Belgium",
    "BF":"Burkina Faso",
    "BG":"Bulgaria",
    "BH":"Bahrain",
    "BI":"Burundi",
    "BJ":"Benin",
    "BM":"Bermuda",
    "BN":"Brunei Darussalam",
    "BO":"Bolivia",
    "BR":"Brazil",
    "BS":"Bahamas",
    "BT":"Bhutan",
    "BV":"Bouvet Island",
    "BW":"Botswana",
    "BY":"Belarus",
    "BZ":"Belize",
    "CA":"Canada",
    "CC":"Cocos (Keeling Islands)",
    "CF":"Central African Republic",
    "CG":"Congo",
    "CH":"Switzerland",
    "CI":"Cote D'Ivoire (Ivory Coast)",
    "CK":"Cook Islands",
    "CL":"Chile",
    "CM":"Cameroon",
    "CN":"China",
    "CO":"Colombia",
    "CR":"Costa Rica",
    "CU":"Cuba",
    "CV":"Cape Verde",
    "CX":"Christmas Island",
    "CY":"Cyprus",
    "CZ":"Czech Republic",
    "DE":"Germany",
    "DJ":"Djibouti",
    "DK":"Denmark",
    "DM":"Dominica",
    "DO":"Dominican Republic",
    "DZ":"Algeria",
    "EC":"Ecuador",
    "EE":"Estonia",
    "EG":"Egypt",
    "EH":"Western Sahara",
    "ER":"Eritrea",
    "ES":"Spain",
    "ET":"Ethiopia",
    "EU":"Europe",
    "FI":"Finland",
    "FJ":"Fiji",
    "FK":"Falkland Islands (Malvinas)",
    "FM":"Micronesia",
    "FO":"Faroe Islands",
    "FR":"France",
    "FX":"France, Metropolitan",
    "GA":"Gabon",
    "GB":"United Kingdom",
    "GD":"Grenada",
    "GE":"Georgia",
    "GF":"French Guiana",
    "GH":"Ghana",
    "GI":"Gibraltar",
    "GL":"Greenland",
    "GM":"Gambia",
    "GN":"Guinea",
    "GP":"Guadeloupe",
    "GQ":"Equatorial Guinea",
    "GR":"Greece",
    "GS":"S. Georgia and S. Sandwich Isls.",
    "GT":"Guatemala",
    "GU":"Guam",
    "GW":"Guinea-Bissau",
    "GY":"Guyana",
    "HK":"Hong Kong",
    "HM":"Heard and McDonald Islands",
    "HN":"Honduras",
    "HR":"Croatia (Hrvatska)",
    "HT":"Haiti",
    "HU":"Hungary",
    "ID":"Indonesia",
    "IE":"Ireland",
    "IL":"Israel",
    "IN":"India",
    "IO":"British Indian Ocean Territory",
    "IQ":"Iraq",
    "IR":"Iran",
    "IS":"Iceland",
    "IT":"Italy",
    "JM":"Jamaica",
    "JO":"Jordan",
    "JP":"Japan",
    "KE":"Kenya",
    "KG":"Kyrgyzstan (Kyrgyz Republic)",
    "KH":"Cambodia",
    "KI":"Kiribati",
    "KM":"Comoros",
    "KN":"Saint Kitts and Nevis",
    "KP":"Korea (North) (People's Republic)",
    "KR":"Korea (South) (Republic)",
    "KW":"Kuwait",
    "KY":"Cayman Islands",
    "KZ":"Kazakhstan",
    "LA":"Laos",
    "LB":"Lebanon",
    "LC":"Saint Lucia",
    "LI":"Liechtenstein",
    "LK":"Sri Lanka",
    "LR":"Liberia",
    "LS":"Lesotho",
    "LT":"Lithuania",
    "LU":"Luxembourg",
    "LV":"Latvia",
    "LY":"Libya",
    "MA":"Morocco",
    "MC":"Monaco",
    "MD":"Moldova",
    "MG":"Madagascar",
    "MH":"Marshall Islands",
    "MK":"Macedonia",
    "ML":"Mali",
    "MM":"Myanmar",
    "MN":"Mongolia",
    "MO":"Macau",
    "MP":"Northern Mariana Islands",
    "MQ":"Martinique",
    "MR":"Mauritania",
    "MS":"Montserrat",
    "MT":"Malta",
    "MU":"Mauritius",
    "MV":"Maldives",
    "MW":"Malawi",
    "MX":"Mexico",
    "MY":"Malaysia",
    "MZ":"Mozambique",
    "NA":"Namibia",
    "NC":"New Caledonia",
    "NE":"Niger",
    "NF":"Norfolk Island",
    "NG":"Nigeria",
    "NI":"Nicaragua",
    "NL":"Netherlands",
    "NO":"Norway",
    "NP":"Nepal",
    "NR":"Nauru",
    "NT":"Neutral Zone (Saudia Arabia/Iraq)",
    "NU":"Niue",
    "NZ":"New Zealand",
    "OM":"Oman",
    "PS":"Palestine",
    "PA":"Panama",
    "PE":"Peru",
    "PF":"French Polynesia",
    "PG":"Papua New Guinea",
    "PH":"Philippines",
    "PK":"Pakistan",
    "PL":"Poland",
    "PM":"St. Pierre and Miquelon",
    "PN":"Pitcairn",
    "PR":"Puerto Rico",
    "PT":"Portugal",
    "PW":"Palau",
    "PY":"Paraguay",
    "QA":"Qatar",
    "RE":"Reunion",
    "RO":"Romania",
    "RU":"Russian Federation",
    "RW":"Rwanda",
    "SA":"Saudi Arabia",
    "SB":"Solomon Islands",
    "SC":"Seychelles",
    "SD":"Sudan",
    "SE":"Sweden",
    "SG":"Singapore",
    "SH":"St. Helena",
    "SI":"Slovenia",
    "SJ":"Svalbard and Jan Mayen Islands",
    "SK":"Slovakia (Slovak Republic)",
    "SL":"Sierra Leone",
    "SM":"San Marino",
    "SN":"Senegal",
    "SO":"Somalia",
    "SR":"Suriname",
    "ST":"Sao Tome and Principe",
    "SU":"Soviet Union (former)",
    "SV":"El Salvador",
    "SY":"Syria",
    "SZ":"Swaziland",
    "TC":"Turks and Caicos Islands",
    "TD":"Chad",
    "TF":"French Southern Territories",
    "TG":"Togo",
    "TH":"Thailand",
    "TJ":"Tajikistan",
    "TK":"Tokelau",
    "TM":"Turkmenistan",
    "TN":"Tunisia",
    "TO":"Tonga",
    "TP":"East Timor",
    "TR":"Turkey",
    "TT":"Trinidad and Tobago",
    "TV":"Tuvalu",
    "TW":"Taiwan",
    "TZ":"Tanzania",
    "UA":"Ukraine",
    "UG":"Uganda",
    "UK":"United Kingdom (Great Britain)",
    "US":"United States",
    "UY":"Uruguay",
    "UZ":"Uzbekistan",
    "VA":"Vatican City State (Holy See)",
    "VC":"Saint Vincent and The Grenadines",
    "VE":"Venezuela",
    "VG":"Virgin Islands (British)",
    "VI":"Virgin Islands (US)",
    "VN":"Viet Nam",
    "VU":"Vanuatu",
    "WF":"Wallis and Futuna Islands",
    "WS":"Samoa",
    "YE":"Yemen",
    "YT":"Mayotte",
    "YU":"Yugoslavia",
    "ZA":"South Africa",
    "ZM":"Zambia",
    "ZR":"Zaire",
    "ZW":"Zimbabwe"
    }

# Dictionary with the keys and values flipped
global COUNTRY_CODES_2CHAR_ABBREVIATION
COUNTRY_CODES_2CHAR_ABBREVIATION = invert_dict(COUNTRY_CODES_2CHAR)

#=============================================================================#
# ObjectName: MONTH_ABBREVIATION
# Returns: Dictionary
#
# Description: Contains a list of month abbreviations and their full names
#
# Usage examples: MONTH_ABBREVIATION["December"] # : "dec"
#                 MONTHS["dec"] #: "December"
#=============================================================================#
global MONTH_ABBREVIATION
MONTH_ABBREVIATION = {
   "jan" : "Janurary",
   "feb" : "Feburary",
   "mar" : "March",
   "apr" : "April",
   "may" : "May",
   "jun" : "June",
   "jul" : "July",
   "aug" : "August",
   "sep" : "September",
   "oct" : "October",
   "nov" : "November",
   "dec" : "December"
  }
  
# Dictionary with the keys and values flipped
global MONTHS
MONTHS = invert_dict(MONTH_ABBREVIATION)
  
#=============================================================================#
# ObjectName: TOP_LEVEL_DOMAINS
# Returns: list
#
# Description: Contains a list of Top Level Domain names as found at:
#                 http://www.icann.org/registries/top-level-domains.htm
#
# Usage examples:
#                 sMy_TLD = "biz"
#                 for sTLD in TOP_LEVEL_DOMAINS:
#                     if(sMy_TLD == sTLD)
#                         print2("Valid Top-Level-Domain = " + sMy_TLD)
#                     else:
#                         print2("INVALID Top-Level-Domain = " + sMy_TLD)
#                     # end
#                 # end
#=============================================================================#
global TOP_LEVEL_DOMAINS
TOP_LEVEL_DOMAINS = [
  "aero", "arpa", "asia", "biz", "cat", "com", "coop", "info", "jobs",
  "mobi", "museum", "name", "net", "org", "pro", "tel", "travel",
  "gov", "edu", "mil", "int",
  "ac", "ad", "ae", "af", "ag", "ai", "al", "am", "an", "ao", "aq", "ar", "as", "at", "au", "aw", "ax", "az",
  "ba", "bb", "bd", "be", "bf", "bg", "bh", "bi", "bj", "bm", "bn", "bo", "br", "bs", "bt", "bv", "bw", "by", "bz",
  "ca", "cc", "cd", "cf", "cg", "ch", "ci", "ck", "cl", "cm", "cn", "cp", "cr", "cu", "cv", "cx", "cz",
  "de", "dj", "dk", "dm", "do", "dz",
  "ec", "ee", "eg", "er", "es", "et", "eu",
  "fi", "fj", "fk", "fm", "fo", "fr",
  "ga", "gb", "gd", "ge", "gf", "gg", "gh", "gi", "gl", "gm", "gn", "gp", "gq", "gr", "gs", "gt", "gu", "gw", "gy",
  "hk", "hm", "hn", "hr", "ht", "hu",
  "id", "ie", "il", "im", "in", "io", "iq", "ir", "is", "it",
  "je", "jm", "jo", "jp",
  "ke", "kg", "kh", "ki", "km", "kn", "kr", "kw", "ky", "kz",
  "la", "lb", "lc", "li", "lk", "lr", "ls", "lt", "lu", "lv", "ly",
  "ma", "md", "mg", "mh", "mk", "ml", "mm", "mn", "mo", "mp", "mr", "ms", "mt", "mu", "mv", "mw", "mz",
  "na", "nc", "ne", "nf", "ng", "ni", "nl", "no", "np", "nr", "nu", "nz",
  "om",
  "pa", "pe", "pf", "pg", "ph", "pk", "pl", "pm", "pn", "pr", "ps", "pt", "pw", "py",
  "qa",
  "re", "ro", "ru", "rw",
  "sa", "sb", "sc", "sd", "se", "sg", "sh", "si", "sj", "sk", "sl", "sm", "sn", "so", "sr", "st", "su", "sv", "sy", "sz",
  "tc", "td", "tf", "tg", "th", "tj", "tk", "tl", "tm", "tn", "to", "tp", "tr", "tt", "tv", "tw", "tz",
  "ua", "ug", "uk", "um", "us", "uy", "uz",
  "va", "vc", "ve", "vg", "vi", "vn", "vu",
  "wf", "ws",
  "ye", "yt", "yu",
  "za", "zm", "zw"
  ]



# END FILE PyWorks_Reflib.py
