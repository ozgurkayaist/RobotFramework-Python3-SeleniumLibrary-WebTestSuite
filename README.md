# RobotFramework-Python3-SeleniumLibrary-WebTestSuite


Tested on:
------------------
Robot Framework 3.1.2 (Python 3.8.1 on win32)

Python 3.8.1

SeleniumLibrary 4.1.0

Required installations:
--------------------
Python 3

pip install robotframework

pip install --upgrade robotframework-pageobjectlibrary

pip install --upgrade robotframework-seleniumlibrary

pip install webdrivermanager

webdrivermanager firefox chrome --linkpath /usr/local/bin

pip install -r requirements.txt

Running Tests Commands:
----------------------
robot tests\HepsiburadaTest.robot

robot --variable BROWSER:Chrome tests\HepsiburadaTest.robot

robot --variable BROWSER:Firefox tests\HepsiburadaTest.robot
