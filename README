
'''
PyWorks doc

Copyright (c) 2008-2011, Joe DiMauro. All rights reserved.

= Welcome to PyWorks!

== Introduction

PyWorks is a Python/Jython toolkit for SOATest.

SOATest v9.0 runs with a bundled version of Jython that is far down-rev.(Jython 2.2.1, circa July 2007),
and Java (Java v1.6.21)
These tools are also written using that same down-rev versions of Jython and Java
so that they integrate with SOATest.

Its a collection of information and utilities written in Jython for developing and executing automated Web Service tests with SOATest.
SOATest provides the ability to extend its capabilities through the use of Jython scripts.

PyWorks is focused at testers who are just starting to use Jython. As such it is highly documented to help get folks on board.
While Jython is more of a programming language than a toolkit PyWorks aims to provide several tools for your toolkit.

PyWorks provides tools to support testing .

PyWorks contains the means to:
* Aggregate unittest files into unittest suites, while still retaining the ability to run any unittest individually
* Collect output generated from a test run (log files, etc), into a common results directory
* Support Data Driven testing
* Utilize Reference data, and common methods to expedite test development

PyWorks also contains:
* A Reference library ( PyWorks_Reflib.rb ) with many useful sets of data, such as:
  * United States Postal Service abbreviations (per http://usps.com)
  * Canadian province abbreviations (per http://canadaonline.about.com)
  * Mexico State abbreviations (per www.iowa.gov/tax/forms/84055.pdf)
  * A list of Top-Level-Domains (per http://icann.org)
* A dictionary file (dictionary_en.txt) and methods to access it
* Full documentation
* Methods that add abilities to Jython:
  * General Utilities ( PyWorks_Utilities.rb )
* Unit tests for the methods and functions in the PyWorks Libraries

PyWorks runs on the Windows platform that SOATest supports.
Additionally should SOATest ever port to other platforms, PyWorks has been unit tested on:
 Linux using both Ubuntu 10.04 and Debian 5.04
 and on MAC OS/X. 

= PyWorks Unit Tests

The Unit tests can be run using an IDE like PyDev in SOATest, or through PyDev in Eclipse or other Eclipse based IDE (e.g. Aptana).
They can be run individually, or run collectively as a PyWorks testsuite.
To run them collectively as a testsuite run PyWorks_unittest_testsuite.py, otherwise run the individual test file (*.unittest.py).

The unit tests are relatively well commented to help you understand what their intended purpose.
They contain information on how to run them and what each test case is covering.

Some of the PyWorks unit tests record output to a log file.

One of the features of the PyWorks is that STDOUT and STDERR can be captured in a log file. That log file is time-stamped and resides in the folder 'results'
Each time a unit test is run, or when multiple test are run as a testsuite, the results folder from the last run
is NOT overwritten. The pre-existing results folder's is re-named by appending a time-stamp to the folder name, and a new results folder is created.
This allows the output from multiple runs to be saved, and compared against other runs.
Be sure to manually clean-up the old results folders when you are done.

The unit tests for PyWorks reside under the folder:
     <InstallDir>\PyWorks\src\Unittest


= SETUP

Prerequisites: Java, Jython, SOATest

To use PyWorks install the following:
* To use PyWorks with SOATest you will need to install SOATest 9.x
* Install Java - A version of Java is included within the SOATest installation. For example:
     C:\Program Files\Parasoft\Test\9.0\plugins\com.parasoft.xtest.jdk.eclipse.core.win32.x86_1.6.0.21\jdk\bin
* Install Jython - While a version of Jython is included within the SOATest installation. For example
     C:\Program Files\Parasoft\Test\9.0\plugins\com.parasoft.xtest.libs.base_9.0.0.20100729
  HOWEVER it is NOT a complete install. THerefore you need to download and install the full
  Jython 2.2.1 from
     http://www.jython.org/archive/21/download.html
  Install it into C:\JYthon\jython2.2.1 which is NOT the default location.
  
  
= Importing PyWorks into SOATest

Once the Prerequisites are met add PyWorks to the SOATest Workspace
* Open SOATest
* Open the PyDev Perspective
  * Windows > Open Perspective > Other ..
  * Select PyDev form the list
* From the PyDev Perspective, create a new top level project (PyWorks)
  * File > New > Project  
  * Select: PyDev > PyDev Project
    Name = PyWorks
    Project Type = Jython
    Interpreter: Select the Jython Interpreter from the C:\Jython\jython2.2.1 install tree
        C:\Jython\jython2.2.1\jython.bat
    *** IMPORTANT *** DO NOT select any of the Jython Interpreters bundled with SOAtest! For example:
         C:\Program Files\Parasoft\Test\9.0\plugins\com.parasoft.xtest.libs.base_9.0.0.20100729\jython.jar
         C:\Program Files\Parasoft\SOAtest\9.0\eclipse\plugins\com.parasoft.xtest.libs.web_9.0.0.20100729\root\jython.jar
         C:\Program Files\Parasoft\Test\9.0\plugins\com.parasoft.xtest.scripting.eclipse.core_9.0.0.20100729\jython\ython.jar
         C:\Program Files\Parasoft\Test\9.0\plugins\com.parasoft.xtest.libs.base_9.0.0.20100729\ython.jar
         C:\Program Files\Common Files\Parasoft\Pydev\1.5.9\eclipse\plugins\org.python.pydev.jython_1.5.9.2010063001\jython.jar
    They are either incomplete, down-rev, or modified for use by SOATest. This is why you should install and use the full
    Jython installation, and will be using that instalation instead.
         
* Copy the PyWorks/src/ files to new SOATest top level project (e.g. PyWorks)
* Refresh the PyWorks project in SOATest


= Using PyWorks with SOATest

PyWorks can be used from the Parasoft SOATest perspective once it was successfully installed as a Python Project
in the PyDev Perspective of SOATest.

* Open your SOAtest Project
* Select: Windows > Preferences
* Select: Parasoft > SOATest > Scripting
    Set the following: 
    Jython Home = C:\Jython\jython2.2.1
    Jython Path = C:\JYhton\jython2.2.1\Lib;<USERPROFILE>\parasoft\workspace\PyWorks\src\Lib;
     where <USERPROFILE> is you personal home. For example: C:\Documents and Settings\jxdima2;
    
* In any SOATest Jython script where the use of Pyworks is needed, add one of the following the entries:

    # Using the PyWorks_Reflib
    from PyWorks_Reflib import *    #  PyWorks Reference data module
    
    # Using multiple PyWorks methods 
    from PyWorks_Utilities import *        # PyWorks General Utilities
    
    # If using only one or a small number of PyWorks methods:
    from PyWorks import <method_1>, <method_2>, <method_3>      # PyWorks General Utilities
    
    
= Modifying PyWorks

Should it be necessary to modify or add additional methods to PyWOrks:
* Open the PyDev perspective
* Make the modification
* Run the unittests from PyDev
* Once the unittests are working bump the release number and SAVE the updated version of PyWorks
* Exit SOATest, re-start SOATest, as sometimes it caches the older version of PyWorks. 
  The restart forces SOATest to use the new version of PyWorks. 


Contributors:
   Joe DiMauro


   Thanks for your ideas and support!

'''
